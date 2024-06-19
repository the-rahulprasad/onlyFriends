from django.urls import path
from utils.views import (
    blog_all
)

urlpatterns = [
    path('posts', blog_all, name='posts'),
]