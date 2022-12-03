from django.db import models

# Create your models here.
class Regmodel(models.Model):
    eid=models.IntegerField(primary_key=True)
    name=models.CharField(max_length=120)
    age=models.IntegerField()
    email=models.EmailField(unique=True)
    experience=models.IntegerField()

    def __str__(self):
        return self.name

class Persons(models.Model):
    firstname=models.CharField(max_length=100)
    secondname=models.CharField(max_length=100)

class Department(models.Model):
    DeptNo=models.IntegerField()
    DeptName=models.CharField(max_length=100) 
    DeptDescription=models.CharField(max_length=120)    

    
class Manager(models.Model):
    first_name=models.CharField(max_length=120)
    last_name=models.CharField(max_length=120)
    email=models.EmailField()
    phone=models.IntegerField()
    pic=models.ImageField(upload_to='profilepic',null=True)
