from django.db import models

# Create your models here.

# books = [
#     {"id": 100, "book_name": "Randamoozham", "author": "mt", "price": 400, "copies": 250},
#     {"id": 101, "book_name": "aarachar", "author": "meera", "price": 500, "copies": 250},
#     {"id": 102, "book_name": "the alchemist", "author": "paulo", "price": 780, "copies": 250},
#     {"id": 103, "book_name": "rainrising", "author": "nirupama", "price": 1000, "copies": 250},
#     {"id": 104, "book_name": "indhulekha", "author": "chandhumenon", "price": 580, "copies": 250}
#
# ]


class Books(models.Model):

    objects = None
    book_name = models.CharField(max_length=100, unique=True)
    author = models.CharField(max_length=100)
    price = models.PositiveIntegerField(default=50)
    copies = models.PositiveIntegerField(default=10)
    active_status = models.BooleanField(default=True)
    image = models.ImageField(upload_to="images", null=True, blank=True)

    def __str__(self):
        return self.book_name

# list price less than 300
# book = Books.objects.filter(price__lt=300)

# list books b/w 300 and 500
# book = Books.objects.filter(price__gt=200,price__lt=500)
# book

# get book aadujeevitham
# book = Books.objects.get(id=4)
# book

# print inactive book
# book = Books.objects.filter(active_status=False).values("book_name")

# create a new application location
# create a model districts with district name, population, 1st dose vaccination rate,2nd dose vaccination rate
