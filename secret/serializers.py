from rest_framework import serializers
from .models import Secret, Comment

class SecretSerializer(serializers.ModelSerializer):
    comments = serializers.SerializerMethodField('get_comments')
    class Meta:
        model = Secret
        fields = ("id", "content","creation_time","hugs", "comments")
    
    def get_comments(self, secret):
        return Comment.objects.filter(secret_id=secret.id).values()

class SecretHeaderSerializer(serializers.ModelSerializer):
    class Meta():
        model = Secret
        fields = ("id", "content","creation_time","hugs")

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ("id", "secret_id", "content", "creation_time", "thanks", "reports")