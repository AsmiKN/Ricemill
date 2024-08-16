from django.shortcuts import render,redirect
from Administrator.models import *
from User.models import *
from Supplier.models import *
from Staff.models import *
from Guest.models import *
from datetime import date
from Customer.models import *
from django.db.models import Sum
import random
from datetime import datetime

# Create your views here.


def LoadingHomePage(request):
         return render(request,"Administrator/HomePage.html")

#district
def districtInsertSelect(request):
    data=tbl_district.objects.all()
    if request.method=="POST":
        disName=request.POST.get('txtdistrict')
        tbl_district.objects.create(district_name=disName)
        return render(request,"Administrator/District.html",{'data':data})
    else:
        return render(request,"Administrator/District.html",{"data":data})
def delDistrict(request,did):
        tbl_district.objects.get(id=did).delete()
        return redirect("Administrator:districtInsertSelect")


def districtupdate(request,eid):
    editdata=tbl_district.objects.get(id=eid)
    if request.method=="POST":
        editdata.district_name=request.POST.get("txtdistrict")
        editdata.save()
        return redirect("Administrator:districtInsertSelect")
    else:
        return render(request,"Administrator/District.html",{"editdata":editdata})


#category

def categoryInsertSelect(request):
    data=tbl_category.objects.all()
    if request.method=="POST":
        catName=request.POST.get('txtcategory')
        tbl_category.objects.create(category_name=catName)
        return render(request,"Administrator/Category.html",{'data':data})
    else:
        return render(request,"Administrator/Category.html",{'data':data})

def delcategory(request,cid):
    tbl_category.objects.get(id=cid).delete()
    return redirect("Administrator:categoryInsertSelect")

def updatecategory(request,eid):
    editdata=tbl_category.objects.get(id=eid)
    if request.method=="POST":
        editdata.category_name=request.POST.get("txtcategory")
        editdata.save()
        return redirect("Administrator:categoryInsertSelect")
    else:
        return render(request,"Administrator/Category.html",{"editdata":editdata})


#department

def departmentInsertSelect(request):
    data=tbl_department.objects.all()
    if request.method=="POST":
        departmentName=request.POST.get('txtdepartment')
        tbl_department.objects.create(department_name=departmentName)
        return render(request,"Administrator/Department.html",{'data':data})
    else:
        return render(request,"Administrator/Department.html",{'data':data})

def deldepartment(request,did):
    tbl_department.objects.get(id=did).delete()
    return redirect("Administrator:departmentInsertSelect")

def updatedepartment(request,eid):
    editdata=tbl_department.objects.get(id=eid)
    if request.method=="POST":
        editdata.department_name=request.POST.get("txtdepartment")
        editdata.save()
        return redirect("Administrator:departmentInsertSelect")
    else:
        return render(request,"Administrator/Department.html",{"editdata":editdata})



#designation

def designationInsertSelect(request):
    data=tbl_designation.objects.all()
    if request.method=="POST":
        desigName=request.POST.get('txtdesignation')
        tbl_designation.objects.create(designation_name=desigName)
        return render(request,"Administrator/Designation.html",{'data':data})
    else:
        return render(request,"Administrator/Designation.html",{'data':data})

def deldesignation(request,did):
    tbl_designation.objects.get(id=did).delete()
    return redirect("Administrator:designationInsertSelect")

def updatedesignation(request,eid):
    editdata=tbl_designation.objects.get(id=eid)
    if request.method=="POST":
        editdata.designation_name=request.POST.get("txtdesignation")
        editdata.save()
        return redirect("Administrator:designationInsertSelect")
    else:
        return render(request,"Administrator/Designation.html",{"editdata":editdata})

#place

def placeInsertSelect(request):
    district = tbl_district.objects.all()
    data=tbl_place.objects.all()
    if request.method=="POST":
        placeName=request.POST.get('txtname')
        dis = tbl_district.objects.get(id=request.POST.get('sel_district'))
        tbl_place.objects.create(place_name=placeName,district=dis)
        return render(request,"Administrator/Place.html",{'data':data})
    else:
        return render(request,"Administrator/Place.html",{'data':data,"districtdata":district})

def delPlace(request,did):
    tbl_place.objects.get(id=did).delete()
    return redirect("Administrator:placeInsertSelect")

