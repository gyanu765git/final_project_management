from django.contrib import admin
from register_app.models import Company,UserProfile,NormalUser
# Register your models here.

class CompanyAdmin(admin.ModelAdmin):
    list_display = ['name','email','city','found_date']
    search_fields = ['name','city']

class UserProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'company',]

admin.site.register(UserProfile, UserProfileAdmin)
admin.site.register(Company, CompanyAdmin)    
admin.site.register(NormalUser)