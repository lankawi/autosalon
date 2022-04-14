from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import *
from myhome.models import Service

def register(request):
	if request.method == "POST":
		form = UserOurRegistration(request.POST);
		if form.is_valid():
			form.save()
			username = form.cleaned_data.get('username')

			new_user = User.objects.get(username = username)

			return redirect('index')
	else:
		form = UserOurRegistration()
	return render(request, 'users/registration.html', {'form': form})

def edit_profile(request):
	if request.method == "POST":		
		form = UppdateProfile(request.POST, instance = request.user);
		if form.is_valid():
			form.save()
			return redirect('prof')
	else:
		form = UppdateProfile(instance = request.user)
	return render(
		request,
		'users/profile.html',
		{'form':form}
	)
	
#def pay_profile(request):
#	serv_inst = Service.objects.all().filter(user = request.user).update(sub=2)
#	return redirect('prof')
