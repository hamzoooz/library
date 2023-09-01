import os 
from django.utils import timezone
from django.db import models
from ckeditor.fields import RichTextField
from users.models import Profile 
# from .models import Books
from datetime import datetime
from django.core.validators import MaxValueValidator, MinValueValidator
# from django.contrib.auth.models import User # get error 
# from rating.models import RatingSystem # get error

import uuid

def get_file_path_cat(request, filename):
    orifinal_filename = filename
    nowtime = datetime.now().strftime('%Y %d %h %M:%S')
    filename = '%s%s' % (nowtime, orifinal_filename)
    return os.path.join('upload/category', filename)

class Category(models.Model):
    create_by = models.ForeignKey(Profile, on_delete=models.CASCADE,default='uncategoraize')
    # books = models.ForeignKey(Books, on_delete=models.CASCADE)
    name = models.CharField(max_length=150, null=False, blank=False)
    slug = models.SlugField(unique=True, max_length=150, null=False, blank=False)
    image = models.ImageField(upload_to=get_file_path_cat,null=True, blank=True,   default='defualt-pic-avater.jpg')
    descrption = models.TextField(max_length=500,  blank=True, null=True)
    status = models.BooleanField(default=False, help_text='0=default, 1 = hidden')
    trending = models.BooleanField( default=False, help_text='0=default, 1 = Trending')
    meta_tilte = models.CharField(max_length=150,  blank=True, null=True)
    meta_keyword = models.CharField(max_length=150,  blank=True, null=True)
    meta_description = models.CharField(max_length=150,  blank=True, null=True)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{ self.id} -  { self.name}'

def get_file_path_books(request, filename):
    orifinal_filename = filename
    name = 'bookhope.com'
    nowtime = datetime.now().strftime('%Y %d %h %M:%S')
    filename = '%s %s.png' % (orifinal_filename, name)
    return os.path.join('upload/books/covers', filename)

def get_file_path_books_thumbnail(request, filename):
    orifinal_filename = filename
    name = 'bookhope.com'
    nowtime = datetime.now().strftime('%Y %d %h %M:%S')
    filename = '%s %s.png' % (orifinal_filename, name)
    return os.path.join('upload/books/thumbnail', filename)

languages = (
    ('ar', 'Arabic'),
    ('en', 'English'),
    ('oth', 'Others'),
)

available = (
    ('publised', 'publised'),
    ('wiating', 'wiating'),
    ('draft', 'draft'),
    ('deleted', 'deleted'),
    )
types = (
    ('pdf', 'pdf'),
    ('docs', 'docs'),
    ('ebok', 'ebok'),
)

   
class Uplaod_Free(models.Model):
    uuid = models.CharField(max_length=200, default=uuid.uuid1())
    user = models.ForeignKey(Profile, on_delete=models.CASCADE)
    title = models.CharField(max_length=150 , )
    the_auther = models.CharField(max_length=100, null=True, blank=True)
    url = models.URLField(null=True, blank=True)
    url2 = models.URLField(null=True, blank=True)
    file = models.FileField(upload_to='upload/free_book', null=True, blank=True)
    sample = models.FileField(upload_to='upload/free_sample', null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, blank=True, default=1)    
    book_image = models.ImageField(upload_to=get_file_path_books, null=True, blank=True)
    published_data = models.DateField(auto_now_add=True)
    number_pages = models.IntegerField(blank=True, null=True)
    language = models.CharField(max_length=3, choices=languages, default='ar')
    isnn = models.IntegerField(blank=True, null=True)
    edition = models.IntegerField(blank=True, null=True)
    published_house = models.CharField(max_length=50, blank=True, null=True)
    small_descrption = models.TextField(max_length=1000, blank=True, null=True)
    descrption = RichTextField(blank=True, null=True)
    type_of_book = models.CharField(max_length=10, default='pdf')
    size = models.PositiveIntegerField(blank=True, null=True)
    tags = models.CharField(max_length=150, blank=True, null=True)
    meta_tilte = models.CharField(max_length=150, blank=True, null=True)
    meta_keyword = models.CharField(max_length=150, blank=True, null=True)
    meta_description = models.CharField(max_length=150, blank=True, null=True)
    
    def __str__(self):
        return f"{self.title} by {self.user.username}"

