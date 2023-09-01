from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404, redirect
from users.models import Profile
from books.models import Books
from .models import *
from django.contrib import messages


def rating_book(request, slug):
    if request.method == "POST":
        if request.user.is_authenticated:
            book = get_object_or_404(Books, slug=slug)
            rating = request.POST.get('value')
            check_rating = RatingSystem.objects.filter( user=request.user, book=book).exists()
            if (check_rating):
                update_rating = RatingSystem.objects.get(user=request.user, book=book)
                update_rating = RatingSystem.objects.filter( user=request.user,  book=book).update(rating=rating)
            else:
                new_rating = RatingSystem.objects.create(user=request.user, book=book, rating=rating)
            return JsonResponse({'status': 'thank\'s for rating to help other reader to Know Thsi'})
        
        else:
            # return redirect('login')
            return JsonResponse({'status': 'login requer to rate this user '})
    return redirect('/')

# ################################################################################

def rating_user(request, user):
    if request.method == "POST":
        if request.user.is_authenticated:
            profile = get_object_or_404(Profile, user=user)
            rating = request.POST.get('value')
            
            check_rating = RatingSystemUser.objects.filter(user=request.user, profile=profile).exists()

            if (check_rating):
                update_rating = RatingSystemUser.objects.get(user=request.user, profile=profile)
                update_rating = RatingSystemUser.objects.filter( user=request.user,  profile=profile).update(rating=rating)
            else:
                new_rating = RatingSystemUser.objects.create(user=request.user, profile=profile, rating=rating)
            return JsonResponse({'status': 'thank\'s for rating to help other reader to Know Thsi'})
        else:
            # return redirect('login')
            return JsonResponse({'status': 'login requer to rate this book'})
    return redirect('/')
