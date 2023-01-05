from django.shortcuts import render
from project_management_app.forms import ProjectRegistrationForm,TaskRegistrationForm,ProjectTypeForm
from .models import Project,Task
# Create your views here.

def newProject(request):
    if request.method == 'POST':
        form = ProjectRegistrationForm(request.POST)
        context = {'form': form}
        if form.is_valid():
            form.save()
            created = True
            form = ProjectRegistrationForm()
            context = {
                'created': created,
                'form': form,
            }
            return render(request, 'new_project.html', context)
        else:
            return render(request, 'new_project.html', context)
    else:
        form = ProjectRegistrationForm()
        context = {
            'form': form,
        }
        return render(request,'new_project.html', context)

def projectsView(request):
    projects = Project.objects.all()
    tasks = Task.objects.all()
    context = {
        'projects' : projects,
        'tasks' : tasks,
    }
    return render(request, 'projects_view.html', context)

# def ProjectViewById(request, id):
#     project = Project.objects.get(id = id)     
#     return render(request, "project_view_id.html",{"project":project})

def ProjectTypeView(request):
    if request.method == 'POST':
        form = ProjectTypeForm(request.POST)
        context = {'form': form}
        if form.is_valid():
            form.save()
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
        form = TaskRegistrationForm(request.POST)
        context = {'form': form}
        if form.is_valid():
            form.save()
            created = True
            context = {
                'created': created,
                'form': form,
            }
            return render(request, 'new_task.html', context)
        else:
            return render(request, 'new_task.html', context)
    else:
        form = TaskRegistrationForm()
        context = {
            'form': form,
        }
        return render(request,'new_task.html', context)