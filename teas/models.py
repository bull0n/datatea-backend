from django.db import models
from django.contrib.auth.models import User

class Tea(models.Model):
    class Category(models.TextChoices):
        WHITE = 'white', 'White'
        GREEN = 'green', 'Green'
        YELLOW = 'yellow', 'Yellow'
        OOLONG = 'oolong', 'Oolong'
        BLACK = 'black', 'Black'
        FERMENTED = 'fermented', 'Fermented'

    name = models.CharField(max_length=100)
    category = models.CharField(max_length=20, choices=Category.choices)
    user = models.ForeignKey(User, on_delete=models.CASCADE) 
    would_buy_again = models.BooleanField(null=True, blank=True)
    price = models.FloatField(null=True, blank=True)
    picking_season = models.DateField(null=True, blank=True)
    origin = models.CharField(max_length=100, blank=True)
    vendor = models.CharField(max_length=50, blank=True)
    url_bought = models.CharField(max_length=200, blank=True)
    vendor_description = models.TextField(blank=True)
    comment = models.TextField()

    def __str__(self):
        return self.name