def placeupdate(request,eid):
    district = tbl_district.objects.all()
    editdata=tbl_place.objects.get(id=eid)
    if request.method=="POST":
        editdata.place_name=request.POST.get("txtname")
        dis = tbl_district.objects.get(id=request.POST.get('sel_district'))
        editdata.district = dis
        editdata.save()
        return redirect("Administrator:placeInsertSelect")
    else:
        return render(request,"Administrator/Place.html",{"editdata":editdata,"districtdata":district})


def employeeInsertSelect(request):
    department = tbl_department.objects.all()
    designation=tbl_designation.objects.all()
    data=tbl_employee.objects.all()
    if request.method=="POST":
        employeeName=request.POST.get('txtname')
        employeeSalary=request.POST.get('txtsalary')
        employeecontact=request.POST.get('txtcontact')
        dep = tbl_department.objects.get(id=request.POST.get('sel_department'))
        dis = tbl_designation.objects.get(id=request.POST.get('sel_designation'))
        tbl_employee.objects.create(employee_name=employeeName,employee_salary=employeeSalary,employee_contact=employeecontact,department=dep,designation=dis)
        
        return render(request,"Administrator/Employee.html",{'data':data})
    else:
        return render(request,"Administrator/Employee.html",{'data':data,"departmentdata":department,"designationdata":designation})

def delemployee(request,eid):
    tbl_employee.objects.get(id=eid).delete()
    return redirect("Administrator:employeeInsertSelect")


def employeeupdate(request,eid):    
    department = tbl_department.objects.all()
    designation=tbl_designation.objects.all()
    editdata=tbl_employee.objects.get(id=eid)
    if request.method=="POST":
        editdata.employee_name=request.POST.get("txtname")
        editdata.employee_salary=request.POST.get("txtsalary")
        editdata.employee_contact=request.POST.get("txtcontact")
        dep = tbl_department.objects.get(id=request.POST.get('sel_department'))
        editdata.department = dep
        des = tbl_designation.objects.get(id=request.POST.get('sel_designation'))
        editdata.designation = des
        editdata.save()
        return redirect("Administrator:employeeInsertSelect")
    else:
        return render(request,"Administrator/Employee.html",{"editdata":editdata,"departmentdata":department,"designationdata":designation})






def courseInsertSelect(request):
    department = tbl_department.objects.all()
    data=tbl_course.objects.all()
    if request.method=="POST":
        courseName=request.POST.get('txtcourse')
        courseDuration=request.POST.get('txtduration')
        courseSemester=request.POST.get('txtsemester')
        dep = tbl_department.objects.get(id=request.POST.get('sel_department'))
        tbl_course.objects.create(course_name=courseName,course_duration=courseDuration,course_semester=courseSemester,department=dep)
        
        return render(request,"Administrator/Course.html",{'data':data})
    else:
            return render(request,"Administrator/Course.html",{'data':data,"departmentdata":department})

def delcourse(request,cid):
    tbl_course.objects.get(id=cid).delete()
    return redirect("Administrator:courseInsertSelect")


def courseupdate(request,cid):    
    department = tbl_department.objects.all()
    editdata=tbl_course.objects.get(id=cid)
    if request.method=="POST":
        editdata.course_name=request.POST.get("txtcourse")
        editdata.course_duration=request.POST.get("txtduration")
        editdata.course_semester=request.POST.get("txtsemester")
        dep = tbl_department.objects.get(id=request.POST.get('sel_department'))
        editdata.department = dep
        editdata.save()
        return redirect("Administrator:courseInsertSelect")
    else:
        return render(request,"Administrator/Course.html",{"editdata":editdata,"departmentdata":department})




def subjectInsertSelect(request):
    data=tbl_subject.objects.all()
    if request.method=="POST":
        subName=request.POST.get('txtname')
        tbl_subject.objects.create(subject_name=subName)
        return render(request,"Administrator/Subject.html",{'data':data})
    else:
        return render(request,"Administrator/Subject.html",{'data':data})

def delsubject(request,sid):
    tbl_subject.objects.get(id=sid).delete()
    return redirect("Administrator:subjectInsertSelect")


def subjectupdate(request,sid):
    editdata=tbl_subject.objects.get(id=sid)
    if request.method=="POST":
        editdata.subject_name=request.POST.get("txtname")
        editdata.save()
        return redirect("Administrator:subjectInsertSelect")
    else:
        return render(request,"Administrator/Subject.html",{"editdata":editdata})




