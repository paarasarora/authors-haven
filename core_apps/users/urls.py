from django.urls import path, include, re_path
from rest_framework.routers import DefaultRouter
from .views import *
app_name = 'users'

router = DefaultRouter()
router.register('users', UserViewSet)

urlpatterns = [
   path('login/', Login.as_view(), name='user_login')
]