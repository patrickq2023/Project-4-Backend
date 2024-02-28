import os
import uuid
import boto3
from django.contrib.auth.models import Group, User
from django.shortcuts import get_object_or_404 
from django.http import JsonResponse
from rest_framework import permissions, viewsets, status
from .models import Image, Comments, Category
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken

from .serializers import *


# def home(request)
    
#     return render(request, 'home.html')

# def image_detail(request, image_id):
#     image = get_object_or_404(Image, pk=image_id)

#     likes = Likes.objects.filter(imagge=image)
#     comments = Comments.objects.filter(image=image)
#     categories = Category.objects.filter(image=image)

#     likes_data = [{'user': like.user.name, 'likes' : like.likes} for like in likes]
#     comments_data = [{'user' : comment.user.name, 'comment' : comment.comments} for comment in comments]
#     categories_data = [{'category' : category.category} for category in categories]

#     image_data = {
#         'id': image.id,
#         'url': image.url,
#         'likes': likes_data,
#         'commnets': comments_data,
#         'categories': categories_data,
#     }

#     return JsonResponse(image_data)

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
    # permission_classes = [permissions.IsAuthenticated]  

    def create(self, request):
        print(request)
        photo_file = request.FILES.get('image', None) 
        if photo_file:
            s3 = boto3.client('s3')
            key = f"{uuid.uuid4().hex[:6]}_{photo_file.name}"
            try:
                bucket = os.environ['S3_BUCKET']
                s3.upload_fileobj(photo_file, bucket, key)
                url = f"{os.environ['S3_BASE_URL']}{bucket}/{key}"
                print('Generated URL:', url)       
                Image.objects.create(url=url, keywords=request.data.get('keywords'),category=request.data.get('category'))
                return Response(status=status.HTTP_205_RESET_CONTENT)
            except Exception as e:
                print('An error occurred uploading file to S3')
                print(e)
            return Response(status=status.HTTP_400_BAD_REQUEST)    
        


        
        
class LogoutView(APIView):
    def post(self, request):
        try:
            refresh_token = request.data["refresh_token"]
            token = RefreshToken(refresh_token)
            token.blacklist()

            return Response(status=status.HTTP_205_RESET_CONTENT)
        except Exception as e:
            return Response(status=status.HTTP_400_BAD_REQUEST)


class SignupView(APIView):
    def post(self, request):
        username = request.data.get('username')
        email = request.data.get('email')
        password = request.data.get('password')
        
        try:
            new_user = User.objects.create(username=username, email=email)
            new_user.set_password(password)
            new_user.save()
            return Response(status=status.HTTP_200_OK)
        except Exception as e:
            return Response(status=status.HTTP_400_BAD_REQUEST)