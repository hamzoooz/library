from django.http import JsonResponse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect , get_object_or_404
from .forms import BookForm
from django.utils.text import slugify
from .models import Books
from users.models import Profile


from django.http import JsonResponse
from django.db.models import Count , Sum , Avg
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from books.models import Books, Category
from tools.models import Whatsapp
from follow.models import FollowSystem
from users.models import Profile 
from rating.models import RatingSystem, RatingSystemUser
from django.db.models import Q
from comments.models import Comments
from quotes.models import  Qoutes
from users.models import Profile
from tools.models import CaruselImage

import PyPDF2
import io
import os 
import langid
from PIL import Image

def error_404_view(request, exception):
    return render(request, 'core/404.html')

def get_total_range(request):    
    total_rating_user = len(RatingSystemUser.objects.all())
    return render(request, '/home/hamzoooz/bookhope/book_hope.com/templates/base.html')

def frontpage(request ):
    carousel_images = CaruselImage.objects.all()[0:5]
    # return render(request, 'inc/slider.html' , {"carousel_images":carousel_images})


    trending_books = Books.objects.filter( available='publised', trending=True)[0:10]
    recent_books = Books.objects.filter( available='publised').order_by('-create_at')[0:10]
    random_books = Books.objects.filter(available='publised').order_by('?')[0:10]
    # print(random_books)
    
    # user_id = request.user
    user_id = request.user.id
    follower = FollowSystem.objects.filter(user=user_id)
    
    ids = []
    id_user = []
    for i in follower:
        ids.append(i.follower)
        id_user.append(User.objects.get(username=i.follower))
    feed_page = Books.objects.filter(user__in=ids)
    
    if request.user.is_authenticated:
        users = Profile.objects.exclude(user__in=id_user).exclude(user=request.user)
    else:
        users = Profile.objects.exclude(user__in=id_user)
    
    return render(request, 'core/frontpage.html', {
        'trending_books': trending_books, 
        'recent_books': recent_books, 
        'feed_page': feed_page, 
        'random_books': random_books, 
        # 'whatsapp': whatsapp, 
        'users': users,
        # "rating": rating,
        "carousel_images": carousel_images,

        })


def book_detail(request, slug):
    # books = Books.objects.get(slug=slug).annotate(avg_rating=Avg('rating'))
    books = Books.objects.get(slug=slug)

    # ################################
    # number of page 
    link = books.file.path
    
    # ################################
    #  get extenion of file 
    file_extension = os.path.splitext(link)[1]
    books.type_of_book = file_extension
    
    # ################################
    #  get size of file 
    print(os.path.getsize(link))
    if not ( os.path.getsize(link)) :
        file_size = os.path.getsize(link)
        books.size = file_size

    # with open(link, 'rb') as file:
    #     # Create a PDF reader object
        
    #     reader = PyPDF2.PdfReader(file)
    #     # Get the total number of pages in the PDF
    #     num_pages = len(reader.pages)
        
    #     title = reader.metadata.title
    #     # creation_date = reader.metadata.creation_date
    #     # meta_keyword = reader.metadata.Keywords
        
    #     # get the first image 
    #     page = reader.pages[0] 


    #     # Extract the text from the PDF
    #     text = ''
    #     # for page in reader.pages:
    #     #     text += page.extract_text()
    #     page = reader.pages[1]
    #     text += page.extract_text()

    #     # Detect the language of the extracted text
    #     language = langid.classify(text)[0]
    #     print(language)
        
    #     # image = page._extract_xobjects().popitem()[1]
    #     # image_data = image.__data
    #     # image_stram  = io.BytestIO(image_data)
    #     # pil_image = Image.open(image_stram)
    # if (title):
    #     books.name = title
    # # books.create_at = creation_date # ger error need to convert to stander format 
    # books.number_pages  = num_pages
    # # ################################
    
    # number of views 
    books.number_of_views += 1

    avg = RatingSystem.objects.filter(book=books).annotate(avg_rating=Avg('rating'))

    books.save()

    categorys = Books.objects.filter(slug=slug )
    comments = Comments.objects.filter(book=books).order_by('-create_at')[0:5]
    qoutes = Qoutes.objects.filter(book=books)
    
    
    if request.user.is_authenticated:
        if (RatingSystem.objects.filter(user=request.user, book=books)):
            rating_book = RatingSystem.objects.filter(user=request.user, book=books).first()
        else:
            rating_book = RatingSystem.objects.filter()
    else:
        rating_book = RatingSystem.objects.filter(book=books)


    same_category = Books.objects.filter(category=books.category.id, available="publised" ).exclude(name=books.name)
    similar_topic = Books.objects.filter( name__icontains=books.name, available="publised").exclude(name=books.name)
    random_book = Books.objects.filter(available="publised").exclude(name=books.name).order_by("?")[0:10 ]
    
    # query = books.name.split()
    query = books.name
    similar_books = Books.objects.exclude(slug=slug).filter( Q(name__icontains=query) | Q(meta_description__icontains=query) | Q(meta_tilte__icontains=query) | Q(meta_keyword__icontains=query) | Q(meta_description__icontains=query) | Q(tags__icontains=query) | Q(available='publised') )[0:20]

    return render(request, 'core/book_detail.html', {
        'books': books, 
        'category': category, 
        'comments': comments, 
        'qoutes': qoutes, 
        # "html": html, 
        "rating_book": rating_book,
        # "avg_rating": avg_rating,
        "similar_books": similar_books,
        "similar_topic": similar_topic,
        "same_category": same_category,
        "random_book": random_book,
        })

