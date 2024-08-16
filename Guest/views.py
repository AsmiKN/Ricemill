from django.shortcuts import render,redirect
from Administrator.models import *
from Guest.models import *
# Create your views here.

def userInsertSelect(request):
    district= tbl_district.objects.all()
    data = tbl_newuser.objects.all()
    if request.method=="POST":
        user_Name=request.POST.get('txtname')
        user_Gender=request.POST.get('gender')
        user_Contact=request.POST.get('txtcontact')
        user_Email=request.POST.get('txtemail')
        user_Password=request.POST.get('txtpassword')
        user_Address=request.POST.get('txtaddress')
        pe = tbl_place.objects.get(id=request.POST.get('sel_place'))
        tbl_newuser.objects.create(newuser_name=user_Name,newuser_gender=user_Gender,newuser_contact=user_Contact,newuser_email=user_Email,newuser_password=user_Password,newuser_address=user_Address,place=pe,newuser_photo=request.FILES.get("fileImage"),newuser_proof=request.FILES.get("fileProof"))
        return render(request,"Guest/Newuser.html",{'data':data})
    else:
        return render(request,"Guest/Newuser.html",{"districtdata":district})

def ajaxplace(request):
    dis = tbl_district.objects.get(id=request.GET.get("did"))
    place = tbl_place.objects.filter(district=dis)
    return render(request,"Guest/AjaxPlace.html",{"place":place})


def Logininsertselect(request):
    if request.method == "POST":
        admincount = tbl_admin.objects.filter(admin_email=request.POST.get("txtemail"),admin_password=request.POST.get("txtpassword")).count()
        staffcount = tbl_staff.objects.filter(staff_email=request.POST.get("txtemail"),staff_password=request.POST.get("txtpassword")).count()
        customercount = tbl_customer.objects.filter(customer_email=request.POST.get("txtemail"),customer_password=request.POST.get("txtpassword")).count()
        suppliercount = tbl_supplier.objects.filter(supplier_email=request.POST.get("txtemail"),supplier_password=request.POST.get("txtpassword")).count()
        print(admincount)
        
        if admincount > 0:
            admin = tbl_admin.objects.get(admin_email=request.POST.get("txtemail"),admin_password=request.POST.get("txtpassword"))
            request.session["aid"] = admin.id
            request.session["aname"] = admin.admin_name
            return redirect("Administrator:homepage")
        elif staffcount > 0:
            staff = tbl_staff.objects.get(staff_email=request.POST.get("txtemail"),staff_password=request.POST.get("txtpassword"))
            request.session["sid"] = staff.id
            request.session["sname"] = staff.staff_name
            return redirect("Staff:homepage")    
        elif customercount > 0:
            customer = tbl_customer.objects.get(customer_email=request.POST.get("txtemail"),customer_password=request.POST.get("txtpassword"))
            request.session["cid"] = customer.id
            request.session["cname"] = customer.customer_name
            return redirect("Customer:homepage")   

        elif suppliercount > 0:
            supplier = tbl_supplier.objects.get(supplier_email=request.POST.get("txtemail"),supplier_password=request.POST.get("txtpassword"))
            request.session["eid"] = supplier.id
            request.session["ename"] = supplier.supplier_name
            return redirect("Supplier:homepage")  
        else:
            return render(request,"Guest/Login.html",{"msg":"Invalid Email Or Password"})
    else:
        return render(request,"Guest/Login.html")

def Index(request):
    return render(request,"Guest/Index.html")

def Logo(request):
    return render(request,"Guest/Login.html")

def customerInsertSelect(request):
    data=tbl_customer.objects.all()
    district=tbl_district.objects.all()
    data = tbl_customer.objects.all()
    if request.method=="POST":
        user_Name=request.POST.get('customer_name')
        user_Gender=request.POST.get('customer_gender')
        user_Contact=request.POST.get('customer_phone')
        user_Email=request.POST.get('customer_email')
        user_Password=request.POST.get('customer_password')
    
        user_Address=request.POST.get('customer_address')
        pe = tbl_place.objects.get(id=request.POST.get('sel_place'))
        tbl_customer.objects.create(customer_name=user_Name,customer_gender=user_Gender,customer_phone=user_Contact,customer_email=user_Email,customer_password=user_Password,customer_address=user_Address,place=pe,customer_photo=request.FILES.get("fileImage"),customer_proof=request.FILES.get("fileProof"))
        return render(request,"Guest/Customer.html",{'data':data})
    else:
        return render(request,"Guest/Customer.html",{"districtdata":district})

def delcustomer(request,cid):
    tbl_customer.objects.get(id=cid).delete()
    return redirect("Guest:customerInsertSelect")   



def about(request):
    return render(request, 'Guest/Aboutus.html')



def contactInsertSelect(request):
    data = Contact.objects.all()
    if request.method=="POST":
        Name=request.POST.get('name')
        Email=request.POST.get('email')
        msg=request.POST.get('message')
        Contact.objects.create(name=Name,email=Email,message=msg)
        return render(request,"Guest/Contact.html",{'data':data})
    else:
        return render(request,"Guest/Contact.html",{'data':data})