def semesterInsertSelect(request):
    data=tbl_semester.objects.all()
    if request.method=="POST":
        semeName=request.POST.get('txtname')
        tbl_semester.objects.create(semester_name=semeName)
        return render(request,"Administrator/Semester.html",{'data':data})
    else:
        return render(request,"Administrator/Semester.html",{'data':data})

def delsemester(request,sid):
    tbl_semester.objects.get(id=sid).delete()
    return redirect("Administrator:semesterInsertSelect")


def semesterupdate(request,sid):
    editdata=tbl_semester.objects.get(id=sid)
    if request.method=="POST":
        editdata.semester_name=request.POST.get("txtname")
        editdata.save()
        return redirect("Administrator:semesterInsertSelect")
    else:
        return render(request,"Administrator/Semester.html",{"editdata":editdata})

def syllabusInsertSelect(request):
    course = tbl_course.objects.all()
    subject=tbl_subject.objects.all()
    semester=tbl_semester.objects.all()
    data=tbl_syllabus.objects.all()
    if request.method=="POST":
        cour = tbl_course.objects.get(id=request.POST.get('sel_course'))
        sub = tbl_subject.objects.get(id=request.POST.get('sel_subject'))
        sem=tbl_semester.objects.get(id=request.POST.get('sel_semester'))
        tbl_syllabus.objects.create(course=cour,subject=sub,semester=sem)
        
        return render(request,"Administrator/Syllabus.html",{'data':data})
    else:
        return render(request,"Administrator/Syllabus.html",{'data':data,"coursedata":course,"subjectdata":subject,"semesterdata":semester})


def delsyllabus(request,sid):
    tbl_syllabus.objects.get(id=sid).delete()
    return redirect("Administrator:syllabusInsertSelect")

def syllabusupdate(request,sid):    
    course = tbl_course.objects.all()
    subject=tbl_subject.objects.all()
    semester=tbl_semester.objects.all()
    editdata=tbl_syllabus.objects.get(id=sid)
    if request.method=="POST":
        cour = tbl_course.objects.get(id=request.POST.get('sel_course'))
        editdata.course = cour
        sub = tbl_subject.objects.get(id=request.POST.get('sel_subject'))
        editdata.subject = sub
        sem= tbl_semester.objects.get(id=request.POST.get('sel_semester'))
        editdata.semester = sem
        editdata.save()
        return redirect("Administrator:syllabusInsertSelect")
    else:
        return render(request,"Administrator/Syllabus.html",{"editdata":editdata,"coursedata":course,"subjectdata":subject,"semesterdata":semester})

def AdminInsertSelect(request):
    data = tbl_admin.objects.all()
    if request.method=="POST":
        admin_Name=request.POST.get('txtname')
        admin_Email=request.POST.get('txtemail')
        admin_Phone=request.POST.get('txtphone')
        admin_Password=request.POST.get('txtpassword')
        tbl_admin.objects.create(admin_name=admin_Name,admin_email=admin_Email,admin_phone=admin_Phone,admin_photo=request.FILES.get("fileImage"),admin_password=admin_Password)
        return render(request,"Administrator/Admin.html",{'data':data})
    else:
        return render(request,"Administrator/Admin.html",{'data':data})

def delAdmin(request,aid):
    tbl_admin.objects.get(id=aid).delete()
    return redirect("Administrator:AdminInsertSelect")

def Adminupdate(request,aid):
    editdata=tbl_admin.objects.get(id=aid)
    if request.method=="POST":
        editdata.admin_name=request.POST.get("txtname")
        editdata.admin_email=request.POST.get("txtemail")
        editdata.admin_password=request.POST.get("txtpassword")
        editdata.admin_address=request.POST.get("txtaddress")
        editdata.save()
        return redirect("Administrator:AdminInsertSelect")
    else:
        return render(request,"Administrator/Admin.html",{"editdata":editdata})



def newuserlist(request):
    data=tbl_newuser.objects.all()
    return render(request,"Administrator/Newuserlist.html",{'data':data})   



def subcategoryInsertSelect(request):
    category=tbl_category.objects.all()
    data=tbl_subcategory.objects.all()
    if request.method=="POST":
        subcategoryName=request.POST.get('txtname')
        cat = tbl_category.objects.get(id=request.POST.get('sel_category'))
        tbl_subcategory.objects.create(subcategory_name=subcategoryName,category=cat)
        return render(request,"Administrator/Subcategory.html",{'data':data})
    else:
        return render(request,"Administrator/Subcategory.html",{'data':data,"categorydata":category})

