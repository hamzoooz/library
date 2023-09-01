from django.contrib.auth.models import User
from django.db import models
from users.models import Profile

class FollowSystem(models.Model):
    # user = models.CharField(max_length=50)
    # follower = models.CharField(max_length=50)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    follower = models.ForeignKey(Profile, on_delete=models.CASCADE)
    create_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'user : {self.user.username} followed {self.follower.user} follower '
    
    
