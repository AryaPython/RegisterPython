from django.db import models

# Create your models here.
class Destination(models.Model):
    name=models.CharField(max_length=250)
    img=models.ImageField(upload_to='pics')
    desc=models.TextField()

    def __str__(self):
        return self.name

class Persons(models.Model):
    name=models.CharField(max_length=350)
    img=models.ImageField(upload_to='person')
    desc=models.TextField()

