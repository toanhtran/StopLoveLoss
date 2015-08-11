
from . import views
from django.conf.urls import include, url

urlpatterns = [
 url(r'^/$', views.home, name='home'),
 url(r'^members/', include('members.urls'), name="members")
]
