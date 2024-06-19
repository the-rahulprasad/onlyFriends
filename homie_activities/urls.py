from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from django.views.generic import RedirectView
from homie_activities.views import (
    home_page,
    about,
    write_post,
    write_post_add,
    login,
    blog_post,
    )

from utils.views import (
    blog_all
)



urlpatterns = [
    path('home_page', home_page, name='home_page'),
    path('about', about, name='about'),
    path('post', write_post, name='post'),
    path('login', login, name='login'),
    path('blog_add_post/', write_post_add, name='write_post_add'),
    path('favicon.ico', RedirectView.as_view(url='/static/images/favicon.ico')),
    path('<str:blog_id>', blog_post, name='blog_page'),
    path('posts/', blog_all, name='blog_all'),

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)