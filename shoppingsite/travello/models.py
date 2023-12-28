from django.db import models

# Create your models here.
class destination(models.Model):
    
    name =  models.CharField(max_length=100)
    img = models.ImageField(upload_to='pics')
    des = models.TextField(max_length=300)
    price = models.IntegerField()
    offer = models.BooleanField(default=False)