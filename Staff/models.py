from django.db import models
from Administrator.models import tbl_staff,tbl_newproduct
from Supplier.models import *
# # Create your models here.
class tbl_rawmaterialbooking(models.Model):
    staff = models.ForeignKey(tbl_staff, on_delete=models.CASCADE)
    booking_date=models.DateField(auto_now_add=True)
    booking_status = models.IntegerField(default="0")
    price = models.CharField(default="0",max_length=40)

class tbl_cart(models.Model):   
    booking = models.ForeignKey(tbl_rawmaterialbooking, on_delete=models.CASCADE)
    product=models.ForeignKey(tbl_supplierraw, on_delete=models.CASCADE)
    cart_qty= models.CharField(max_length=500)
    cart_status=models.IntegerField(default="0")

# class tbl_purchase(models.Model):
#    date=models.CharField(max_length=50)
#    quantity=models.CharField(max_length=50)
#    amount=models.CharField(max_length=50)
#    supplier_name= models.ForeignKey(tbl_supplier, on_delete=models.CASCADE)
#    rawmaterial=models.ForeignKey(tbl_rawmaterial, on_delete=models.CASCADE)