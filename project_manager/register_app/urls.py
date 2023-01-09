from django.urls import path
from register_app import views

app_name = 'register_app'

urlpatterns = [
    path("register/", views.register_request, name="register"),
    path("login/", views.login_request, name="login"),
    path("logout", views.logout_request, name= "logout"),
    path('new-company/', views.newCompany, name='new-company'),
    path('company/', views.companyView, name='company'),
    path('company/update/<int:id>',views.companyUpdateView,name="company_update"),
    path('company/delete/<int:id>/',views.companyDelete,name='company_delete'),
    
]
