from django import forms
from django.forms import ModelForm
from myProfiles.models import UserProfile
from django.contrib.auth.models import User
from registration.forms import RegistrationForm

class MyRegistrationForm(RegistrationForm):
	first_name = forms.CharField(label='Your First Name')
	last_name = forms.CharField(label='Your Last Name')
	zipcode = forms.CharField(label='Your Zip Code', required=True)

class MyProfileForm(ModelForm):
	class Meta:
		model = UserProfile
		fields = ('image', 'email', 'phone', 'notes')
