from django.db import models

# Create your models here.

# User model
class User(models.Model):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    app_label = 'app'

# Stock Data model
class StockData(models.Model):
    ticker = models.CharField(max_length=10)
    shares = models.IntegerField()
    purchase_price = models.DecimalField(max_digits=10, decimal_places=2)
    purchase_date = models.DateField()