"""curta URL Configuration

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
from django.contrib import admin
from django.urls import path, re_path, include

from curta.central import views as views_central

urlpatterns = [
    path('admin/', admin.site.urls),
    # re_path('^$', views_central.homepage, name='homepage'),
    re_path('^$', views_central.Homepage.as_view(), name='homepage'),
    re_path('^login/$', views_central.login, name='login'),
    re_path('^logout/$', views_central.logout, name='logout'),
    re_path('^auth/', include('social_django.urls', namespace='social')),
    re_path(r'^c/', views_central.redirect_url, name='redirecionar'),

]
