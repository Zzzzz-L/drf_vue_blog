from django.http import JsonResponse
from . import models
from .serializers import ArticleListSerializer
# Create your views here.
def article_list(request):
    articles = models.Article.objects.all()
    serializer = ArticleListSerializer(articles,many=True)
    return JsonResponse(serializer.data, safe=False)