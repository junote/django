from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^bootstrap', views.bootstrap, name='bootstrap'),
    url(r'^bs2', views.bs2, name='bs2'),
]
