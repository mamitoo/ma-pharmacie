from django.shortcuts import render,redirect
from django.views.generic import CreateView
from .models import Client
from .form import *
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
# Create your views here.

def ClientRegister(request):
	form =ClientSignUpForm(request.POST or None)
	if form.is_valid():
		user      = form.save(commit=False)
		username  =	form.cleaned_data['name']
		password  = form.cleaned_data['password1']
		user.set_password(password)
		user.save()
		user = authenticate(username=username,password=password)
		if user is not None:
			if user.is_active:
				login(request,user)
				return redirect("profile")
			else:
				return render(request,'Depot/login.html',{'error_message':'Your account disable'})
	context ={
		'form':form
	}			
	return render(request,'Depot/signup.html',context)


 
def customerLogin(request):
	if request.method=="POST":
		username = request.POST['username']
		password = request.POST['password']
		user     = authenticate(username=username,password=password)
		if user is not None:
			if user.is_active:
				login(request,user)
				return redirect("profile")
			else:
				return render(request,'Depot/login.html',{'error_message':'Your account disable'})
		else:
			return render(request,'Depot/login.html',{'error_message': 'Invalid Login'})
	return render(request,'Depot/login.html')



def Logout(request):
	if request.user.is_active:
		logout(request)
		return redirect("login")
	 

 
@login_required(login_url='/login') 
def createCommande(request):
	form=CommandeForm(request.POST or None)
	if form.is_valid():
		instance = form.save(commit=False)
		instance.client = request.user
		instance.save()
		return redirect("profile")
	context={
	'form':form
	}
	return render(request,'Depot/Profile.html',context)

