from django.db import models
from datetime import datetime,date

# Create your models here.
class Teacher_Credentials(models.Model):
    # id = models.AutoField(unique=True,blank=False,auto_created=True,primary_key=True)
    name = models.CharField(max_length=255,blank=False)
    emp_id = models.CharField(max_length=20,blank=False,default="Not Given")
    email = models.CharField(max_length=255,default='Not Given')
    phone = models.CharField(max_length=50,default='Not Given',blank=False)
    u_id = models.CharField(max_length=255,unique=True,blank=False,primary_key=True)
    password = models.CharField(max_length=255,default='1234')
    exp = models.CharField(max_length=255,blank=False,default='Advanced')
    budget = models.CharField(max_length=255,blank=False,default='0')
    meeting_length = models.Charfield(max_length=255,blank=False,default='0000') #[45,60,90,120]
    status = models.CharField(max_length=50,default='Active',auto_created=True,blank=False)


class Student_Credentials(models.Model):
    # id = models.AutoField(unique=True,blank=False,auto_created=True,primary_key=True)
    name = models.CharField(max_length=255,blank=False)
    student_id = models.CharField(max_length=20,blank=False,default="Not Given")
    email = models.CharField(max_length=255,default='Not Given')
    phone = models.CharField(max_length=50,default='Not Given',blank=False)
    u_id = models.CharField(max_length=255,unique=True,blank=False,primary_key=True)
    password = models.CharField(max_length=255,default='1234')
    status = models.CharField(max_length=50,default='Active',auto_created=True,blank=False)
