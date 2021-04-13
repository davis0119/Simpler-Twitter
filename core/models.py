from django.db import models
from django.contrib.auth.models import User

class HashTag(models.Model):
    tag = models.CharField(max_length=50)
    def __str__(self):
        return self.tag

class Tweet(models.Model):
    body = models.TextField()
    created_at = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    likes = models.IntegerField()
    hashtags = models.ManyToManyField(HashTag)