def delsubcategory(request,sid):
    tbl_subcategory.objects.get(id=sid).delete()
    return redirect("Administrator:subcategoryInsertSelect")

def subcategoryupdate(request,sid):
    category = tbl_category.objects.all()
    editdata=tbl_subcategory.objects.get(id=sid)
    if request.method=="POST":
        editdata.subcategory_name=request.POST.get("txtname")
        cat = tbl_category.objects.get(id=request.POST.get('sel_category'))
        editdata.subcategory = cat
        editdata.save()
        return redirect("Administrator:productInsertSelect")
    else:
        return render(request,"Administrator/product.html",{"editdata":editdata,"subcategorydata":subcategory})



def productInsertSelect(request):
    category= tbl_category.objects.all()
    subcategory= tbl_subcategory.objects.all()
    data = tbl_product.objects.all()
    if request.method=="POST":
        product_Name=request.POST.get('txtproduct')
        product_Price=request.POST.get('txtprice')
        product_Details=request.POST.get('txtdetails')
        sub = tbl_subcategory.objects.get(id=request.POST.get('sel_subcategory'))
        tbl_product.objects.create(product_name=product_Name,product_price=product_Price,product_details=product_Details,subcategory=sub,product_photo=request.FILES.get("fileImage"))
        return render(request,"Administrator/Product.html",{'data':data})
    else:
        return render(request,"Administrator/Product.html",{"categorydata":category})

def ajaxsubcategory(request):
    cat = tbl_category.objects.get(id=request.GET.get("did"))
    subcategory= tbl_subcategory.objects.filter(category=cat)
    return render(request,"Administrator/AjaxSubcategory.html",{"subcategory":subcategory})



def galleryInsertSelect(request):
    data=tbl_gallery.objects.all()
    category = tbl_category.objects.all()
    if request.method=="POST":
        desc=request.POST.get('txtdesc')
        subcategory=tbl_subcategory.objects.get(id=request.POST.get('sel_subcategory'))
        product=tbl_product.objects.get(id=request.POST.get('sel_product'))
        tbl_gallery.objects.create(gallery_description=desc,gallery_photo=request.FILES.get("fileImage"),product_name=product)
        return render(request,"Administrator/Gallery.html",{'categorydata':category,'data':data})
    else:
        return render(request,"Administrator/Gallery.html",{'categorydata':category,'data':data})



def ajaxproduct(request):
    subcategory = tbl_subcategory.objects.get(id=request.GET.get("did"))
    product = tbl_product.objects.filter(subcategory=subcategory)
    return render(request,"Administrator/Ajaxproduct.html",{"product":product})


      
    

# def ComplaintListNew(request):

#     userdata=tbl_customer.objects.all()
#     userComplaint=tbl_complaint.objects.filter(complaint_status=0,user__in=userdata)

#     freedata=tbl_freelancer.objects.all()
#     freeComplaint=tbl_complaint.objects.filter(complaint_status=0,freelancer__in=freedata)

#     instdata=tbl_institute.objects.all()
#     instComplaint=tbl_complaint.objects.filter(complaint_status=0,inst__in=instdata)

#     return render(request,"Administrator/ComplaintListNew.html",{'userComplaint':userComplaint,'freeComplaint':freeComplaint,'instComplaint':instComplaint})

def ComplaintReply(request,cid):
    complaint = tbl_complaint.objects.get(id=cid)
    if request.method=="POST":
        complaint.complaint_replydate = date.today()
        complaint.complaint_reply=request.POST.get('txtreply')
        complaint.complaint_status=1
        complaint.save()
        return redirect("Administrator:LoadingHomePage")
    else:
        return render(request,"Administrator/ComplaintListReply.html",{'complaint':complaint})

    
def ComplaintSolved(request):
    userdata=tbl_newuser.objects.all()
    userComplaint=tbl_complaint.objects.filter(complaint_status=1,user__in=userdata)
    freedata=tbl_freelancer.objects.all()
    freeComplaint=tbl_complaint.objects.filter(complaint_status=1,freelancer__in=freedata)
    instdata=tbl_institute.objects.all()
    instComplaint=tbl_complaint.objects.filter(complaint_status=1,inst__in=instdata)
    return render(request,"Administrator/ComplaintListSolved.html",{'userComplaint':userComplaint,'freeComplaint':freeComplaint,'instComplaint':instComplaint})   
       
