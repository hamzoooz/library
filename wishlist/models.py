from django.contrib.auth.models import User
from django.db import models
from books.models import Books




class WishList(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Books, on_delete=models.CASCADE)
    create_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f'{ self.user } - { self.book }'

