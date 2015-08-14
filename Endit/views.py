from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.core.urlresolvers import reverse
from members.views import User
from django.shortcuts import redirect
from Endit.models import Highs, Lows


# Create your views here.
def home(request):
	return render(request,'Endit/home.html',{})

def create_high(request):
	return render(request, 'Endit/high_form.html', {})

def new_highs(request):
	new_highs=Highs()
	new_highs.description = request.POST.get('highs')
	new_highs.user_id = request.user.id
	new_highs.save()
	return redirect('Endit:show_HiLo')

def show_HiLo(request):
	highs = Highs.objects.filter(user_id=request.user.id)
	lows = Lows.objects.filter(user_id=request.user.id)
	return render(request,'Endit/HiLo.html',{'highs':highs,'lows':lows})

	# total = 0
	# for high in highs:
	# 	total += highs.description
	# return render(request,'Endit/HiLo.html',{'highs':highs,'lows':lows,'total':total})
	

def create_low(request):
	return render(request, 'Endit/low_form.html',{})

def new_lows(request):
	new_lows=Lows()
	new_lows.desciption = request.POST.get('lows')
	new_lows.user_id = request.user.id
	new_lows.save()
	return redirect('Endit:show_HiLo')
