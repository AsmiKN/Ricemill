from django.shortcuts import render,redirect
from Administrator.models import *
from Guest.models import *
from Supplier.models import *
from Staff.models import *
from Customer.models import *
from Supplier import views
from Staff import views
import random
from datetime import datetime


# Create your views here.
def homepage(request):
    return render(request,"Supplier/Homepage.html")

def my_pro(request):
    data=tbl_supplier.objects.get(id=request.session["eid"])
    return render(request,"Supplier/Myprofile.html",{'data':data})

def editprofile(request):
    prodata=tbl_supplier.objects.get(id=request.session["eid"])
    if request.method=="POST":
        prodata.supplier_name=request.POST.get('txtname')
        prodata.supplier_phone=request.POST.get('txtphone')
        prodata.supplier_email=request.POST.get('txtemail')
        prodata.save()
        return render(request,"Supplier/Editprofile.html",{'msg':"Profile Updated"})
    else:
        return render(request,"Supplier/Editprofile.html",{'prodata':prodata})

def changepassword(request):
    if request.method=="POST":
        ccount=tbl_supplier.objects.filter(id=request.session["eid"],supplier_password=request.POST.get('txtcurpass')).count()
        if ccount>0:
            if request.POST.get('txtnewpass')==request.POST.get('txtconpass'):
                userdata=tbl_supplier.objects.get(id=request.session["eid"],supplier_password=request.POST.get('txtcurpass'))
                userdata.newuser_password=request.POST.get('txtnewpass')
                userdata.save()
                return render(request,"Supplier/ChangePassword.html",{'msg':"Password Updated"})
            else:
                return render(request,"Supplier/ChangePassword.html",{'msg1':"Error in confirm Password"})
        else:
            return render(request,"Supplier/ChangePassword.html",{'msg1':"Error in current password"})
    else:
        return render(request,"Supplier/ChangePassword.html")



def suprawInsertSelect(request):
    data=tbl_supplierraw.objects.filter(supplier=request.session["eid"])
    supplier=tbl_supplier.objects.get(id=request.session["eid"]) 
    raw=tbl_rawmaterial.objects.all()
    uni=tbl_unit.objects.all()
    if request.method=="POST":
        rate=request.POST.get('txtrate')
        uni = tbl_unit.objects.get(id=request.POST.get('sel_unit'))
        raw = tbl_rawmaterial.objects.get(id=request.POST.get('sel_rawmaterial'))
        tbl_supplierraw.objects.create(supraw_rate=rate,unit=uni,rawmaterial=raw,supplier=supplier)
        return redirect("Supplier:suprawInsertSelect")
    else:
        return render(request,"Supplier/SupplierRawmaterial.html",{'data':data,"rawmaterialdata":raw,"unitdata":uni})

def delsupraw(request,eid):
    tbl_supplierraw.objects.get(id=eid).delete()
    return redirect("Supplier:suprawInsertSelect")   

def updatesupraw(request,eid):
    rawmaterial=tbl_rawmaterial.objects.all()
    unit=tbl_unit.objects.all()
    sup=tbl_supplier.objects.all()
    editdata=tbl_supplierraw.objects.get(id=eid)
    if request.method=="POST":
        editdata.rate=request.POST.get("txtrate")
       
       
        editdata.save()
        return redirect("Supplier:suprawInsertSelect")
    else:
        return render(request,"Supplier/SupplierRawmaterial.html",{"editdata":editdata,"rawmaterialdata":rawmaterial,"unitdata":unit,"supplierdata":sup})


# def salesreport(request):
#     data=tbl_sales.objects.all()
#     return render(request,"Supplier/Viewsalesreport.html",{'data':data}) 


def logout(request):
    del request.session["eid"]
    return redirect("Guest:Logininsertselect")

def Report(request):
  
   
    if request.method=="POST":
        fromdate=request.POST.get('txtfdate')
        todate=request.POST.get('txtdate')
        data=tbl_cart.objects.filter(booking__booking_date__gte=fromdate,booking__booking_date__lte=todate)
        bill = []
        for i in data:
            bill.append(random.randint(10000,99999))
        datas = zip(data,bill)
        return render(request,"Supplier/Report.html",{'data':datas})
    else:
        return render(request,"Supplier/Report.html")
