<<<<<<< HEAD
from django.conf.urls import url
 
from . import views

urlpatterns = [
 url(r'^$', views.home, name='home'),
 url(r'^highs$', views.highs, name='highs'),
 url(r'^lows$', views.lows, name='lows')

=======

from . import views
from django.conf.urls import include, url

urlpatterns = [
 url(r'^/$', views.home, name='home'),
 url(r'^members/', include('members.urls'), name="members")
>>>>>>> 0dfbdeb4cc76ff4636028d779ef8117857bcab08
]
