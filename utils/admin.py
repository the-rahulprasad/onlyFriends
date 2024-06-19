from django.contrib import admin
from utils.models import (
    Homie,
    Post,
    PostImage,
    )


# Register your models here.
admin.site.register(Homie)
admin.site.register(Post)
admin.site.register(PostImage)