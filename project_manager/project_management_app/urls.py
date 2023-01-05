from django.urls import path
from project_management_app import views

app_name = 'project_management_app'

urlpatterns = [

    path('', views.projectsView, name='projects'),
    path('new-project/', views.newProject, name='new-project'),
    path("project-type/",views.ProjectTypeView,name="project-type"),
    path('new-task/', views.newTask, name='new-task'),
]
