from rest_framework import serializers
from . import models


class ArticleListSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(allow_blank=True, max_length=100)
    body = serializers.CharField(allow_blank=True)
    created = serializers.DateTimeField()
    updated = serializers.DateTimeField()


class ArticleModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Article
        fields = [
            'id', 'title', 'body'
        ]


class ArticleDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Article
        fields = '__all__'