def complaintSelect(request):
    userdata=tbl_customer.objects.all()
    data=tbl_complaint.objects.filter(complaint_status=0,user__in=userdata)
    return render(request,"Administrator/NewComplaint.html",{'data':data})
    

def complaintreplayInsert(request,cid):
    complaint = tbl_complaint.objects.get(id=cid)
    if request.method=="POST":
        complaint.complaint_replydate = date.today()
        complaint.complaint_reply=request.POST.get('txtreply')
        complaint.complaint_status=1
        complaint.save()
        return redirect("Administrator:complaintSelect")
    else:
        return render(request,"Administrator/ComplaintReply.html",{'complaint':complaint})

def complaintsolvedSelect(request):
    userdata=tbl_customer.objects.all()
    data=tbl_complaint.objects.filter(complaint_status=1,user__in=userdata)
    return render(request,"Administrator/SolvedComplaints.html",{'data':data})

def feedbackSelect(request):
    data=tbl_feedback.objects.all()
    return render(request,"Administrator/FeedbackView.html",{'data':data})

def feedbackDelete(request,cid):
    tbl_feedback.objects.get(id=cid).delete()
    return redirect("Administrator:feedbackSelect")










def roleInsertSelect(request):
    data=tbl_role.objects.all()
    if request.method=="POST":
        roleName=request.POST.get('txtname')
        tbl_role.objects.create(role_name=roleName)
        return render(request,"Administrator/role.html",{'data':data})
    else:
        return render(request,"Administrator/role.html",{'data':data})

def delrole(request,rid):
    tbl_role.objects.get(id=rid).delete()
    return redirect("Administrator:roleInsertSelect")

def updaterole(request,rid):
    editdata=tbl_role.objects.get(id=rid)
    if request.method=="POST":
        editdata.role_name=request.POST.get("txtname")
        editdata.save()
        return redirect("Administrator:roleInsertSelect")
    else:
        return render(request,"Administrator/Role.html",{"editdata":editdata})

def staffInsertSelect(request):
    data=tbl_staff.objects.all()
    role=tbl_role.objects.all()
    if request.method=="POST":
        name=request.POST.get('txtname')
        address=request.POST.get('txtaddress')
        email=request.POST.get('txtemail')
        doj=request.POST.get('txtdoj')
        phone=request.POST.get('txtphone')
        password=request.POST.get('txtpassword')
        st = tbl_role.objects.get(id=request.POST.get('sel_role'))
        tbl_staff.objects.create(staff_name=name,staff_address=address,staff_email=email,staff_doj=doj,staff_phone=phone,staff_password=password,staff_photo=request.FILES.get("fileImage"),staff_proof=request.FILES.get("fileImg"),role=st)
        return redirect("Administrator:staffInsertSelect")
    else:
        return render(request,"Administrator/Staff.html",{'data':data,"role":role})

def delstaff(request,sid):
    tbl_staff.objects.get(id=sid).delete()
    return redirect("Administrator:staffInsertSelect")   

def staffupdate(request,sid):
    role=tbl_role.objects.all()
    editdata=tbl_staff.objects.get(id=sid)
    if request.method=="POST":
        editdata.staff_name=request.POST.get("txtname")
        editdata.staff_address=request.POST.get("txtaddress")
        editdata.staff_email=request.POST.get("txtemail")
        editdata.staff_dob=request.POST.get("txtdoj")
        editdata.staff_phone=request.POST.get("txtphone")
        editdata.staff_password=request.POST.get("txtpassword")
        editdata.save()
        return redirect("Administrator:staffInsertSelect")
    else:
        return render(request,"Administrator/Staff.html",{"editdata":editdata,"role":role})


def Dashboard(request):
     return render(request,"Administrator/Admin_dashboard.html")


def rawmaterialInsertSelect(request):
    data=tbl_rawmaterial.objects.all()
    if request.method=="POST":
        rawName=request.POST.get('txtname')
        tbl_rawmaterial.objects.create(rawmaterial=rawName)
        return render(request,"Administrator/Rawmaterial.html",{'data':data})
    else:
        return render(request,"Administrator/Rawmaterial.html",{'data':data})

