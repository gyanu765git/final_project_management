from django.contrib import admin
from register_app.models import Company
# Register your models here.

class CompanyAdmin(admin.ModelAdmin):
    list_display = ['name','email','city','found_date']
    search_fields = ['name','city']

admin.site.register(Company, CompanyAdmin)    