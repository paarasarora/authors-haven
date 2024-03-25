import requests
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.decorators import action
from rest_framework.viewsets import ModelViewSet
from rest_framework import status
from .models import *
from core_apps.profiles.models import Profile

from django.shortcuts import redirect
from .serialziers import UserSerializer, CreateUserSerializer

from rest_framework.permissions import IsAuthenticated
from authorsHaven.utils import custom_success_response
from django.utils.crypto import get_random_string
from django.conf import settings
from django.utils.html import strip_tags
from authorsHaven.viewsets import ModelViewSet as CustomModelViewSet
from rest_framework.response import Response


EMAIL_HOST_USER = settings.EMAIL_HOST_USER

def pageLogout(request):
    if request.method == "POST":
        
        logout(request)
        response=redirect('home')
        response.delete_cookie('login_token')
        return response


class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    permission_classes = [] 
    serializer_class = CreateUserSerializer

    def create(self, request, *args, **kwargs):

        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)

        headers = self.get_success_headers(serializer.data)
        return custom_success_response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


    @action(detail=False, methods=['get'], permission_classes=[IsAuthenticated, ])
    def my_account(self, request):
        return custom_success_response(self.get_serializer(request.user).data)


"""User Sing-in process
required field: username['email'], password
"""
class Login(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data,
                                           context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            'token': token.key,
            'user_id': user.pk,
            'email': user.email
        })


