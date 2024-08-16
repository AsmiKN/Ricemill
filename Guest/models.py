from django.db import models
from Administrator.models import *

#Create your models here.
class tbl_newuser(models.Model):
    newuser_name=models.CharField(max_length=150)
    newuser_gender=models.CharField(max_length=150)
    newuser_contact=models.CharField(max_length=100)
    newuser_email=models.CharField(max_length=100)
    newuser_password=models.CharField(max_length=100)
    newuser_address=models.CharField(max_length=100)
    place= models.ForeignKey(tbl_place, on_delete=models.CASCADE)
    newuser_photo = models.FileField(upload_to='Assets/UserPhoto/')
    newuser_proof = models.FileField(upload_to='Assets/UserProof/')
    newuser_status = models.IntegerField(default="0")

class tbl_customer(models.Model):
    customer_name=models.CharField(max_length=150)
    customer_gender=models.CharField(max_length=150)
    customer_email=models.CharField(max_length=150)
    customer_phone=models.CharField(max_length=100)
    customer_address=models.CharField(max_length=100)
    customer_password=models.CharField(max_length=100)
    place=models.ForeignKey(tbl_place, on_delete=models.CASCADE)
    customer_photo = models.FileField(upload_to='Assets/UserPhoto/')
    customer_proof = models.FileField(upload_to='Assets/UserProof/')

class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
   