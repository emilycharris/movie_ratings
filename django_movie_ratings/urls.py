"""django_movie_ratings URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin

from movieratings import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.index_view, name='index'),
    url(r'^raters/(?P<rater_id>\w+)$', views.rater_view, name='raters'),
    url(r'^movies/(?P<movie_id>\w+)/$', views.movie_view, name='movies'),
]
