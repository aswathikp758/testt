from django.db import models

# Create your models here.
class new_user(models.Model):
    username=models.CharField(max_length=200)
    password=models.CharField(max_length=200)
    image=models.ImageField(upload_to='pics')
