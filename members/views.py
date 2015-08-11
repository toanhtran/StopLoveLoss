from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.core.urlresolvers import reverse


# Create your views here.

def index(request):
	if not request.user.is_authenticated():
		return HttpResponseRedirect(reverse('members:login'))
 	return render(request, 'members/index.html', {})

def signup_form(request):
	return render(request, 'members/signup.html', {})

def login(request):
	return render(request, 'members/login.html', {})
