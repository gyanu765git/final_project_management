from django.shortcuts import  render, redirect
from .forms import RegistrationForm
from django.contrib.auth import login,authenticate,logout
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm 
from .forms import CompanyRegistrationForm
from .models import Company
from .forms import ProfilePictureForm,NormalUserForm
from django.contrib.auth.models import User
from register_app.models import NormalUser


def register_request(request):
	if request.method == "POST":
		form = RegistrationForm(request.POST)
		if form.is_valid():
			user = form.save()
			login(request, user)
			messages.success(request, "Registration successful.")
			return redirect("register_app:new-company")
		messages.error(request, "Unsuccessful registration. Invalid information.")
	form = RegistrationForm()
	return render (request=request, template_name="register.html", context={"register_form":form})
  


def login_request(request):
	if request.method == "POST":
		form = AuthenticationForm(request, data=request.POST)
		if form.is_valid():
			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password')
			user = authenticate(username=username, password=password)
			if user is not None:
				login(request, user)
				messages.info(request, f"You are now logged in as {username}.")
				return redirect("base_app:index")
			else:
				messages.error(request,"Invalid username or password.")
		else:
			messages.error(request,"Invalid username or password.")
	form = AuthenticationForm()
	return render(request=request, template_name="login.html", context={"login_form":form})


def logout_request(request):
	logout(request)
	messages.info(request, "You have successfully logged out.") 
	return redirect("base_app:home")


def newCompany(request):
    if request.method == 'POST':
        form = CompanyRegistrationForm(request.POST)
        context = {'form':form}
        if form.is_valid():
            obj= form.save(commit=False)
            obj.user= request.user
            obj.save()
            created = True
            form = CompanyRegistrationForm()
            context = {
                'created' : created,
                'form' : form,
                       }
            return redirect("base_app:index")
        else:
            return render(request, 'new_company.html', context)
    else:
        form = CompanyRegistrationForm()
        context = {
            'form' : form,
        }
        return render(request, 'new_company.html', context)

def companyUpdateView(request, id):
    objects = Company.objects.get(id=id)
    if request.method == 'POST':
        form = CompanyRegistrationForm(request.POST, instance=objects)
        if form.is_valid():
            form.save()
            return redirect("register_app:company")
    else:
        form = CompanyRegistrationForm(instance=objects)
    return render(request,"company_update.html",{'form': form,"objects":objects})      
	
def companyDelete(request, id):
  project_object = Company.objects.get(id=id)
  project_object.delete()
  return redirect("register_app:company")

def companyView(request):
    if request.user.is_superuser:
        companies = Company.objects.all()
    else:
        companies=Company.objects.filter(user=request.user)   
    context = {
        'companies' : companies,
    }
    return render(request, 'company_view.html', context)   
      
def createNewUser(request):
    if request.method == 'POST':
        form = NormalUserForm(request.POST)
        context = {'form':form}
        if form.is_valid():
            obj= form.save(commit=False)
            obj.user= request.user
            obj.save()
            created = True
            form = NormalUserForm()
            context = {
                'created' : created,
                'form' : form,
                       }
            return redirect("register_app:users")
        else:
            return render(request, 'new_user.html', context)
    else:
        form = NormalUserForm()
        context = {
            'form' : form,
        }
        return render (request=request, template_name="new_user.html", context={"form":form})

def userDelete(request, id):
  user_object = NormalUser.objects.get(id=id)
  user_object.delete()
  return redirect("register_app:users")

def userUpdateView(request, id):
    objects = NormalUser.objects.get(id=id)
    if request.method == 'POST':
        form = NormalUserForm(request.POST, instance=objects)
        if form.is_valid():
            form.save()
            return redirect("register_app:users")
    else:
        form = NormalUserForm(instance=objects)
    return render(request,"user_update.html",{'form': form,"objects":objects})   

def usersView(request):
    if request.user.is_superuser:
        users = NormalUser.objects.all()
    else:
        users=NormalUser.objects.filter(user=request.user)    
    context = {
        'users' : users
    }
    return render(request, 'users_view.html', context)        
	

def profile(request):
    if request.method == 'POST':
        img_form = ProfilePictureForm(request.POST, request.FILES)
        print('PRINT 1: ', img_form)
        context = {'img_form' : img_form }
        if img_form.is_valid():
            img_form.save(request)
            updated = True
            context = {'img_form' : img_form, 'updated' : updated }
            return render(request, 'profile.html', context)
        else:
            return render(request, 'profile.html', context)
    else:
        img_form = ProfilePictureForm()
        context = {'img_form' : img_form }
        return render(request, 'profile.html', context)

def renderprofile(request):
    return render(request,"profile.html")
