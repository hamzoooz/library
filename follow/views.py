from django.shortcuts import render , redirect 
from django.http import JsonResponse
from follow.models import FollowSystem
from users.models import Profile
from django.contrib.auth.models import User

def follow(request, username):
    if request.method == 'POST':
        if request.user.is_authenticated:
            user_id = request.POST.get('user') #  === request.user.id
            follower_id = request.POST.get('follower')
            
            user = User.objects.get(pk=user_id)
            follower = Profile.objects.get(user=follower_id)
            if (FollowSystem.objects.filter(follower=follower, user=user)):
                delete_follower = FollowSystem.objects.filter(follower=follower, user=user)
                delete_follower.delete()
                return JsonResponse({'status': "Unfollow Successfuly ! ", 'text': "Follow", 'color': "primary"})
            else:
                new_follower = FollowSystem.objects.create(follower=follower, user=user)
                new_follower.save()
                return JsonResponse({'status': "Your Follow Successfuly  ", 'text': "UnFollow", 'color': "danger"})
        else:
            return JsonResponse({'status': "Login to Continue"})
    return redirect('/')

