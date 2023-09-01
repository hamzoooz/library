from django.shortcuts import render

# Create your views here.
from tools.models import * 

def get_carusel(request):
    carousel_images = CaruselImage.objects.all()[0:3]
    return render(request, 'inc/slider.html' , {"carousel_images":carousel_images})