def delrawmaterial(request,rid):
    tbl_rawmaterial.objects.get(id=rid).delete()
    return redirect("Administrator:rawmaterialInsertSelect")

def rawmaterialupdate(request,rid):
    editdata=tbl_rawmaterial.objects.get(id=rid)
    if request.method=="POST":
        editdata.rawmaterial=request.POST.get("txtname")
        editdata.save()
        return redirect("Administrator:rawmaterialInsertSelect")
    else:
        return render(request,"Administrator/Rawmaterial.html",{"editdata":editdata})


def unitInsertSelect(request):
    data=tbl_unit.objects.all()
    if request.method=="POST":
        unitName=request.POST.get('txtname')
        tbl_unit.objects.create(unit=unitName)
        return render(request,"Administrator/Unit.html",{'data':data})
    else:
        return render(request,"Administrator/Unit.html",{'data':data})

def delunit(request,uid):
    tbl_unit.objects.get(id=uid).delete()
    return redirect("Administrator:unitInsertSelect")

def unitupdate(request,uid):
    editdata=tbl_unit.objects.get(id=uid)
    if request.method=="POST":
        editdata.unit_name=request.POST.get("txtname")
        editdata.save()
        return redirect("Administrator:unitInsertSelect")
    else:
        return render(request,"Administrator/Unit.html",{"editdata":editdata})


def newproductInsertSelect(request):
    data=tbl_newproduct.objects.all()
    cat=tbl_category.objects.all()
    uni=tbl_unit.objects.all()
    for product in data:
        total_stock = tbl_stock.objects.filter(product=product).aggregate(total=Sum('stock_quantity'))['total']
        total_cart = tbl_pcart.objects.filter(product=product.id,cart_status=1).aggregate(total=Sum('cart_qty'))['total']
        print(total_stock,"stock")
        print(total_cart,"cart")
        if total_stock is None:
            total_stock = 0
        if total_cart is None:
            total_cart = 0
        if isinstance(total_stock, int):
            total_stock = total_stock
        else:
            total_stock = 0     
            if isinstance(total_cart, int):
                total_cart = total_cart
            else:
                total_cart = 0
        total=  total_stock-total_cart
        print(total)
        product.total_stock=total
    if request.method=="POST":
        name=request.POST.get('txtproduct')
        price=request.POST.get('txtprice')
        details=request.POST.get('txtdetails')
        stock=request.POST.get('txtstock')
        uni = tbl_unit.objects.get(id=request.POST.get('sel_unit'))
        cat = tbl_category.objects.get(id=request.POST.get('sel_category'))
        tbl_newproduct.objects.create(newproduct_name=name,newproduct_price=price,newproduct_details=details,newproduct_stock=stock,newproduct_photo=request.FILES.get("fileImage"),unit=uni,category=cat)
        return redirect("Administrator:newproductInsertSelect")
    else:
        return render(request,"Administrator/Newproduct.html",{'data':data,"categorydata":cat,"unitdata":uni})

def delnewproduct(request,pid):
    tbl_newproduct.objects.get(id=pid).delete()
    return redirect("Administrator:newproductInsertSelect")   

def newproductupdate(request,pid):
    category=tbl_category.objects.all()
    unit=tbl_unit.objects.all()
    editdata=tbl_newproduct.objects.get(id=pid)
    if request.method=="POST":
        editdata.newproduct_name=request.POST.get("txtproduct")
        editdata.newproduct_price=request.POST.get("txtprice")
        editdata.newproduct_details=request.POST.get("txtdetails")
        editdata.newproduct_stock=request.POST.get("txtstock")
        editdata.save()
        return redirect("Administrator:newproductInsertSelect")
    else:
        return render(request,"Administrator/Newproduct.html",{"editdata":editdata,"categorydata":category,"unitdata":unit})


def suppliersInsertSelect(request): 
  
    pla=tbl_place.objects.all()  
    data=tbl_supplier.objects.all()
    if request.method=="POST":
        supName=request.POST.get('txtname')
        supCon=request.POST.get('txtcontact')
        supEma=request.POST.get('txtemail')
        supAdd=request.POST.get('txtaddress')
        supGst=request.POST.get('txtgst')
        suppass=request.POST.get('txtpassword')
        pla = tbl_place.objects.get(id=request.POST.get('sel_place'))
        tbl_supplier.objects.create(supplier_name=supName,supplier_contact=supCon,supplier_email=supEma,supplier_address=supAdd,supplier_gstno=supGst,supplier_password=suppass,place=pla)
        return render(request,"Administrator/Supplier.html",{'data':data})
    else:
        return render(request,"Administrator/Supplier.html",{'data':data,"placedata":pla})

