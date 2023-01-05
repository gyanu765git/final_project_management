
from django.urls import path
from base_app import views

app_name = 'base_app'

urlpatterns = [
    path("",views.renderHome,name="home"), 
    path("index/",views.renderIndex,name="index"), 
    path('dashboard/', views.dashboard, name='dashboard'),
]
