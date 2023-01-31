from django.shortcuts import render
from django.contrib.auth.models import User
from project_management_app.models import Project,Task
from register_app.models import Company
# Create your views here.

def renderHome(request):
    return render(request,"base_home.html")

def renderIndex(request):
    return render(request,"index.html")


def dashboard(request):
    if request.user.is_superuser:
        companies = Company.objects.all()
        projects = Project.objects.all()
        tasks=Task.objects.all()
    else:
        companies = Company.objects.filter(user=request.user)
        projects = Project.objects.filter(user=request.user)
        tasks=Task.objects.filter(user=request.user) 
    context = {
        'companies' : companies,
        'projects' : projects,
        'tasks' : tasks,
    }
    return render(request, 'dashboard.html', context)    