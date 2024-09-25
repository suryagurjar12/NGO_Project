from django.db import models

# Create your models here.

As_role=[ 
    ('User','User'),
    ('Admin','Admin')
]
 
class RegistrationModel(models.Model):
    name=models.CharField(max_length=45 )
    email=models.EmailField()
    contact=models.IntegerField()
    password=models.CharField(max_length=50)
    confirm_password=models.CharField(max_length=50)
    role=models.CharField(max_length=50,choices=As_role,null=True)
    
    def __str__(self):
        return self.name
    
role=[
    ('Super_Admin','Super_Admin'),
    ('NGO_Admin','NGO_Admin'),
    ('User_admin','User_Admin'),
    ('Query_Admin','Query_Admin')
]


class AdminModel(models.Model):
    name=models.CharField(max_length=45 )
    email=models.EmailField()
    contact=models.IntegerField()
    password=models.CharField(max_length=50)
    confirm_password=models.CharField(max_length=50)
    role=models.CharField(max_length=50,choices=role,null=True)
    


