from django.shortcuts import render,redirect
from project_management_app.forms import ProjectRegistrationForm,TaskRegistrationForm,ProjectTypeForm
from .models import Project,Task
from django.contrib.auth.models import User
# Create your views here.

def newProject(request):
    if request.method == 'POST':
        form = ProjectRegistrationForm(request.user,request.POST)
        context = {'form': form}
        if form.is_valid():
            obj=form.save(commit=False)
            obj.user=request.user
            obj.save()
            created = True
            context = {
                'created': created,
                'form': form,
            }
            return redirect("project_management_app:projects")
        else:
            return render(request, 'new_project.html', context)
    else:
        form = ProjectRegistrationForm(request.user)
        context = {
            'form': form,
        }
        return render(request,'new_project.html', context)

def projectsView(request):
    if request.user.is_superuser:
        projects=Project.objects.all()
    else:    
        projects = Project.objects.filter(user=request.user)
    context = {
        'projects' : projects,
    }
    return render(request, 'projects_view.html', context)

def projectUpdateView(request, id):
    objects = Project.objects.get(id=id)
    tasks=Task.objects.filter(project_id=id)
    if request.method == 'POST':
        form = ProjectRegistrationForm(request.user,request.POST, instance=objects)
        if form.is_valid():
            form.save()
            return redirect("project_management_app:projects")
    else:
        form = ProjectRegistrationForm(request.user,instance=objects)
    return render(request,"project_update.html",{'form': form,"objects":objects,"tasks":tasks})

def projectDelete(request, id):
  project_object = Project.objects.get(id=id)
  project_object.delete()
  return redirect("project_management_app:projects")

def ProjectTypeView(request):
    if request.method == 'POST':
        form = ProjectTypeForm(request.POST)
        context = {'form': form}
        if form.is_valid():
            obj=form.save(commit=False)
            obj.user=request.user
            obj.save()
            created = True
            context = {
                'created': created,
                'form': form,
            }
            return render(request, 'project_type.html', context)
        else:
            return render(request, 'project_type.html', context)
    else:
        form = ProjectTypeForm()
        context = {
            'form': form,
        }
        return render(request,'project_type.html', context)

def newTask(request):
    if request.method == 'POST':
        form = TaskRegistrationForm(request.user,request.POST)
        context = {'form': form}
        if form.is_valid():
            obj=form.save(commit=False)
            obj.user=request.user
            obj.save()
            created = True
            context = {
                'created': created,
                'form': form,
            }
            return redirect("project_management_app:tasks")
    else:
        form = TaskRegistrationForm(request.user)
        context = {
            'form': form,
        }
        return render(request,'new_task.html', context)

def taskView(request):
    if request.user.is_superuser:
        tasks = Task.objects.all()  
    else:
        tasks=Task.objects.filter(user=request.user) 
    context = {
        'tasks' : tasks,
    }
    return render(request, 'tasks_view.html', context)        

def taskUpdateView(request, id):
    objects = Task.objects.get(id=id)
    if request.method == 'POST':
        form = TaskRegistrationForm(request.user,request.POST, instance=objects)
        if form.is_valid():
            form.save()
            return redirect("project_management_app:tasks")
    else:
        form = TaskRegistrationForm(request.user,instance=objects)

    return render(request,"task_update.html",{'form': form ,"objects":objects})    

def taskDelete(request, id):
  task_object = Task.objects.get(id=id)
  task_object.delete()
  return redirect("project_management_app:tasks")