class Pay_Books(models.Model):
    uuid = models.CharField(max_length=200, default=uuid.uuid1())
    user = models.ForeignKey(Profile, on_delete=models.CASCADE, default=1)
    title = models.CharField(max_length=150, null=True, blank=True)
    the_auther = models.CharField(max_length=100, null=True, blank=True)
    url = models.URLField(null=True, blank=True)
    url1 = models.URLField(null=True, blank=True)
    file = models.FileField(  upload_to="upload/pay_books", null=True, blank=True)
    sample = models.FileField(   upload_to="upload/pay_books",  null=True, blank=True)
    category = models.ForeignKey( Category, on_delete=models.CASCADE , null=True, blank=True, default=1)
    slug = models.SlugField(unique=True, max_length=150, null=True, blank=True )
    book_image = models.ImageField(upload_to=get_file_path_books, null=True, blank=True)
    thumbnail = models.ImageField( upload_to=get_file_path_books_thumbnail, null=True, blank=True)
    published_data = models.DateField(auto_now_add=True)
    number_pages = models.IntegerField(blank=True, null=True)
    language = models.CharField(max_length=10, default='english' , blank=True, null=True)
    # short_link = models.URLField(blank=True, null=True)
    isnn = models.IntegerField(blank=True, null=True)
    # ordered = models.IntegerField(blank=True, null=True) #  null 
    edition = models.IntegerField(blank=True, null=True)
    published_house = models.CharField(max_length=50, blank=True, null=True)
    # available = models.CharField(max_length=10, choices=available, default='wiating')
    # number_of_views = models.IntegerField(default=0)
    small_descrption = models.TextField(max_length=1000, blank=True, null=True)
    descrption = RichTextField(blank=True, null=True)
    quantity = models.PositiveIntegerField(blank=True, null=True , default=1)
    number_of_download = models.IntegerField(default=0)
    original_price = models.FloatField(default=0, null=True, blank=True)
    selling_price = models.FloatField(default=0, null=True, blank=True)
    # type_of_book = models.CharField(max_length=10, choices=types, default='pdf')
    type_of_book = models.CharField(max_length=10, default='pdf')
    size = models.PositiveIntegerField(blank=True, null=True)
    status = models.BooleanField(default=False, help_text='0=default, 1 = hidden')
    # trending = models.BooleanField(default=False, help_text='0=default, 1 = Trending')
    # rating = models.IntegerField(default=0 , validators=[MinValueValidator(1) ,MinValueValidator(5) ])
    # rating = models.ForeignKey(RatingSystem, on_delete=models.CASCADE)
    tags = models.CharField(max_length=150, blank=True, null=True)
    meta_tilte = models.CharField(max_length=150, blank=True, null=True)
    meta_keyword = models.CharField(max_length=150, blank=True, null=True)
    meta_description = models.CharField(max_length=150, blank=True, null=True)
    
    def __str__(self):
        return f'{self.title} by {slef.user.username}'

