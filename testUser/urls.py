#python
from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url('registerform', views.indexForm, name='indexForm'),
    url('register', views.register, name='register'),
    url('home', views.home, name='home'),
]
