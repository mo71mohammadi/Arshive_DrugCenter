from django.urls import path, include
from django.conf.urls import url
from . import  views

app_name = 'user'


urlpatterns = [
    url(r'^$', views.index.as_view(), name='index'),
    url(r'^molecule/(?P<pk>[0-9]+)', views.detail.as_view(), name='detail'),
    url(r'^molecule/generic/(?P<pk>[0-9]+)', views.detai.as_view(), name='detai'),

]