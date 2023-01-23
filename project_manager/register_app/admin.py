from django.contrib import admin
from register_app.models import Company,UserProfile,NormalUser
# Register your models here.
admin.site.register(NormalUser)
admin.site.register(UserProfile)
admin.site.register(Company)    
