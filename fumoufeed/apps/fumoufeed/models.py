from django.db import models

# Create your models here.

class People(models.Model):
    name = models.CharField(max_length=255)
    title = models.CharField(max_length=511)
    fb_id = models.CharField(max_length=511)

class Post(models.Model):
    author = models.ForeignKey(People)
    feed_id = models.CharField(max_length=511)
    priority = models.IntegerField(default=10)
    live = models.BooleanField(default=True)
    create_time = models.DateTimeField(auto_now_add=True)
