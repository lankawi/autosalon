from django.shortcuts import render, redirect
from django.urls import reverse
from .models import Brand, Modell, Body_type, Body_color, Country, Insurance, Automobile, Type_of_service, Service
from .forms import *
from django.views.decorators.csrf import csrf_exempt

def index(request):
	autos = Automobile.objects.order_by('-date')
	return render(request, 'myhome/homePage.html', {'autos':autos})

def exit(request):
	autos = Automobile.objects.order_by('-date')
	return render(request, 'myhome/exit.html', {'autos':autos})

def show_auto(request, auto_id):
	auto_inst = Automobile.objects.get(pk=auto_id)
	auto = Automobile.objects.all()
	user_inst = User.objects.get(username = request.user)
	if request.method == "POST":
		form = ServiceForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('show_auto')
	else:
		form = ServiceForm()

	return render(
		request,
		'myhome/show_auto.html',
		{'auto':auto, 'auto_inst':auto_inst, 'form':form, 'user_inst':user_inst}
	)


def autos_by_brand(request, brand_name):
	Brand_list = Brand.objects.all()
	Brand_inst = Brand.objects.get(brand = brand_name)
	autos_list = Automobile.objects.all().filter(brand = brand_inst.id)
	return render(
		request,
		'myhome/autos.html',
		{'autos_list':autos_list, 'brand_list':bran_list}
	)