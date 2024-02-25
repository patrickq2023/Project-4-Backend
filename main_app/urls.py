from django.urls import path
from .views import image_detail, home


urlpatterns = [
    path('', home, name='home'),
    path('api/image/<int:image_id>/', image_detail, name='image_detail_api')
]