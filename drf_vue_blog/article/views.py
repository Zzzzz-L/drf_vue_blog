from django.http import JsonResponse, Http404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.views import APIView

from . import models
from .serializers import ArticleListSerializer, ArticleModelSerializer, ArticleDetailSerializer


# Create your views here.
def article_lists(request):
    articles = models.Article.objects.all()
    serializer = ArticleModelSerializer(articles, many=True)
    return JsonResponse(serializer.data, safe=False)


@api_view(['GET', 'POST'])
def article_list(request):
    if request.method == 'GET':
        articles = models.Article.objects.all()
        serializer = ArticleModelSerializer(articles, many=True)
        return JsonResponse(serializer.data, safe=False)
    elif request.method == 'POST':
        serializer = ArticleModelSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)


class ArticleDetail(APIView):
    """文章详情视图"""

    def get_object(self, pk):
        """获取单个文章对象"""
        try:
            # pk 即主键，默认状态下就是 id
            return models.Article.objects.filter(pk=pk)[0]
        except:
            raise Http404

    def get(self, request, pk):
        article = self.get_object(pk)
        serializer = ArticleDetailSerializer(article)
        # 返回 Json 数据
        return Response(serializer.data)

    def put(self, request, pk):
        article = self.get_object(pk)
        serializer = ArticleDetailSerializer(article, data=request.data)
        # 验证提交的数据是否合法
        # 不合法则返回400
        if serializer.is_valid():
            # 序列化器将持有的数据反序列化后，
            # 保存到数据库中
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        article = self.get_object(pk)
        article.delete()
        # 删除成功后返回204
        return Response(status=status.HTTP_204_NO_CONTENT)
