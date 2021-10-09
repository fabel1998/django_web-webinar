from django.urls import path
from .views import index, register, platform


app_name = 'users'
urlpatterns = [
    path('', index, name='index'),
    path('platform/', platform, name='platform'),
    path('register/', register, name='register'),
]