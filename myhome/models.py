from django.db import models
from django.contrib.auth.models import User

from PIL import Image
from .models import Image

class Brand(models.Model):
	brand = models.CharField(max_length=45, verbose_name = "Марка автомобиля")

	def __str__(self):
		return self.brand

	class Meta:
		verbose_name = 'Марка автомобиля'
		verbose_name_plural = 'Марки автомобилей'

class Modell(models.Model):
	modell = models.CharField(max_length=45, default = 'RS6', verbose_name = "Модель автомобиля")

	def __str__(self):
		return self.modell

	class Meta:
		verbose_name = 'Модель автомобиля'
		verbose_name_plural = 'Модели автомобилей'

class Body_type(models.Model):
	body_type = models.CharField(max_length=45, default = 'универсал', verbose_name = "Тип кузова")

	def __str__(self):
		return self.body_type

	class Meta:
		verbose_name = 'Тип кузова'
		verbose_name_plural = 'Типы кузова'

class Body_color(models.Model):
	color = models.CharField(max_length=45, default = 'черный', verbose_name = "Цвет кузова")

	def __str__(self):
		return self.color

	class Meta:
		verbose_name = 'Цвет кузова'
		verbose_name_plural = 'Цвета кузова'

class Country(models.Model):
	country = models.CharField(max_length=45, default = 'Германия', verbose_name = "Страна-производитель")

	def __str__(self):
		return self.country

	class Meta:
		verbose_name = 'Страна-производитель'
		verbose_name_plural = 'Страны-производители'

class Insurance(models.Model):
	insurance = models.CharField(max_length=45, default = 'каско', verbose_name = "Страхование")

	def __str__(self):
		return self.insurance

	class Meta:
		verbose_name = 'Страхование'
		verbose_name_plural = 'Страхование'

class Automobile(models.Model):
	FUEL = {
		('benzine', 'бензин'),
		('diesel', 'дизель'),
		('electro', 'электро'),
		('hybrid', 'гибрид'),
	}
	GEARBOX = {
		('manual', 'механика'),
		('automatic', 'автомат'),
	}
	DRIVE = {
		('RWD', 'задний'),
		('FWD', 'передний'),
		('4WD', 'полный (постоянный и подключаемый)'),
		('AWD', 'автоматически подключаемый полный'),
	}
	COLOR = {
		('light', 'светлый'),
		('dark', 'темный'),
	}

	brand = models.ForeignKey(Brand, default = '1', on_delete=models.CASCADE, verbose_name = "Марка автомобиля")
	modell = models.ForeignKey(Modell, default = '1', on_delete=models.PROTECT, verbose_name = "Модель автомобиля")
	year = models.CharField(max_length=45, default = '2021', verbose_name = "Год")
	type_of_fuel = models.CharField(max_length=45, choices=FUEL, default = 'benzine', verbose_name = "Вид топлива")
	engine_volume = models.CharField(max_length=6, default = '4.0 л', verbose_name = "Объем двигателя")
	power = models.CharField(max_length=10, default = '600 л.с.', verbose_name = "Мощность")
	gearbox = models.CharField(max_length=45, choices=GEARBOX, default = 'automatic', verbose_name = "КПП")
	body_type = models.ForeignKey(Body_type, max_length=45, default = '1', on_delete=models.PROTECT, verbose_name = "Тип кузова")
	drive_unit = models.CharField(max_length=45, choices=DRIVE, default = 'RWD', verbose_name = "Привод")
	body_color = models.ForeignKey(Body_color, max_length=45, default = '1', on_delete=models.PROTECT, verbose_name = "Цвет кузова")
	interior_color = models.CharField(max_length=45, choices=COLOR, default = 'dark', verbose_name = "Цвет салона")
	country = models.ForeignKey(Country, max_length=45, default = '1', on_delete=models.PROTECT, verbose_name = "Страна")
	vin = models.CharField(max_length=16, default = '1', verbose_name = "VIN")
	date = models.DateTimeField(verbose_name="Дата выхода")
	description = models.TextField(max_length=1000, default = '4-х дверная', verbose_name = "Описание")
	price = models.IntegerField(default = 'BYN', verbose_name = "Цена")
	insurance = models.ForeignKey(Insurance, max_length=200, default = '1', on_delete=models.PROTECT, verbose_name = "Страхование")
	image1 = models.FileField(blank = True, upload_to ='myhome', verbose_name = 'Ссылка картинки')
	image2 = models.FileField(blank = True, upload_to ='myhome', verbose_name = 'Ссылка картинки')
	image3 = models.FileField(blank = True, upload_to ='myhome', verbose_name = 'Ссылка картинки')
	image4 = models.FileField(blank = True, upload_to ='myhome', verbose_name = 'Ссылка картинки')
	image5 = models.FileField(blank = True, upload_to ='myhome', verbose_name = 'Ссылка картинки')

	def __str__(self):
		return self.brand.brand+' | '+self.modell.modell+' | '+self.year

	class Meta:
		verbose_name = 'Автомобиль'
		verbose_name_plural = 'Автомобили' 

class Type_of_service(models.Model):
	type_of_service = models.CharField(max_length=45, default = 'бронь', verbose_name = "Вид услуги")

	def __str__(self):
		return self.type_of_service

	class Meta:
		verbose_name = 'Вид услуги'
		verbose_name_plural = 'Виды услуг'

class Service(models.Model):
	# nazvanie = models.CharField(max_length=65, default = 'Audi RS6 2019', verbose_name = "Данные автомобиля")
	type_of_service = models.ForeignKey(Type_of_service, default = '1', on_delete=models.PROTECT, verbose_name = "Вид услуги")
	user = models.ForeignKey(User, default = '1', on_delete=models.PROTECT, verbose_name = "Пользователь")
	date_of_service = models.DateTimeField(verbose_name="Дата услуги")

	def __str__(self):
		return self.type_of_service.type_of_service+' | '+str(self.date_of_service)	

	class Meta:
		verbose_name = 'Услуга'
		verbose_name_plural = 'Услуги'