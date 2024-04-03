from django.contrib.auth import get_user_model
from django.db import models

from core_apps.common.models import TimeStampedUUIDModel

User = get_user_model()


class Comment(models.Model):
    article = models.ForeignKey(
        "articles.Article", on_delete=models.CASCADE, related_name="comments"
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    parent_comment = models.ForeignKey(
        "self", on_delete=models.CASCADE, null=True, blank=True
    )
    content = models.TextField()

    class Meta:
        verbose_name = "Comment"
        verbose_name_plural = "Comments"

    def __str__(self):
        return f"{self.user.first_name} commented on {self.article}"