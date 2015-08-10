from django.conf.urls import url
from django.contrib import admin 
from . import views
 
urlpatterns = [
 url(r'^$', views.home, name='home'),
 url(r'login_form', views.login_form, name='login_form'),
]
