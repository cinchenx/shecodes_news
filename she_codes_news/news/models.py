from django.db import models
from django.contrib.auth import get_user_model


class NewsStory(models.Model):
    title = models.CharField(max_length=200)
    # author = models.CharField(max_length=200)
    author = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE
        )
    pub_date = models.DateTimeField()
    content = models.TextField()
    # ok if it's empty, will use placeholder image in its place
    image = models.URLField(null=True, blank=True)

class AddComment(models.Model):
    story = models.ForeignKey(
        NewsStory, related_name="comments", on_delete=models.CASCADE
    )
    author = models.ForeignKey(
        get_user_model(), related_name="comments",
        on_delete=models.CASCADE
        )
    pub_date = models.DateTimeField(auto_now="True")
    content = models.TextField()
    