from django.shortcuts import render
from django.http import HttpResponse , JsonResponse
from django.db.models import Q
from books.models import Books, Category 
def search(request):
    query = request.GET.get('productsearch', '')
    
    books = Books.objects.filter(
        Q(name__icontains=query) |
        Q(meta_description__icontains=query) |
        Q(meta_tilte__icontains=query) |
        Q(meta_keyword__icontains=query) |
        Q(meta_description__icontains=query) |
        # Q(category__icontains=query) |
        Q(isnn__icontains=query) |
        # Q(user__icontains=query) |
        Q(published_house__icontains=query) |
        Q(tags__icontains=query) |
        Q(create_at__icontains=query) , 
        available='publised'
        )

    return render(request, 'search/search.html', {
        'query':query,
        'books':books,
    })

def book_list(request):
    books = Books.objects.filter(available='publised').values_list('name' , flat=True)
    book_list = list(books)[0:100]
    # book_list = list(books)

    return JsonResponse(book_list, safe=False )

