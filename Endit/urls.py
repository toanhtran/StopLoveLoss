
from django.conf.urls import url
 
from . import views

urlpatterns = [
 url(r'^$', views.home, name='home'),
 url(r'^create_high$', views.create_high, name='create_high'),
 url(r'^new_highs$', views.new_highs, name='new_highs'),
 url(r'^show_HiLo$', views.show_HiLo, name='show_HiLo'),
 url(r'^create_low$', views.create_low, name='create_low'),
 url(r'^new_lows$', views.new_lows, name='new_lows')

]