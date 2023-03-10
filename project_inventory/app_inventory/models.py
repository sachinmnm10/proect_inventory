from django.db import models
from datetime import datetime

# Create your models here.
class AppUser(models.Model):    # inheritance a model called Model from models
    full_name = models.CharField(max_length = 200)
    email = models.EmailField(unique=True)
    contact = models.CharField(max_length=100)
    password = models.CharField(max_length=100)

    def __str__(self):
        return self.full_name

    class Meta:     # metadata of our class data
        db_table = "app_users"

class Item(models.Model):
    title = models.CharField(max_length=100)
    particular = models.CharField(max_length=200)
    lf = models.CharField(max_length=100, null=True, blank=True)
    quantity = models.IntegerField(max_length=20)
    price = models.FloatField(max_length=200)
    total = models.FloatField(max_length=200)
    added_at = models.DateTimeField(default=datetime.now())
    user = models.ForeignKey(AppUser, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    class Meta:
        db_table = "app_items"