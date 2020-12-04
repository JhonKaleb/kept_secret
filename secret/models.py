from datetime import datetime
from django.db import models

class Secret(models.Model):
    id = models.AutoField(primary_key = True)
    content = models.TextField()
    creation_time = models.DateTimeField(default=datetime.now, blank=True)
    hugs = models.IntegerField(default=0)

class Comment(models.Model):
    id = models.AutoField(primary_key = True)
    secret_id = models.ForeignKey( 'Secret', on_delete=models.CASCADE)
    content = models.TextField()
    creation_time = models.DateTimeField(default=datetime.now, blank=True)
    thanks = models.IntegerField(default=0)
    reports = models.IntegerField(default=0)

class CommentAnswer(models.Model):
    id = models.AutoField(primary_key = True)
    comment_id = models.ForeignKey( 'Comment', on_delete=models.CASCADE)
    content = models.TextField()
    creation_time = models.DateTimeField(default=datetime.now, blank=True)
    reports = models.IntegerField(default=0)
