from django.db import models
from django.contrib.auth.models import User
from users.models import Profile
from books.models import Books


status = (
    ('publised', 'publised'),
    ('wiating', 'wiating'),
    ('draft', 'draft'),
    ('deleted', 'deleted'),)


class Qoutes(models.Model):
    user = models.ForeignKey(Profile, on_delete=models.CASCADE)
    book = models.ForeignKey(Books, on_delete=models.CASCADE)
    text = models.CharField(max_length=255, null=False, blank=False)
    number_of_like = models.IntegerField(default=0)
    status = models.CharField(max_length=10, choices=status, default='wiating')
    number_of_deslike = models.IntegerField(default=0)
    number_of_view = models.IntegerField(default=0)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.pk} : {self.user.user} take qoute from {self.book.name} = {self.text}'