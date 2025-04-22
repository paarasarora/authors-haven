from django_elasticsearch_dsl_drf.serializers import DocumentSerializer
from .documents import ArticleDocument
from core_apps.articles.models import Article

class ArticleElasticSearchSerializer(DocumentSerializer):
    class Meta:
        document = ArticleDocument
        model = Article

        fields = [
            "title",
            "body",
            "author",
            "description",
            "slugs",
            "created_at",
        ]

