from django.db import models
from django.contrib.auth.models import User
from users.models import Profile
import os 
from datetime import datetime 


class CaruselImage(models.Model):
    title = models.CharField(max_length=50, null=True, blank=True)
    caption = models.CharField(max_length=255, null=True, blank=True)
    image = models.FileField(upload_to='upload/carusel',null=True, blank=True, default='whatsapp-icon.png')

    def __str__(self):
        return f'{self.title}  {self.caption[0:150]} '


def get_file_path_image(request, filename):
    orifinal_filename = filename
    nowtime = datetime.now().strftime('%Y %d %h %M:%S')
    filename = '%s%s' % (nowtime, orifinal_filename)
    return os.path.join('upload/image', filename)

class Whatsapp(models.Model):
    status = models.BooleanField(default=True)
    number = models.CharField(max_length=50, null=False, blank=False)
    message = models.TextField(max_length=500)
    width = models.CharField(max_length=50, null=False, blank=False)
    heigth = models.CharField(max_length=50, null=False, blank=False)
    icon = models.ImageField(upload_to=get_file_path_image, null=True,blank=True, default='assets/images/whatsapp-icon.png')

    def __str__(self):
        return self.message

class LikePost(models.Model):
    post_id = models.CharField(max_length=500)
    username = models.CharField(max_length=100)

    def __str__(self):
        return self.username
    
