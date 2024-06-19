from django.shortcuts import render, HttpResponse
from django.http import JsonResponse
import json
from utils.models import (
    Post,
    PostImage,
)



def home_page(request):
    return render(request, 'home.html')

def blog_post(request, blog_id):
    blog_post = Post.objects.get(id=blog_id)
    images=PostImage.objects.filter(post=blog_post)
    print(images)
    return render(request, 'blog.html', {
        'blog_details': blog_post,
        'images':images}
    )

def about(request):
    return HttpResponse('about')

def write_post(request):
    return render(request, 'blog_write.html', )

def write_post_add(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        blog_content = request.POST.get('blog_content')
        image = request.FILES.get('image')

        post = Post.objects.create(
            author=request.user.homie,
            body=blog_content,
            title=title,
            post_image=image
        )
        
        post.save()
        return JsonResponse({'message': 'Blog posted successfully'})

def login(request):
    return HttpResponse('login')