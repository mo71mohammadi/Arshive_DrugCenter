"""DrugCenter_0 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
import patterns as patterns
from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url
from drug import views
from user import views as user_view


urlpatterns = [
    url(r'^$', views.HomePage),
    path('admin/', admin.site.urls),
    url(r'^noskhe/', views.index),
    # path('noskhe/', views.index),
    path('nos/', views.create_book_normal),
    path('noskh/', views.search),
    url(r'^pt/', views.Home),
    url(r'^signup/$', user_view.signup, name='signup'),
    path('user/', include('user.urls')),
    path('accounts/', include('django.contrib.auth.urls')),

]
