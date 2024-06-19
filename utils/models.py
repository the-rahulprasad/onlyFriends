from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Homie(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE
    )
    first_name = models.CharField(
        max_length=25
    )
    last_name = models.CharField(
        max_length=25
    )
    email = models.EmailField(
        max_length=100,
        unique=True
    )
    def __str__(self):
        return self.first_name + ' ' +self.last_name
    
class Post(models.Model):
    author = models.ForeignKey(
        Homie,
        on_delete=models.CASCADE
    )
    body = models.TextField()
    title = models.CharField(
        max_length=255
    )
    post_image = models.ImageField(upload_to='static/images/blog_post')

class PostImage(models.Model):
    post = models.ForeignKey(
        Post, 
        related_name='images',
        on_delete=models.CASCADE
    )
    image = models.ImageField(upload_to='static/images/blog_post')