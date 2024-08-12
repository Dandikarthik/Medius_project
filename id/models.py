from django.db import models
from datetime import datetime
# models.py
from django.db import models

# class Employee(models.Model):
#     file = models.FileField(upload_to='xlsx_files/')
# Create your models here.

class Employee(models.Model):
    
    Date = models.CharField(max_length=50)
    ACCNO = models.CharField(max_length=12) 
    CustState = models.CharField(max_length=150)
    custpin = models.CharField(max_length=6)
    DPD = models.CharField(max_length=100)
    
    
    
    
    
    
    
    