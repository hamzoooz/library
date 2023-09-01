from django.shortcuts import render, redirect 
from django.http import JsonResponse
from wishlist.models import WishList
from books.models import Books
from django.contrib.auth.decorators import login_required

@login_required
def wishlist(request):
    wishlists = WishList.objects.filter(user=request.user)
    return render(request, 'wishlist/wishlist.html', {'wishlists': wishlists})

def add_to_wishlist(request):
    if request.method == "POST":
        if request.user.is_authenticated:
            book_id = int(request.POST.get('book_id'))
            book_check = Books.objects.get(id=book_id)
            if (book_check):
                if (WishList.objects.filter(user=request.user.id, book_id=book_id)):
                    return JsonResponse({'status': "Book Already in Favoret List "})
                else:
                    WishList.objects.create(user=request.user, book_id=book_id)
                    return JsonResponse({'status': "Your book added Successfuly to Favoret  "})
            else:
                return JsonResponse({'status': "No Such Book Found "})
        else:
            return JsonResponse({'status': "Login to Continue"})
    return redirect('/')


def remove_from_wishlist(request):
    if request.method == "POST":
        book_id = int(request.POST.get('book_id'))
        wishlistitem = WishList.objects.filter(user=request.user, book=book_id)
        if (wishlistitem):
            wishlistitem.delete()
        return JsonResponse({'status':'The book Removed from Favoret successfully '})

