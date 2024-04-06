from django.urls import path,include
from .views import ArticleElasticSearchView
from rest_framework.routers import DefaultRouter

urlpatterns = [
    path('search/', ArticleElasticSearchView.as_view({"get":"list"}), 
         name='search'),
]