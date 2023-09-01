from django.http.response import JsonResponse
from django.shortcuts import render, redirect
# from carts.models import Cart
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from books.models import Books
from carts.models import Cart,  Order, OrderItem
from django.contrib import messages
from users.models import Profile
import random


@login_required
def cart_view(request):
    carts = Cart.objects.filter(user=request.user)
    total_price = 0
    for item in carts:
        total_price = total_price + item.book.selling_price

    return render(request, 'carts/cart_view.html', {'carts': carts, 'total_price': total_price})

# @login_required # get error 
def add_to_cart(request):
    if request.method == 'POST':
        if request.user.is_authenticated:
            book_id = int(request.POST.get('book_id'))
            book_check = Books.objects.get(id=book_id)
            print(book_id)
            print(book_check)
            if (book_check):
                if (Cart.objects.filter(user=request.user.id, book_id=book_id)):
                    return JsonResponse({'status': "Book Already in Cart"})
                else:
                    Cart.objects.create(user=request.user, book_id=book_id)
                    return JsonResponse({'status': "Your book added Successfuly  "})
            else:
                return JsonResponse({'status': "No Such Book Found "})
        else:
            return JsonResponse({'status': "Login to Continue"})
    return redirect('/')


def remove_form_cart(request):
    if request.method == 'POST':
        book_id = int(request.POST.get('book_id'))
        if (Cart.objects.filter(user=request.user, book=book_id)):
            cartitem = Cart.objects.get(book=book_id, user=request.user)
            cartitem.delete()
        return JsonResponse({'status': "Your Cart Deleted Successfuly ..."})

# #############################
#          Checkout 
# #############################

@login_required
def checkout(request):    
    carditem = Cart.objects.filter(user=request.user)
    user_profile = Profile.objects.filter(user=request.user).first()
    total_price = 0 
    for item in carditem:
        total_price = total_price + item.book.selling_price
    return render(request, 'checkout/checkout.html', {
        'carditem': carditem,
        'total_price': total_price,
        'user_profile': user_profile,
        })
    
@login_required(login_url='login')
def placeorder(request):
    if request.method == "POST":
        user_profile = Profile.objects.filter(user=request.user).first()
        current_user = User.objects.filter(id=request.user.id).first()
        
        # check if user data complete to complate 
        if not current_user.first_name:
            current_user.first_name = request.POST.get('fname')
            current_user.save()
        if not current_user.last_name:
            current_user.save()
            current_user.last_name = request.POST.get('lname')
            current_user.save()
        if not current_user.email:
            current_user.email = request.POST.get('email')
            current_user.save()
        
        # check if user Profile data complete to complate 
        if not user_profile.phone:
            user_profile.phone = request.POST.get('phone')
            user_profile.save()
        if not user_profile.address:
            user_profile.address = request.POST.get('address')
            user_profile.save()
        if not user_profile.city:
            user_profile.city = request.POST.get('city')
            user_profile.save()
        if not user_profile.stats:
            user_profile.stats = request.POST.get('stats')
            user_profile.save()
        if not user_profile.conutry:
            user_profile.conutry = request.POST.get('conutry')
            user_profile.save()
        if not user_profile.pincode:
            user_profile.pincode = request.POST.get('pincode')
            user_profile.save()
        #  user,  fname, lname, email, phone, address, city, stats, conutry, pincode, 
        # total_price, payment_mode, payment_id, satuts, message, tracking_no, update_at
        #  Make New Order 
        
        
        new_order = Order()
        new_order.user = request.user
        new_order.fname = request.POST.get('fname')
        new_order.lname = request.POST.get('lname')
        new_order.email = request.POST.get('email')
        new_order.phone = request.POST.get('phone')
        new_order.address = request.POST.get('address')
        new_order.city = request.POST.get('city')
        new_order.stats = request.POST.get('stats')
        new_order.conutry = request.POST.get('conutry')
        new_order.pincode = request.POST.get('pincode')
        new_order.payment_mode = request.POST.get('payment_mode')
        # new_order.payment_id = request.POST.get('payment_id')

        card = Cart.objects.filter(user=request.user)
        card_total_price = 0
        for item in card:
            card_total_price = card_total_price + item.book.selling_price 
            user = item.user.username
        new_order.total_price = card_total_price
        print(user)
        # trackno = "hamzoooz" + str(random.randint(1111111, 9999999))
        trackno = user + str(random.randint(1111111, 9999999))
        while Order.objects.filter(tracking_no=trackno) is None:
            # trackno = "hamzoooz" + str(random.randint(1111111, 9999999))
            trackno = user + str(random.randint(1111111, 9999999))

        new_order.tracking_no = trackno
        new_order.save()

        # user, book, create_at, qunatity
        new_order_item = Cart.objects.filter(user=request.user)
        for item in new_order_item:
            OrderItem.objects.create(
                order=new_order,
                price=item.book.selling_price,
                book=item.book, 
        )
            
            order_book = Books.objects.filter(id=item.book_id).first()
            # order_book.quantity = order_book.quantity - item.book_qty
            order_book.save()

        # To Clear User's Cart
        Cart.objects.filter(user=request.user).delete()
        messages.success(request, 'Your Order has been placed successfuly ! ')
 
        payMode = request.POST.get('payment_mode')
        if (payMode == "Paid by Razorpay"):
            return JsonResponse({'status': 'Your Order has been placed successfuly ! '})

    return redirect('/')
    # return render(request, 'checkout/placeorder.html')
