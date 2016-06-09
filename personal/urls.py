from django.conf.urls import url, include
from django.views.generic import ListView, DetailView
from . import views
from blog.models import Post

urlpatterns = [
    url(r'^$',views.base,name='base'),
    url(r'^index/$',views.base,name='index'),
    url(r'^contact/$',views.contact,name='contact'),
    url(r'^accounts/profile/$',views.profile,name='profile'),
    url(r'^accounts/profile/create$',views.create,name='create'),
    url(r'^blog/$',ListView.as_view(queryset=Post.objects.all().order_by("-date"),template_name="blog/blog.html")),
    url(r'^blog/(?P<pk>\d+)$', DetailView.as_view(model=Post,template_name='blog/post.html')),
    url(r'^create/',views.create,name="create"),
    ]