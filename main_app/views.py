# import os
# import uuid
# import boto3
from django.contrib.auth.models import Group, User
from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from rest_framework import permissions, viewsets
from .models import Image, Likes, Comments, Category
from .serializers import *


# def home(request)
    
#     return render(request, 'home.html')

def image_detail(request, image_id):
    image = get_object_or_404(Image, pk=image_id)

    likes = Likes.objects.filter(imagge=image)
    comments = Comments.objects.filter(image=image)
    categories = Category.objects.filter(image=image)

    likes_data = [{'user': like.user.name, 'likes' : like.likes} for like in likes]
    comments_data = [{'user' : comment.user.name, 'comment' : comment.comments} for comment in comments]
    categories_data = [{'category' : category.category} for category in categories]

    image_data = {
        'id': image.id,
        'url': image.url,
        'likes': likes_data,
        'commnets': comments_data,
        'categories': categories_data,
    }

    return JsonResponse(image_data)

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]
    

class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]

class ImageViewSet(viewsets.ModelViewSet):
    queryset = Image.objects.all()
    serializer_class = ImagesSerializer
    permission_classes = [permissions.IsAuthenticated]    