def delsupplier(request,vid):
    tbl_supplier.objects.get(id=vid).delete()
    return redirect("Administrator:suppliersInsertSelect")

def updatesupplier(request,vid):
    pla=tbl_place.objects.all()
    editdata=tbl_supplier.objects.get(id=vid)
    if request.method=="POST":
        editdata.supplier_name=request.POST.get("txtname")
        editdata.supplier_contact=request.POST.get("txtcontact")
        editdata.supplier_email=request.POST.get("txtemail")
        editdata.supplier_address=request.POST.get("txtaddress")
        editdata.supplier_password=request.POST.get("txtpassword")
        editdata.supplier_gstno=request.POST.get("txtgst")
        editdata.save()
        return redirect("Administrator:suppliersInsertSelect")
    else:
        return render(request,"Administrator/Supplier.html",{"editdata":editdata,"placedata":pla})

def rawmaterialconsInsertSelect(request):
    data=tbl_rawmaterialcons.objects.all()
    rawmaterial=tbl_rawmaterial.objects.all()
    uni=tbl_unit.objects.all()
    if request.method=="POST":
        date=request.POST.get('txtdate')
        qty=request.POST.get('txtqty')
        uni = tbl_unit.objects.get(id=request.POST.get('sel_unit'))
        rawmaterial = tbl_rawmaterial.objects.get(id=request.POST.get('sel_rawmaterial'))
        tbl_rawmaterialcons.objects.create(rawcons_date=date,rawcons_qty=qty,unit=uni,rawmaterial=rawmaterial)
        return redirect("Administrator:rawmaterialconsInsertSelect")
    else:
        return render(request,"Administrator/Rawmaterial_con.html",{'data':data,"rawmaterialdata":rawmaterial,"unitdata":uni})

def delrawmaterialcons(request,vid):
    tbl_rawmaterialcons.objects.get(id=vid).delete()
    return redirect("Administrator:rawmaterialconsInsertSelect")   

def rawmaterialconsupdate(request,vid):
    rawmaterial=tbl_rawmaterial.objects.all()
    unit=tbl_unit.objects.all()
    editdata=tbl_rawmaterialcons.objects.get(id=vid)
    if request.method=="POST":
        editdata.rawcons_qty=request.POST.get("txtqty")
        editdata.rawcons_date=request.POST.get("txtdate")
        
        editdata.save()
        return redirect("Administrator:rawmaterialconsInsertSelect")
    else:
        return render(request,"Administrator/Rawmaterial_con.html",{"editdata":editdata,"rawmaterialdata":rawmaterial,"unitdata":unit})



def productionInsertSelect(request):
    data=tbl_production.objects.all()
    product=tbl_newproduct.objects.all()
    uni=tbl_unit.objects.all()
    if request.method=="POST":
        date=request.POST.get('txtdate')
        qty=request.POST.get('txtqty')
       
        uni = tbl_unit.objects.get(id=request.POST.get('sel_unit'))
        product = tbl_newproduct.objects.get(id=request.POST.get('sel_newproduct_name'))
        tbl_production.objects.create(production_date=date,production_qty=qty,unit=uni,newproduct_name=product)
        return redirect("Administrator:productionInsertSelect")
    else:
        return render(request,"Administrator/Production.html",{'data':data,"productdata":product,"unitdata":uni})

def delproduction(request,pid):
    tbl_production.objects.get(id=pid).delete()
    return redirect("Administrator:productionInsertSelect")   

def updateproduction(request,pid):
    product=tbl_newproduct.objects.all()
    unit=tbl_unit.objects.all()
    editdata=tbl_production.objects.get(id=pid)
    if request.method=="POST":
        editdata.production_date=request.POST.get("txtdate")
        editdata.production_qty=request.POST.get("txtqty")
       
        editdata.save()
        return redirect("Administrator:productionInsertSelect")
    else:
        return render(request,"Administrator/Production.html",{"editdata":editdata,"productdata":product,"unitdata":unit})



