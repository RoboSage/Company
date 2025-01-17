from django.db import models

# Create your models here.

#creating Company Model
class Company(models.Model):
    id = models.AutoField(primary_key = True)
    name = models.CharField(max_length = 50)
    location = models.CharField(max_length = 50)
    about = models.TextField()
    type = models.CharField(
        max_length = 100, 
        choices = (
            ('product_base','Product Based'),
            ('service_based','Service based')
            )
        )
    added_date = models.DateField(auto_now = True)
    active = models.BooleanField(default = True)