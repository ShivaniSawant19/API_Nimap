from django.db import models

# Create your models here.
from django.db import models

# Create your models here.

class Project(models.Model):
    id = models.IntegerField(primary_key= True)
    project_name = models.CharField(max_length= 200)
    #created_at = models.DateField(max_length=20,null=True,blank=True)
    created_by = models.CharField(max_length= 200)
    
class Client1(models.Model):
    id = models.IntegerField(primary_key= True)
    client_name = models.CharField(max_length= 200)
    created_at = models.DateField(max_length=20,null=True,blank=True)