from django.db import models

# Create your models here.
class SuperAdminModel(models.Model):
    name=models.CharField(max_length=45)
    email=models.EmailField()
    contact=models.IntegerField()
    password=models.CharField(max_length=50)
    confirm_password=models.CharField(max_length=50)
    

    def __str__(self):
        return self.name,self.email,self.contact,self.password,self.confirm_password
