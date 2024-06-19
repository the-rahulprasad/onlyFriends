from django.shortcuts import render
from django.http import JsonResponse
from utils.serializers import PostFullDetailSerializer
from utils.models import Post


def blog_all(request):
    posts = Post.objects.all()
    serialized_post = PostFullDetailSerializer(posts, many=True)
    return JsonResponse({'posts': serialized_post.data}, safe=True) 