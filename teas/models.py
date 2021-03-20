from django.db import models
from django.contrib.auth.models import User

class Tea(models.Model):
    name = models.CharField(max_length=100)
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
