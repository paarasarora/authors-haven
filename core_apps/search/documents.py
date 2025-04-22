from django_elasticsearch_dsl import Document,fields
from django_elasticsearch_dsl.registries import registry
from core_apps.articles.models import Article

@registry.register_document
class ArticleDocument(Document):
    title = fields.TextField(attr="title")
    description = fields.TextField(attr="description")
    body = fields.TextField(attr="body")
    author_first_name = fields.TextField(attr="author__first_name")
    author_last_name = fields.TextField(attr="author__last_name")
    
    class Index:
        name = "articles"
        settings = {
            "number_of_shards": 1,
            "number_of_replicas": 0
            }

    class Django:
        model = Article
        fields = [
            "created_at"
        ]
    
    def prepare_author_first_name(self, obj):
        return obj.author.first_name

    def prepare_author_last_name(self, obj):
        return obj.author.last_name
    
    def prepare_tags(self, obj):
        return [tag.name for tag in obj.tags.all()]