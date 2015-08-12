from django.conf.urls import url
 
from . import views

urlpatterns = [
 url(r'^$', views.home, name='home'),
 url(r'^highs$', views.highs, name='highs'),
 url(r'^lows$', views.lows, name='lows')

]
