from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.core.urlresolvers import reverse
from members.views import User
from django.shortcuts import redirect
from Endit.models import Highs, Lows

# Create your views here.
def home(request):
	return render(request,'Endit/home.html',{})
def quiz(request):
	return render(request,'Endit/quizIndex.html',{})

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
	
	total_highs = 0
	total_lows = 0
	for high in highs:
		total_highs += 1
	print total_highs
	for low in lows:
		total_lows += 1
	print total_lows
	if total_highs:
		ratio = float(total_lows)/total_highs
	else:
		ratio = 0
		message = 'none'
	if ratio > 0.0:
		message = "Your relationship is BAD. Trash day is fast approaching."
	if ratio > 0.03:
		message = "Your relationship is okay. You are Brozne. You would last longer than Hollywood couple."
	if ratio > 0.06:
		message = "Your relationship is awesome! You are Platinum. The notebook couple has nothing on you." 
	if ratio >  0.1:
		message = "Your relationship could be better. Your relationship is So-So"
	if ratio > 1.0:
		message = "Your relationship is heading towards splitsville. It's time to give the, 'The Talk'."
	if ratio > 3.0:
		message = "Your relationship sucks! It is time to END.IT.NOW."
	
	level = 3

	return render(request,'Endit/HiLo.html',{'highs':highs,'lows':lows,'total_highs':str(total_highs),'total_lows':str(total_lows),"message":message,'level':level})


def delete_Hi(request, high_id):
	highs=Highs.objects.get(id=high_id)
	highs.delete()
	return HttpResponseRedirect(reverse('Endit:show_HiLo'))

def delete_Lo(request, low_id):
	lows=Lows.objects.get(id=low_id)
	lows.delete()
	return HttpResponseRedirect(reverse('Endit:show_HiLo'))

def create_low(request):
	return render(request, 'Endit/low_form.html',{})

def new_lows(request):
	new_lows=Lows()
	new_lows.description = request.POST.get('lows')
	new_lows.level = request.POST.get('level')[0]
	new_lows.user_id = request.user.id
	new_lows.save()
	return redirect('Endit:show_HiLo')

# def dealbreakers(request):
	# return HttpResponse("This is the dealbreak page")
# 	new_lows=Lows()
# 	new_lows.description = request.POST.get('lows')
# 	new_lows.level = request.POST.get('level')[0]
# 	new_lows.user_id = request.user.id
# 	new_lows.save()
# 	for low in lows:
# 		total_lows += 1
# 	print total_lows
# 	for level in lows_level:
# 		total_level +=1

# 	return render(request, 'Endit/dealbreakers.html',{'lows':lows,'total_lows':str(total_lows)'total_level':total_level})
		
