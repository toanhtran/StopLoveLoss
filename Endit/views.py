from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.core.urlresolvers import reverse





# Create your views here.
def home(request):
	return render(request,'Endit/home.html',{})

