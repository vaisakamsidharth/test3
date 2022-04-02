from django.db import models
from django.contrib.auth.models import User
from owner.models import Books

# Create your models here.


class Carts(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    item = models.ForeignKey(Books, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)
    options = (
        ('in_cart', 'in_cart'),
        ('cancelled', 'cancelled'),
        ('order_placed', 'order_placed')
    )
    status = models.CharField(max_length=120, choices=options, default='in_cart')


class Orders(models.Model):
    item = models.ForeignKey(Books, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)
    address = models.CharField(max_length=250)
    options = (
        ("order_placed", "order_placed"),
        ("dispatched", "dispatched"),
        ("cancelled", "cancelled"),
        ("delivered", "delivered")
    )
    status = models.CharField(max_length=50, choices=options, default="order_placed")
    expected_delivery_date = models.DateField(null=True)


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="customer")
    phone_no = models.CharField(max_length=12)
    address = models.TextField()
    profile_pic = models.ImageField(upload_to="images")



