from books.models import Books
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from users.models import Profile
from django.contrib import messages
from django.http import JsonResponse
from django.shortcuts import render
from quotes.models import Qoutes


def qoutes(request,slug):
    # quotes-section
    qoutes = Qoutes.objects.filter(slug=slug)
    return render(request, 'qoutes/qoutes.html', {'qoutes': qoutes})

def add_quote(request, slug):
    books = Books.objects.get(slug=slug)
    if request.method == "POST":
        book_id = request.POST.get('book_quote')
        text = request.POST.get('text_quote')
        
        if request.user.is_authenticated:
            user = request.user.id
            profile = Profile.objects.get(user=user)
            book = Books.objects.get(slug=slug)
            new_quote = Qoutes.objects.create( user=profile, book=book, text=text)
            new_quote.save()
            
            quotes = Qoutes.objects.filter(book=book)
            html =  render(request, 'qoutes/add_quote.html', {"books": books, "quotes": quotes, }).content
            return JsonResponse({'html': html, "status": "Comment Send successfuly ! ..."})
        else:
            # messages.info(request, "Login To contnu ...")
            return JsonResponse({"status": "Login To Continu"})    
    return render(request, 'qoutes/add_quote.html' , { "books": books, "quotes": quotes, } ) 


def delete_quote(request, pk):
    # quote_id = request.POST.get('quote_id')
    print(pk)
    if request.user.is_authenticated:
        try:
            quote = Qoutes.objects.get(id=pk)
            quote.delete()
            return JsonResponse({'success': True})
        except Qoutes.DoesNotExist:
            return JsonResponse({'success': False})
    else:
        messages.info(request, "Login To contnu ...")
        return JsonResponse({"status": "Login To Continu"})
