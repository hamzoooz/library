from django import forms
# from ckeditor.fields import RichTextField
from .models import  Books
from django.forms import BaseForm, BaseModelForm


class BookForm(forms.ModelForm):
    
   #  name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control my-2', 'placeholder': 'Enter Name of Book '}))
   #  file = forms.CharField(widget=forms.FileInput( attrs={'class': ' form-control my-2 class-file '}))
   #  sample = forms.CharField(widget=forms.FileInput( attrs={'class': ' form-control my-2 class-sample '}))
   #  category = forms.CharField(widget=forms.SelectMultiple( attrs={'class': ' form-control my-2 class-category '}))
   #  book_image = forms.CharField(widget=forms.FileInput( attrs={'class': ' form-control my-2 class-book_image '}))
   #  number_pages = forms.CharField(widget=forms.NumberInput(attrs={'class':' form-control my-2 class-number_pages ' }))
   #  language = forms.CharField(widget=forms.TextInput(attrs={'class':' form-control my-2 class-language ' }))
   #  short_link = forms.URLField(widget=forms.URLInput(attrs={'class': ' form-control my-2 class-short_link '}))
   #  isnn = forms.CharField(widget=forms.TextInput(attrs={'class':' form-control my-2 class-isnn ' }))
   #  edition = forms.CharField(widget=forms.TextInput(attrs={'class':' form-control my-2 class-edition ' }))
   #  published_house = forms.CharField(widget=forms.TextInput(attrs={'class':' form-control my-2 class-published_house ' }))
   #  number_of_views = forms.CharField(widget=forms.TextInput(attrs={'class':' form-control my-2 class-number_of_views ' }))
   #  small_descrption = forms.CharField(widget=forms.TextInput(attrs={'class':' form-control my-2 class-small_descrption ' }))
   #  descrption = forms.CharField(widget=forms.TextInput(attrs={'class':' form-control my-2 class-descrption ' }))
   #  descrption = RichTextField()
   #  quantity = forms.CharField(widget=forms.TextInput(attrs={'class':' form-control my-2 class-quantity ' }))
   #  original_price = forms.CharField(widget=forms.NumberInput(attrs={'class':' form-control my-2 class-original_price ' }))
   #  selling_price = forms.CharField(widget=forms.NumberInput(attrs={'class':' form-control my-2 class-selling_price ' }))
   #  type_of_book = forms.CharField(widget=forms.TextInput(attrs={'class':' form-control my-2 class-type_of_book ' }))
   #  size = forms.CharField(widget=forms.NumberInput(attrs={'class':' form-control my-2 class-size ' }))
   #  tags = forms.CharField(widget=forms.TextInput(attrs={'class':' form-control my-2 class-tags ' }))
   #  meta_tilte = forms.CharField(widget=forms.TextInput(attrs={'class':' form-control my-2 class-meta_tilte ' }))
   #  meta_keyword = forms.CharField(widget=forms.TextInput(attrs={'class':' form-control my-2 class-meta_keyword ' }))
   #  meta_description = forms.CharField(widget=forms.TextInput(attrs={'class':' form-control my-2 class-meta_description ' }))
    
    
    class Meta:
        model = Books
        fields = ('name', 'file', 'sample', 'book_image', 'category',  'language',
                  'type_of_book', 'size',  'number_pages', 'short_link', 'isnn', 'edition', 
                  'published_house', 'descrption', 'quantity', 'original_price', 'selling_price', 
                  'tags', 'meta_tilte', 'meta_keyword', 'meta_description','url' )
        # fields = ( '__all__' , )
        widgets = {
            'name' :  forms.TextInput(attrs={ 'class':'form-control my-2 class-name' }),
            'url' :  forms.TextInput(attrs={ 'class':'form-control my-2 class-url' }),
            'file' :  forms.FileInput(attrs={ 'class':'form-control my-2 class-file' }),
            'sample':  forms.FileInput(attrs={'class': 'form-control my-2 class-sample'}),
            'category' :  forms.Select(attrs={ 'class':'form-control my-2 class-category' }),
            'book_image':  forms.FileInput(attrs={'class': 'form-control my-2 class-book_image'}),
            'number_pages' :  forms.TextInput(attrs={ 'class':'form-control my-2 class-number_pages' }),
            'language' :  forms.Select(attrs={ 'class':'form-control my-2 class-language' }),
            'short_link' :  forms.TextInput(attrs={ 'class':'form-control my-2 class-short_link' }),
            'isnn' :  forms.TextInput(attrs={ 'class':'form-control my-2 class-isnn' }),
            'edition' :  forms.TextInput(attrs={ 'class':'form-control my-2 class-edition' }),
            'published_house' :  forms.TextInput(attrs={ 'class':'form-control my-2 class-published_house' }),
            'descrption' :  forms.Textarea(attrs={ 'class':'form-control my-2 class-descrption' }),
            'quantity' :  forms.TextInput(attrs={ 'class':'form-control my-2 class-quantity' }),
            'original_price' :  forms.TextInput(attrs={ 'class':'form-control my-2 class-original_price' }),
            'selling_price' :  forms.TextInput(attrs={ 'class':'form-control my-2 class-selling_price' }),
            'type_of_book':  forms.TextInput(attrs={'class': 'form-control my-2 class-type_of_book'}),
            'size' :  forms.TextInput(attrs={ 'class':'form-control my-2 class-size' }),
            'tags' :  forms.TextInput(attrs={ 'class':'form-control my-2 class-tags' }),
            'meta_tilte' :  forms.TextInput(attrs={ 'class':'form-control my-2 class-meta_tilte' }),
            'meta_keyword' :  forms.TextInput(attrs={ 'class':'form-control my-2 class-meta_keyword' }),
            'meta_description' :  forms.TextInput(attrs={ 'class':'form-control my-2 class-meta_description' }),
        }


# status, trending, create_at, update_at, available, user, url, published_data, ordered, small_descrption,  number_of_download, rating, abrov