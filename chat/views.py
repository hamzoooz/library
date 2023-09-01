from django.shortcuts import render , redirect
from django.db.models import Q
from django.contrib.auth.models import User
from django.http import JsonResponse , HttpResponse
# from django.contrib import messages as ms # get empty messages as noice
from chat.models import Message , RoomChat
from users.models import Profile

from django.core.serializers import serialize

def all_messages(request ):
    user = request.user
    profile = User.objects.get(username=user)
    user_recever = Profile.objects.get(user=profile)
    # all_messages = Message.objects.filter(Q(recever=user_recever) | Q(sender=profile))
    all_rooms = RoomChat.objects.filter( Q(recever=user_recever) | Q(sender=profile))

    sender = request.user  # This for new site if no chat r or users 
    for i in all_rooms:
        sender = i.sender
        recever  = i.recever

    
    return render(request, 'messages/home.html', {
        # "all_messages":all_messages,
        "all_rooms":all_rooms,
        "sender ": sender,
        })

def view_messages(request, pk ):
    room = RoomChat.objects.filter(name=pk).first()
    user = request.user.id
    messages_view = Message.objects.filter(room__name=room.name)

    return render(request, 'messages/view_message.html', {
        "messages_view": messages_view,
        "room": room,
        })

def send_message(request, recever):
    recever_id  = request.POST['recever']
    message_text  = request.POST['message_text']
    message_topic  = request.POST['message_topic']
    user_recever = User.objects.get(username=recever)
    user_sender = User.objects.get(username=request.user)
    recever = Profile.objects.get(user=user_recever)
    
    if (RoomChat.objects.filter(Q(recever=recever) | Q(sender=user_sender))):
        room  = RoomChat.objects.filter(Q(recever=recever) | Q(sender=user_sender)).first()

    else:
        room  = RoomChat.objects.create(recever=recever , sender=user_sender )

    if request.user.is_authenticated:
        if (message_text != '' ):
            new_message = Message.objects.create(sender=user_sender, recever=recever, topic=message_topic, message=message_text , room=room)
        else:
            return JsonResponse({"status":"Can't be Empty "})        
    else:
        return JsonResponse({"status":"Login To Continu ! "})

    return HttpResponse('send')

def get_message(request, recever):
    user = User.objects.get(username=recever)
    recever = Profile.objects.get(user=user)
    
    if request.user.is_authenticated:
        # messages = Message.objects.filter(sender=request.user, recever=recever)
        messages = Message.objects.filter(Q(recever=recever) | Q(sender=request.user) )
        print(messages)
        return JsonResponse({'messages': list(messages.values())})
    else:
        return JsonResponse({'status': "Login to Continu "})
    return redirect('login')


def get_number_of_messages(request):
    number_of_messages = len(Message.objects.filter(recever=request.user.id))
    # print(number_of_messages)
    return render(request, '/home/hamzoooz/bookhope/book_hope.com/templates/inc/nav.html', {'number_of_messages': number_of_messages})
