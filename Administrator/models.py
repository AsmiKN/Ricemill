from django.db import models




# Create your models here.
class tbl_district(models.Model):
   district_name=models.CharField(max_length=150)

class tbl_admin(models.Model):
    admin_name=models.CharField(max_length=50)
    admin_email=models.CharField(max_length=50)
    admin_phone=models.CharField(max_length=50)
    admin_password=models.CharField(max_length=50)
    admin_photo = models.FileField(upload_to='Assets/UserPhoto/')

class tbl_category(models.Model):
    category_name=models.CharField(max_length=50)


class tbl_department(models.Model):
    department_name=models.CharField(max_length=50)

class tbl_designation(models.Model):
    designation_name=models.CharField(max_length=50)




class tbl_place(models.Model):
   place_name=models.CharField(max_length=50)
   district = models.ForeignKey(tbl_district, on_delete=models.CASCADE)


#bringing department,designation to employee table  
class tbl_employee(models.Model):
   employee_name=models.CharField(max_length=50)
   employee_contact=models.CharField(max_length=50)
   employee_salary=models.CharField(max_length=50)
   department= models.ForeignKey(tbl_department, on_delete=models.CASCADE)
   designation=models.ForeignKey(tbl_designation, on_delete=models.CASCADE)

#bringing departmet to course table
class tbl_course(models.Model):
   course_name=models.CharField(max_length=50)
   course_duration=models.CharField(max_length=50)
   course_semester=models.CharField(max_length=50)
   department=models.ForeignKey(tbl_department, on_delete=models.CASCADE)


class tbl_subject(models.Model):
   subject_name=models.CharField(max_length=50)



class tbl_semester(models.Model):
   semester_name=models.CharField(max_length=50)


class tbl_syllabus(models.Model):
   course= models.ForeignKey(tbl_course, on_delete=models.CASCADE)
   subject=models.ForeignKey(tbl_subject, on_delete=models.CASCADE)
   semester=models.ForeignKey(tbl_semester, on_delete=models.CASCADE)


class tbl_subcategory(models.Model):
   category= models.ForeignKey(tbl_category, on_delete=models.CASCADE)
   subcategory_name=models.CharField(max_length=50)
 
class tbl_product(models.Model):
   product_name=models.CharField(max_length=50)
   product_price=models.CharField(max_length=50)
   product_details=models.CharField(max_length=50)
   subcategory=models.ForeignKey(tbl_subcategory, on_delete=models.CASCADE)
   product_photo = models.FileField(upload_to='Assets/UserPhoto/')
   product_status = models.IntegerField(default="0")

class tbl_gallery(models.Model):
   gallery_description=models.CharField(max_length=50)
   product_name=models.ForeignKey(tbl_product, on_delete=models.CASCADE)
   gallery_photo = models.FileField(upload_to='Assets/UserPhoto/')
   gallery_status = models.IntegerField(default="0")

class tbl_supplier(models.Model):
   supplier_name=models.CharField(max_length=50)
   supplier_contact=models.CharField(max_length=50)
   supplier_email=models.CharField(max_length=50)
   supplier_address=models.CharField(max_length=50)
   supplier_gstno=models.CharField(max_length=50)
   supplier_password=models.CharField(max_length=50)
   place= models.ForeignKey(tbl_place, on_delete=models.CASCADE)
 

class tbl_role(models.Model):
   role_id=models.CharField(max_length=50)
   role_name=models.CharField(max_length=50)


class tbl_staff(models.Model):
   staff_id=models.CharField(max_length=50)
   staff_name=models.CharField(max_length=50)
   staff_phone=models.CharField(max_length=50)
   staff_email=models.CharField(max_length=50)
   staff_address=models.CharField(max_length=50) 
   staff_doj=models.CharField(max_length=50)
   staff_password=models.CharField(max_length=50)
   staff_photo = models.FileField(upload_to='Assets/staffphoto/')
   role = models.ForeignKey(tbl_role, on_delete=models.CASCADE)
   staff_proof = models.FileField(upload_to='Assets/staffproof/')

class tbl_unit(models.Model):
   unit=models.CharField(max_length=150)





class tbl_rawmaterial(models.Model):
   rawmaterial=models.CharField(max_length=150)  

class tbl_newproduct(models.Model):
   unit=models.ForeignKey(tbl_unit, on_delete=models.CASCADE)
   category=models.ForeignKey(tbl_category, on_delete=models.CASCADE)
   newproduct_name=models.CharField(max_length=50)
   newproduct_price=models.CharField(max_length=50)
   newproduct_details=models.CharField(max_length=50)
   newproduct_stock=models.CharField(max_length=50)
   newproduct_photo = models.FileField(upload_to='Assets/UserPhoto/')
   newproduct_status = models.IntegerField(default="0")

class tbl_rawmaterialcons(models.Model):
   rawmaterial= models.ForeignKey(tbl_rawmaterial, on_delete=models.CASCADE)
   unit=models.ForeignKey(tbl_unit, on_delete=models.CASCADE)
   rawcons_qty=models.CharField(max_length=50)
   rawcons_date=models.CharField(max_length=50)

class tbl_production(models.Model):
   production_date= models.CharField(max_length=50)
   production_qty=models.CharField(max_length=50)
   unit=models.ForeignKey(tbl_unit, on_delete=models.CASCADE)
   newproduct_name=models.ForeignKey(tbl_newproduct, on_delete=models.CASCADE)
   
class tbl_stock(models.Model):
   stock_quantity=models.IntegerField()
   product = models.ForeignKey(tbl_newproduct, on_delete=models.CASCADE)
   stock_date=models.DateField(null=True)  




   