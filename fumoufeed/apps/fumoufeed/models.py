from django.db import models

# Create your models here.

class People(models.Model):
    fuid = models.CharField(max_length=255, primary_key=True)
    title = models.CharField(max_length=511, null=True, blank=True)
    name = models.CharField(max_length=511, null=True, blank=True)

class Post(models.Model):
    author = models.ForeignKey(People)
    fpid = models.CharField(max_length=255, primary_key=True)
    priority = models.IntegerField(default=10)
    live = models.BooleanField(default=True)
    create_time = models.DateTimeField(auto_now_add=True)
