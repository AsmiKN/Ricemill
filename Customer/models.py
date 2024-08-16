from django.db import models
from Guest.models import *
from Administrator.models import *
from Customer.models import *



#Create your models here.
class tbl_productbooking(models.Model):
    customer = models.ForeignKey(tbl_customer, on_delete=models.CASCADE)
    booking_date=models.DateField(auto_now_add=True)
    booking_status = models.IntegerField(default="0")
    price = models.CharField(default="0",max_length=40)

class tbl_pcart(models.Model):   
    booking = models.ForeignKey(tbl_productbooking, on_delete=models.CASCADE)
    product=models.ForeignKey(tbl_newproduct, on_delete=models.CASCADE)
    cart_qty= models.CharField(max_length=500)
    cart_status=models.IntegerField(default="0")
    ship_status=models.IntegerField(default="0")

class tbl_complaint(models.Model):
    complaint_title=models.CharField(max_length=500)
    complaint_details=models.CharField(max_length=500)
    complaint_postdate=models.DateField(auto_now_add=True)
    complaint_reply=models.CharField(max_length=500)
    complaint_replydate=models.DateField(null=True)
    complaint_status = models.IntegerField(default="0")
    user = models.ForeignKey(tbl_customer, on_delete=models.CASCADE,null=True)

class tbl_feedback(models.Model):
    feedback_subject=models.CharField(max_length=500)
    feedback_details=models.CharField(max_length=500)
    feedback_postdate=models.DateField(auto_now_add=True)
    feedback_status = models.IntegerField(default="0")
    user = models.ForeignKey(tbl_customer, on_delete=models.CASCADE)


