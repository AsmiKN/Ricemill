from django.db import models
from Administrator.models import tbl_unit,tbl_rawmaterial,tbl_supplier


# Create your models here.

class tbl_supplierraw(models.Model):
   supraw_rate=models.CharField(max_length=50)
   unit=models.ForeignKey(tbl_unit, on_delete=models.CASCADE)
   rawmaterial=models.ForeignKey(tbl_rawmaterial, on_delete=models.CASCADE)
   supplier=models.ForeignKey(tbl_supplier, on_delete=models.CASCADE) 

class tbl_sales(models.Model):
   date=models.CharField(max_length=50)
   quantity=models.CharField(max_length=50)
   amount=models.CharField(max_length=50)

   rawmaterial=models.ForeignKey(tbl_rawmaterial, on_delete=models.CASCADE)