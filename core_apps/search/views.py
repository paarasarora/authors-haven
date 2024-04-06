from django_elasticsearch_dsl_drf.filter_backends import FilteringFilterBackend,IdsFilterBackend,OrderingFilterBackend,DefaultOrderingFilterBackend,SearchFilterBackend
from django_elasticsearch_dsl_drf.viewsets import DocumentViewSet
from .documents import ArticleDocument
from .serializers import ArticleDocumentSerializer
from .models import Article
from rest_framework import permissions


# Create your views here.

class ArticleElasticSearchView(DocumentViewSet):
    document = ArticleDocument
    serializer_class = ArticleDocumentSerializer
    lookup_field = "id"
    permission_classes = [permissions.AllowAny]

    filter_backends = [
        FilteringFilterBackend,
        IdsFilterBackend,
        OrderingFilterBackend,
        DefaultOrderingFilterBackend,
        SearchFilterBackend
    ]

    search_fields = ("title","description","body","author__first_name","author__last_name","tags")

    filter_fields = {
        "slugs": "slugs.raw",
        "created_at": "created_at",
        "title": "title",
        "description": "description",
        "body": "body",
        "author__first_name": "author__first_name",
        "author__last_name": "author__last_name",
        "tags": "tags",
    }

    ordering_fields = {
        "created_at": "created_at",
    }
    ordering = ("-created_at")
