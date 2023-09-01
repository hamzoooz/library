from django.db import models
from django.db.models import Count, Sum, Avg
from django.contrib.auth.models import User
from books.models import Books
from users.models import Profile
# Create your models here.


class RatingSystem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Books, on_delete=models.CASCADE)
    rating = models.IntegerField(default=0)
    rate_in = models.CharField(max_length=255, default='book_dateil', null=True, blank=True)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now_add=True)

    # def get_avra_rate(self):
        # return self.number_of_rate.count / 5

    def get_total_rating(self):
        # slef.book.rating = Books.objects.filter(rating=self.book.rating)
        return len(self.book.rating)

    def get_avg(self):
        avg_rating = Avg(self.rating) 
        
        return avg_rating 

    def __str__(self):
        # return f'{self.user.username} rate {self.book.name} by {self.rating} av = {  self.get_total_rating}'
        return f'{self.user.username} rate {self.book.name} by {self.rating}'
        # return f'{self.user.username} rate {self.book.name}  av = {  self.get_total_rating}'
    
class RatingSystemUser(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    rating = models.IntegerField(default=0)
    rate_in = models.CharField(max_length=255, default='book_dateil', null=True, blank=True)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now_add=True)

    def get_avra_rate(self):
        return self.number_of_rate.count / 5

    def __str__(self):
        return f'{self.user.username} rate {self.profile.user} by {self.rating}'

    # def __str__(self):
    #     return f'{self.user.username} rate {self.book}'

    def get_total_rating(self):
        return slef.count
