from django.db import models
from datetime import datetime
# Create your models here.

class Blog(models.Model):
    title=models.CharField(max_length=50)
    #images
    image=models.ImageField(upload_to="images/")
    #videos
    # video=models.FileField(upload_to='media/')
    description=models.TextField()
    author=models.CharField(max_length=50)
    created_at=models.DateTimeField(default=datetime.now)
   
    def __str__(self):
        return self.title

# from django.db import models

# class MyModel(models.Model):
#     fullname = models.CharField(max_length=200)
#     mobile_number = models.IntegerField()