#Admin login
def homepage(request):
    return render(request,"Administrator/Homepage.html")

def my_pro(request):
    data=tbl_admin.objects.get(id=request.session["aid"])
    return render(request,"Administrator/Myprofile.html",{'data':data})

def editprofile(request):
    prodata=tbl_admin.objects.get(id=request.session["aid"])
    if request.method=="POST":
        prodata.admin_name=request.POST.get('txtname')
        prodata.admin_phone=request.POST.get('txtphone')
        prodata.admin_email=request.POST.get('txtemail')
        prodata.save()
        return render(request,"Administrator/Editprofile.html",{'msg':"Profile Updated"})
    else:
        return render(request,"Administrator/Editprofile.html",{'prodata':prodata})

def changepassword(request):
    if request.method=="POST":
        ccount=tbl_admin.objects.filter(id=request.session["aid"],admin_password=request.POST.get('txtcurpass')).count()
        if ccount>0:
            if request.POST.get('txtnewpass')==request.POST.get('txtconpass'):
                admindata=tbl_admin.objects.get(id=request.session["aid"],admin_password=request.POST.get('txtcurpass'))
                admindata.admin_password=request.POST.get('txtnewpass')
                admindata.save()
                return render(request,"Administrator/ChangePassword.html",{'msg':"Password Updated"})
            else:
                return render(request,"Administrator/ChangePassword.html",{'msg1':"Error in confirm Password"})
        else:
            return render(request,"Administrator/ChangePassword.html",{'msg1':"Error in current password"})
    else:
        return render(request,"Administrator/ChangePassword.html")

 


#admin add/dlt supplier




def supplierrawmaterial(request):
    data=tbl_supplierraw.objects.all()
    return render(request,"Administrator/Viewsupplierrawmateril.html",{'data':data})   


def supplierdetails(request):
    data=tbl_supplier.objects.all()
    return render(request,"Administrator/Viewsupplierdetails.html",{'data':data})  


def addstock(request,did):
    product =  tbl_newproduct.objects.get(id=did)
    stock_entry = tbl_stock.objects.filter(product=product).first()
    data = tbl_stock.objects.all()
    if request.method == "POST":
        date = request.POST.get('txtdate')
        stock_quantity = request.POST.get("txtstock")
        tbl_stock.objects.create(stock_date=date,stock_quantity=stock_quantity,product=product)

        return render(request, "Administrator/AddStock.html", {'data': data})
    else:
        return render(request, "Administrator/AddStock.html", {'data': data, "productdata": product})


def delstock(request,did):
    tbl_stock.objects.get(id=did).delete()
    return redirect("Administrator:newproductInsertSelect")





def details(request,did):
    #booking=tbl_productbooking.objects.get(id=did)
    data=tbl_pcart.objects.filter(booking=did)
    print(data)
    return render(request,"Administrator/Viewpurchasedetails.html",{"Data":data})


def vieworder(request):
    data=tbl_productbooking.objects.all()
    return render(request,"Administrator/Vieworder.html",{"Data":data,})

def updateproductbooking(request,bid):
    item = tbl_pcart.objects.get(id=bid)
    if item.ship_status == 0:
        item.ship_status = 1  
    if item.ship_status == 1:
        item.ship_status = 2  
    elif item.ship_status == 2:
        item.ship_status = 3
    elif item.ship_status == 3:
        item.ship_status = 4
    elif item.ship_status == 4:
        item.ship_status = 5  
    item.save()  
    return redirect("Administrator:vieworder")


def logout(request):
    del request.session["aid"]
    return redirect("Guest:Logininsertselect")



def viewcustomer(request):
    data=tbl_customer.objects.all()
    return render(request,"Administrator/Viewcustomer.html",{'data':data})  

def adminsreport(request):
    
    if request.method=="POST":
        # data=tbl_pcart.objects.all()
        fromdate=request.POST.get('txtfdate')
        todate=request.POST.get('txtdate')
        data=tbl_pcart.objects.filter(booking__booking_date__gte=fromdate,booking__booking_date__lte=todate)
        bill = []
        for i in data:
            bill.append(random.randint(10000,99999))
        datas = zip(data,bill)
        return render(request,"Administrator/Reports.html",{'data':datas})
    else:
        return render(request,"Administrator/Reports.html") 