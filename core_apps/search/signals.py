from django.db.models.signals import post_save,post_delete
from django.dispatch import receiver
from django_elasticsearch_dsl.registries import registry
from django.contrib.auth import get_user_model
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

from core_apps.articles.models import Article
from core_apps.articles.read_time_engine import ArticleReadTimeEngine


@receiver(post_save, sender=Article)
def update_document(sender, instance=None,created = False, **kwargs):
    registry.update(instance)

@receiver(post_delete, sender=Article)
def delete_document(sender, instance=None, **kwargs):
    registry.delete(instance)