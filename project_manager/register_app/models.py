from django.db import models
from django.contrib.auth.models import User
from project_management_app.models import Project
# Create your models here.

class Company(models.Model):
    name = models.CharField(max_length=80)
    email = models.EmailField()
    city = models.CharField(max_length=50)
    found_date = models.DateField()
    user = models.ForeignKey(User,null=True, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = 'Companies'
        ordering = ('name',)


    def __str__(self):
        return (self.name)

class UserProfile(models.Model):
    user = models.ForeignKey(User,null=True,on_delete=models.CASCADE)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    project = models.ManyToManyField(Project, blank=True)
    img    = models.ImageField(upload_to='base_app/static/img/avatar', blank=True, default='base_app/static/img/avatar/blank_profile.png')

    def __str__(self):
        return (str(self.user))