from .models import Client
from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import *

class ClientSignUpForm(UserCreationForm):
 
	class Meta:
		model = Client
		fields=['username','name','email','password1','password2','phone','adresse']

		  
class CommandeForm(forms.ModelForm):
	class Meta:
		model =Commande
		fields =['medicament','status','location']