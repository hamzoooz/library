from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from books.models import Books
from django.contrib.auth.decorators import login_required


# @login_required
def list_books(request):
    books = Books.objects.all()
    books_limt = Books.objects.all()[0:5]
    
    data = {'Results': list(books.values( "pk", "name", "slug" , "status", "trending", "meta_tilte", "meta_keyword", "meta_description", "create_at", "update_at", "available", "user", "url", "category", "published_data", "number_pages", "language", "short_link", "isnn", "ordered", "edition", "published_house", "number_of_views", "small_descrption", "quantity", "number_of_download", "original_price", "selling_price", "type_of_book", "size", "rating", "tags", "abrov"))}
    books_limt = {'Results': list(books_limt.values("pk", "name", "status", "trending", "meta_tilte", "meta_keyword", "meta_description", "create_at", "update_at", "available", "user", "url", "category", "published_data", "number_pages", "language", "short_link", "isnn", "ordered", "edition", "published_house", "number_of_views", "small_descrption", "quantity", "number_of_download", "original_price", "selling_price", "type_of_book", "size", "rating", "tags", "abrov"))}
    
    # if request.user.is_authenticated:
    if request.user.is_staff:
        return JsonResponse(data)
    else:
        # return JsonResponse({"Result":"You'r not authenticated to Access to this Page "})
        return JsonResponse(books_limt)
    

def book_detail_slug(request, slug):
    # books = get_object_or_404(Books, slug=slug)
    books = Books.objects.filter(slug=slug)
    # books_limit = Books.objects.filter(slug=slug)[0:5]
    # categorys = Books.objects.filter(slug=slug)
    # comments = Comments.objects.filter(book=books).order_by('-create_at')[0:5]
    # html = render(request, 'comments/comments.html',{'comments': comments}).content
    # qoutes = Qoutes.objects.filter(book=books)
    # if request.user.is_authenticated:
    #     if (RatingSystem.objects.filter(user=request.user, book=books)):
    #         rating_book = RatingSystem.objects.filter( user=request.user, book=books).first()
    #     else:
    #         rating_book = RatingSystem.objects.filter(book=books).first()
    # else:
    #     rating_book = RatingSystem.objects.filter(book=books)
    # total_rating = len(RatingSystem.objects.filter(book=books))

    data = {"book": list(books.values("pk", "name", "status", "trending", "meta_tilte", "meta_keyword", "meta_description", "create_at", "update_at", "available", "user", "url", "category", "published_data", "number_pages", "language","short_link", "isnn", "ordered", "edition", "published_house", "number_of_views", "small_descrption", "quantity", "number_of_download", "original_price", "selling_price", "type_of_book", "size", "rating", "tags", "abrov"))}
    data_limt = {
        "pk":books_limt.id,
        "name":books_limt.name,
        "small_descrption":books_limt.small_descrption,
        "language":books_limt.language,
        "number_pages":books_limt.number_pages, }
    if request.user.is_authenticated:
        return JsonResponse(data)
    else:
        # return JsonResponse({"Result": "You'r not authenticated to Access to this Page "})
        return JsonResponse(data_limt)

def book_detail_pk(request, pk):
    # books = get_object_or_404(Books, pk=pk)
    books = Books.objects.filter(pk=pk)
    books_limt = Books.objects.get(pk=pk)
    # books = Books.objects.filter(pk=pk)
    # categorys = Books.objects.filter(slug=slug)
    # comments = Comments.objects.filter(book=books).order_by('-create_at')[0:5]
    # html = render(request, 'comments/comments.html',{'comments': comments}).content
    # qoutes = Qoutes.objects.filter(book=books)
    # if request.user.is_authenticated:
    #     if (RatingSystem.objects.filter(user=request.user, book=books)):
    #         rating_book = RatingSystem.objects.filter( user=request.user, book=books).first()
    #     else:
    #         rating_book = RatingSystem.objects.filter(book=books).first()
    # else:
    #     rating_book = RatingSystem.objects.filter(book=books)
    # total_rating = len(RatingSystem.objects.filter(book=books))

    data = {"book": list(books.values("pk", "name", "slug", "status", "trending", "meta_tilte", "meta_keyword", "meta_description", "create_at", "update_at", "available", "user", "url", "category", "published_data", "number_pages", "language","short_link", "isnn", "ordered", "edition", "published_house", "number_of_views", "small_descrption", "quantity", "number_of_download", "original_price", "selling_price", "type_of_book", "size", "rating", "tags", "abrov"))}
    # data_limt = {"book": list(books.values("pk", "name", "slug" ,"status", "trending", "meta_tilte", "meta_keyword", "meta_description", "create_at", "update_at", "available", "user", "url", "category", "published_data", "number_pages", "language","short_link", "isnn", "ordered", "edition", "published_house", "number_of_views", "small_descrption", "quantity", "number_of_download", "original_price", "selling_price", "type_of_book", "size", "rating", "tags", "abrov"))}
    data_limt = {
        "pk":pk,
        "name":books_limt.name,
        "small_descrption":books_limt.small_descrption,
        "language":books_limt.language,
        "number_pages":books_limt.number_pages,
        # "number_pages", "language",
    }
    if request.user.is_authenticated:
        return JsonResponse(data)
    else:
        # return JsonResponse({"Result": "You'r not authenticated to Access to this Page "})
        return JsonResponse(data_limt)

    # return render(request, 'core/book_detail.html', { 'books': books, 'category': category, 'comments': comments, 'qoutes': qoutes, "html": html, "rating_book": rating_book,"total_rating": total_rating,})
#     {