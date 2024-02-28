import os
import uuid
import boto3
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Image(models.Model):    
    url = models.URLField()
    # likes = models.IntegerField(default=0)
    # comments = models.TextField(max_length=400)
    keywords = models.CharField(max_length=100)    
    category = models.CharField(max_length=100)


    def __str__(self):
        return self.url


# class Likes(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     image = models.ForeignKey(Image, on_delete=models.CASCADE, related_name ='likes')
#     likes = models.IntegerField(default=0)

#     def __str__(self):
#         return f'{self.user}likes {self.image}'   


class Comments(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ForeignKey(Image, on_delete=models.CASCADE, related_name='comments')
    comments = models.TextField(max_length=400)  

    def __str__(self):
        return f'{self.user} comments on {self.image}'  


class Category(models.Model):
    image = models.ForeignKey(Image, on_delete=models.CASCADE, related_name='categories')
    category = models.CharField(max_length= 100)

    def __str__(self):
        return f'{self.image} is in category {self.category}'



