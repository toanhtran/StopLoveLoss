from django.shortcuts import render
from django.http import HttpResponse
<<<<<<< HEAD
# from django.contrib.auth.models import User
# from django.contrib.auth import authenticate, login, logout
# from django.core.urlresolvers import reverse
=======
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.core.urlresolvers import reverse



>>>>>>> 0dfbdeb4cc76ff4636028d779ef8117857bcab08


# Create your views here.
def home(request):
	return render(request,'Endit/home.html',{})

<<<<<<< HEAD
def highs(request):
	return render(request,'Endit/HiLo.html',{})

def lows(request):
	return render(request, 'Endit/lows.html', {})
=======
>>>>>>> 0dfbdeb4cc76ff4636028d779ef8117857bcab08
