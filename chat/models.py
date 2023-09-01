from django.db import models
from django.contrib.auth.models import User
from users.models import Profile
import uuid

class RoomChat(models.Model):
    
    # name = models.CharField(max_length=150, default=uuid.uuid1())
    name = models.CharField(max_length=150)
    sender = models.ForeignKey(User, on_delete=models.CASCADE)
    recever = models.ForeignKey(Profile, on_delete=models.CASCADE)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.name} send {self.sender} to {self.recever}'
        # return f'{self.name} '
        

class Message(models.Model):
    sender = models.ForeignKey(User, on_delete=models.CASCADE)
    recever = models.ForeignKey(Profile, on_delete=models.CASCADE)
    room = models.ForeignKey(RoomChat, on_delete=models.CASCADE)
    topic = models.CharField(max_length=100 , null=True, blank=True)
    message = models.TextField(max_length=500, null=False, blank=False)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=False)

    def get_sender(self):
        return Profile.objects.get(user=self.sender)

    
    def __str__(self):
        return f'{self.sender} send {self.message} to {self.recever}'