class Books(models.Model):
    # uuid = models.CharField(max_length=200, default=uuid.uuid1())
    user = models.ForeignKey(Profile, on_delete=models.CASCADE, default=1)
    name = models.CharField(max_length=150, null=True, blank=True)
    # the_auther = models.CharField(max_length=100, null=True, blank=True)
    url = models.URLField(null=True, blank=True)
    file = models.FileField(null=True, blank=True)
    sample = models.FileField( null=True, blank=True)
    category = models.ForeignKey( Category, on_delete=models.CASCADE , null=True, blank=True, default=1)
    slug = models.SlugField(unique=True, max_length=150, null=True, blank=True )
    book_image = models.ImageField(upload_to=get_file_path_books, null=True, blank=True)
    thumbnail = models.ImageField( upload_to=get_file_path_books_thumbnail, null=True, blank=True)
    published_data = models.DateField(auto_now_add=True)
    number_pages = models.IntegerField(blank=True, null=True)
    language = models.CharField(max_length=3, choices=languages, default='ar')
    short_link = models.URLField(blank=True, null=True)
    isnn = models.IntegerField(blank=True, null=True)
    ordered = models.IntegerField(blank=True, null=True) #  null 
    edition = models.IntegerField(blank=True, null=True)
    published_house = models.CharField(max_length=50, blank=True, null=True)
    available = models.CharField(max_length=10, choices=available, default='wiating')
    number_of_views = models.IntegerField(default=0)
    small_descrption = models.TextField(max_length=1000, blank=True, null=True)
    descrption = RichTextField(blank=True, null=True)
    quantity = models.PositiveIntegerField(blank=True, null=True , default=1)
    number_of_download = models.IntegerField(default=0)
    original_price = models.FloatField(default=0, null=True, blank=True)
    selling_price = models.FloatField(default=0, null=True, blank=True)
    # type_of_book = models.CharField(max_length=10, choices=types, default='pdf')
    type_of_book = models.CharField(max_length=10, default='pdf')
    size = models.PositiveIntegerField(blank=True, null=True)
    status = models.BooleanField(default=False, help_text='0=default, 1 = hidden')
    trending = models.BooleanField(default=False, help_text='0=default, 1 = Trending')
    rating = models.IntegerField(default=0 , validators=[MinValueValidator(1) ,MinValueValidator(5) ])
    # rating = models.ForeignKey(RatingSystem, on_delete=models.CASCADE)
    tags = models.CharField(max_length=150, blank=True, null=True)
    meta_tilte = models.CharField(max_length=150, blank=True, null=True)
    meta_keyword = models.CharField(max_length=150, blank=True, null=True)
    meta_description = models.CharField(max_length=150, blank=True, null=True)
    create_at = models.DateTimeField(auto_now_add=True)
    # creation_date = models.DateTimeField(default=timezone.now)
    update_at = models.DateTimeField(auto_now=True)
    abrov = models.BooleanField(default=False)

    def get_metadata(self):
        link = self.file.path
        print(self.file.path)
        return link
    
    class Meta:
        managed = True
        verbose_name = 'Book'
        verbose_name_plural = 'Books'
        # ordering = ('-create_at',)
        # unique_together = (('user', 'meal'),)
        # index_together = (('user', 'meal'),)
        

    def extract_data_from_pdf(self):
        link = self.file.path

        # ################################
        #  get extenion of file
        file_extension = os.path.splitext(link)[1]
        self.type_of_book = file_extension

        # ################################
        #  get size of file
        file_size = os.path.getsize(link)
        self.size = file_size
        
        with open(link, 'rb') as file:
            reader = PyPDF2.PdfReader(file)
            # Get the total number of pages in the PDF
            num_pages = len(reader.pages)

            title = reader.metadata.title
            # creation_date = reader.metadata.creation_date
            # meta_keyword = reader.metadata.Keywords

            # get the first image
            page = reader.pages[0]

            # Extract the text from the PDF
            text = ''
            # for page in reader.pages:
            #     text += page.extract_text()
            page = reader.pages[1]
            text += page.extract_text()

            # Detect the language of the extracted text
            language = langid.classify(text)[0]
            # print(language)

            # image = page._extract_xobjects().popitem()[1]
            # image_data = image.__data
            # image_stram  = io.BytestIO(image_data)
            # pil_image = Image.open(image_stram)

            # Get the total number of pages in the PDF
            self.number_pages = len(reader.pages)

            title = reader.metadata.title
            # self.creation_date = reader.metadata.creation_date
            # meta_keyword = reader.metadata.Keywords

            # Detect the language of the extracted text
            self.language = langid.classify(text)[0]
            
            if  not (self.name):
                self.name = title
            # books.create_at = creation_date # ger error need to convert to stander format
            books.number_pages = num_pages
        # ################################

            # Create a PDF reader object
            # Save the model instance
            self.save()


    def __str__(self):
        return self.name

    def get_display_price(self):
        # return self.selling_price / 100  # to convert from cet to doller
        return self.selling_price 
    
    def get_display_thumbnamil(self):
        if self.thumbnail:
            return self.thumbnail.url
        else:
            if self.book_image:
                self.thumbnail = self.make_thumbnail(self.book_image)
                self.save()
                return self.thumbnail.url 
            else:
                return 'https://via.placeholder.com/240x240.jpg'
        
    def make_thumbnail(self, book_image, size = (300, 300) ):
        img = Image.open(image)
        img.convert('RGB')
        img.thumbnail(size)
        
        thumb_io = BytestID()
        img.save(thumb_io , 'JPEG', quality=85)
        name = image.name.replace('upload/books/thumbnail', '')
        
        thumbnail = File(thumb_io , name=name)
        return thumbnail
   