# Category 
def category_detail(request, slug):
    categoreis = get_object_or_404(Category, slug=slug)
    books = Books.objects.filter(category=categoreis.id, available='publised')
    return render(request, 'core/category_detail.html', {'categoreis': categoreis, 'books': books, })

def category(request):
    categoreis = Category.objects.all()
    return render(request, 'core/category.html', {'categoreis': categoreis})

# Pages 
def trending_page(request):
    trending_books = Books.objects.filter(trending=True, available='publised')
    return render(request, 'core/pages/trending_page.html', {'trending_books': trending_books})
def recent_page(request):
    recent_books = Books.objects.filter( available='publised').order_by('-create_at')
    return render(request, 'core/pages/recent_page.html', {'recent_books': recent_books})

@login_required()
def feed_page(request):
    user_id = request.user.id
    follower = FollowSystem.objects.filter(user=user_id)
    ids = []
    for i in follower:
        ids.append(i.follower)
    feed_page = Books.objects.filter(user__in=ids)

    users = Profile.objects.all().exclude(user=user_id)
    
    return render(request, 'core/pages/feed_page.html', {'feed_page': feed_page, 'users': users})


def random_books(request):
    random_books = Books.objects.filter(available='publised').order_by('?')
    return render(request, 'core/pages/random_books.html', {'random_books': random_books})


# PUK for Zain M. hassan  30436082


def test_template(request):
    return render(request, 'tem.html')




@login_required
def add_book(request):
    if request.method == 'POST':
        # title = request.POST['name']
        # file = request.FILES.get('file')
        # sample = request.FILES.get('sample')
        # category = request.POST['category']
        # book_image = request.FILES.get('book_image')
        # number_pages = request.POST['number_pages']
        # language = request.POST['language']
        # short_link = request.POST['short_link']
        # isnn = request.POST['isnn']
        # edition = request.POST['edition']
        # published_house = request.POST['published_house']
        # small_descrption = request.POST['small_descrption']
        # descrption = request.POST['descrption']
        # original_price = request.POST['original_price']
        # selling_price = request.POST['selling_price']
        # # type_of_book = request.POST['type_of_book']
        # size = request.POST['size']
        # tags = request.POST['tags']
        # meta_tilte = request.POST['meta_tilte']
        # meta_keyword = request.POST['meta_keyword']
        # meta_description = request.POST['meta_description']
        
        form  = BookForm(request.POST , request.FILES )
        if form.is_valid():
            title = request.POST.get('name')
            book = form.save(commit=False)
            book.slug = slugify(title)
            get_user = request.user
            profile = Profile.objects.get(user=get_user)
            book.user = profile
            book.save()
            messages.info(request, 'Your Book Added sucessfuly waiting publish... ')
            return redirect('my_store')
    else:
        form = BookForm()
        # messages.info(request, 'There Are wrang in your data ...! ')
    return render(request, 'books/add_book.html', {
        'form': form,
        'title': 'Add Book',
        'button': 'Add Book',
    })

@login_required
def edit_book(request, pk):
    book_detial = Books.objects.get(pk=pk)
    # book_detial = get_object_or_404(Books, pk)
    if request.method == 'POST':
        book =  Books.objects.get(pk=pk)
        # book = get_object_or_404(Books, pk)
        if (request.user == book.user) or request.user.is_staff:
            form = BookForm(request.POST, request.FILES, instance=book )
            if form.is_valid():
                form.save()
                messages.info(request, 'Your Changes has been added sucssessfuly... ')
                if request.META.get('HTTP_REFERER'):
                # print(f'request.resolver_match.url_name {request.resolver_match.url_name}')  # edit_book
                # print(f'request.META.get("HTTP_REFERER") {request.META.get("HTTP_REFERER")}') #  http://127.0.0.1:8000/my_library/edit_book/3/
                    return redirect(request.META.get("HTTP_REFERER"))
                else:
                    return redirect('my_store')
        else:        
            messages.info(request, "You hav'nt access to Edit This Book but you edit send to auther as seagest ! ")
            return redirect('my_store')
    else:
        # book = get_object_or_404(Books, pk)
        book = Books.objects.get(pk=pk)
        form = BookForm(instance=book)
        return render(request, 'books/edit_book.html', { 
                'title':'edit Book', 
                'form':form,  
                'book': book,
                'book_detial':book_detial
                })

 # Login 

@login_required
def delet_book(request, pk):
    profile = Profile.objects.get(books=pk)
    

    if (request.user.is_staff):
        book = Books.objects.get(pk=pk)
        book.available = 'draft'
        book.save()
        return JsonResponse({"status":f'The Book - { book.name } -  Was Moved to Trash sucssessfuly '})
        # messages.info(request,  f'The Book - { book.name } -  Was Moved to Trash sucssessfuly ' )
    elif (str(profile) == str(request.user)):
        book = Books.objects.get(pk=pk)
        book.available = 'draft'
        book.save()
        # messages.info(request,  f'The Book - { book.name } - Was Moved to Trash sucssessfuly' )
        return JsonResponse({"status":f'The Book - { book.name } -  Was Moved to Trash sucssessfuly '})
    else:
        return JsonResponse({"status": 'You not have access to delete this book '})
        
        # messages.info(request,  'You not have access to delete this book ')
    if request.META.get('HTTP_REFERER'):
        return redirect(request.META.get("HTTP_REFERER"))
    else:
        return redirect('my_store')


def incres_number_of_download(request , pk):
    book_id = request.POST['book_id_download']
    get_book = Books.objects.get(pk=book_id)
    get_book.number_of_download  += 1 
    get_book.save()
    
    return JsonResponse({"status":"download successfully ! "})


