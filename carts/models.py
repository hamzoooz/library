from django.db import models
from django.contrib.auth.models import User
from books.models import Books
import uuid

class Cart(models.Model):
    user = models.ForeignKey(User,  blank=True, null=True, on_delete=models.CASCADE)
    book = models.ForeignKey(Books,  on_delete=models.CASCADE)
    create_at = models.DateTimeField(auto_now_add=True)
    qunatity = models.IntegerField(default=1)

    def __str__(self):
        
        return f"{self.user.username} - {self.book.name } - {self.qunatity } "
class Order(models.Model):

    order_status = (
        ('pending', 'pending'),
        ('out for Shipping', 'out for Shipping'),
        ('Completed', 'Completed'), )
    
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    fname = models.CharField(max_length=150, null=False)
    lname = models.CharField(max_length=150, null=False)
    email = models.EmailField(max_length=150, null=False)
    phone = models.CharField(max_length=150, null=False)
    address = models.TextField()
    city = models.CharField(max_length=150, null=False)
    conutry = models.CharField(max_length=150, null=False)
    pincode = models.CharField(max_length=150, null=False)
    total_price = models.FloatField(null=False)
    payment_mode = models.CharField(max_length=150, null=False)
    payment_id = models.CharField( max_length=150, null=False, default=uuid.uuid4)
    satuts = models.CharField( max_length=150, choices=order_status, default='pending')
    message = models.TextField(blank=True,null=True)
    tracking_no = models.CharField(max_length=150, null=False)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"order for {self.id} , has email {self.email}   with {self.tracking_no}"
    
    class Meta:
        ordering = ('-create_at', )


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    book = models.ForeignKey(Books, on_delete=models.CASCADE)
    price = models.FloatField(null=False)
    quantity = models.IntegerField(null=False, default=1)

    def __str__(self):
        return f"order for {self.order.id} , has email {self.order.email}   with {self.order.tracking_no}"