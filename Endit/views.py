from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login





# Create your views here.
def home(request):
	# return HttpResponse("This is the index page.")
	return render(request,'Endit/home.html',{})

def login_form(request,user):
	# return HttpResponse("This will be the login page.")
	return render(request,'Endit/login.html',{})

def userInfo(request):
	request_context = RequestContext(request)
	request_context.push({"my_name":"ToAnh"})
	return render(reqest,'Endit/userInfo.html',request_context)