from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class UserOurRegistration(UserCreationForm):
	first_name = forms.CharField()
	last_name = forms.CharField()

	class Meta:
		model = User
		fields = ['username', 'first_name', 'last_name', 'password1', 'password2']


class UppdateProfile(forms.ModelForm):

	class Meta:
		model = User
		fields = ['username', 'first_name', 'last_name']
