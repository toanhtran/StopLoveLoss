from django.conf.urls import url
 
from . import views

urlpatterns = [
 url(r'^$', views.index, name='index'),
<<<<<<< HEAD
 url(r'^register$', views.register, name='register'),
 url(r'^signup$', views.signup_form, name='signup'),
 url(r'^login$', views.login_form, name='login'),
 url(r'^login_user$', views.login_user, name='login_user'),
 url(r'^logout$', views.logout_view, name='logout_view')
=======
 url(r'^signup$', views.signup_form, name='signup'),
 url(r'^login$', views.login, name='login')


>>>>>>> 0dfbdeb4cc76ff4636028d779ef8117857bcab08
 ]