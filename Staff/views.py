from django.shortcuts import render,redirect
from Guest.models import *
from Administrator.models import *
from Supplier.models import *
from Staff.models import *
import random
from datetime import datetime

# Create your views here.
def homepage(request):
    return render(request,"Staff/Homepage.html")

def my_pro(request):
    data=tbl_staff.objects.get(id=request.session["sid"])
    return render(request,"Staff/Myprofile.html",{'data':data})

def editprofile(request):
    prodata=tbl_staff.objects.get(id=request.session["sid"])
    if request.method=="POST":
        prodata.staff_name=request.POST.get('txtname')
        prodata.staff_address=request.POST.get('txtaddress')
        prodata.staff_email=request.POST.get('txtemail')
        prodata.save()
        return render(request,"Staff/Editprofile.html",{'msg':"Profile Updated"})
    else:
        return render(request,"Staff/Editprofile.html",{'prodata':prodata})

def changepassword(request):
    if request.method=="POST":
        ccount=tbl_staff.objects.filter(id=request.session["sid"],staff_password=request.POST.get('txtcurpass')).count()
        if ccount>0:
            if request.POST.get('txtnewpass')==request.POST.get('txtconpass'):
                userdata=tbl_staff.objects.get(id=request.session["sid"],staff_password=request.POST.get('txtcurpass'))
                userdata.newuser_password=request.POST.get('txtnewpass')
                userdata.save()
                return render(request,"Staff/ChangePassword.html",{'msg':"Password Updated"})
            else:
                return render(request,"Staff/ChangePassword.html",{'msg1':"Error in confirm Password"})
        else:
            return render(request,"Staff/ChangePassword.html",{'msg1':"Error in current password"})
    else:
        return render(request,"Staff/ChangePassword.html")

def supplierdetails(request):
    data=tbl_supplier.objects.all()
    return render(request,"Staff/Viewsupplierlist.html",{'data':data})  


def supplierrawmaterial(request):
    data=tbl_supplierraw.objects.all()
    return render(request,"Staff/Viewsupplierrawmaterial.html",{'data':data}) 

def Addcart(request,pid):
    productdata=tbl_supplierraw.objects.get(id=pid)
    custdata=tbl_staff.objects.get(id=request.session["sid"])
    bookingcount=tbl_rawmaterialbooking.objects.filter(staff=custdata,booking_status=0).count()
    if bookingcount>0:
        bookingdata=tbl_rawmaterialbooking.objects.get(staff=custdata,booking_status=0)
        cartcount=tbl_cart.objects.filter(booking=bookingdata,product=productdata).count()
        if cartcount>0:
            msg="Already added"
            return render(request,"Staff/Mycart.html",{'msg':msg})
        else:
            tbl_cart.objects.create(booking=bookingdata,product=productdata,cart_qty=1)
            msg="Added to cart"
            return render(request,"Staff/Mycart.html",{'msg':msg})
    else:
        tbl_rawmaterialbooking.objects.create(staff=custdata)
        bookingcount=tbl_rawmaterialbooking.objects.filter(booking_status=0,staff=custdata).count()
        if bookingcount>0:
            bookingdata=tbl_rawmaterialbooking.objects.get(staff=custdata,booking_status=0)
            cartcount=tbl_cart.objects.filter(booking=bookingdata,product=productdata).count()
            if cartcount>0:
                msg="Already added"
                return render(request,"Staff/Mycart.html",{'msg':msg})
            else:
                tbl_cart.objects.create(booking=bookingdata,product=productdata,cart_qty=1)
                msg="Added to cart"
                return render(request,"Staff/Mycart.html",{'msg':msg})
    

def Mycart(request):
    if request.method=="POST":
        bookingdata=tbl_rawmaterialbooking.objects.get(id=request.session["bookingid"])
        bookingdata.price=request.POST.get("carttotalamt")
        bookingdata.booking_status=1
        bookingdata.save()
        return redirect("Staff:payment")
    else:
        customerdata=tbl_staff.objects.get(id=request.session["sid"])
        bcount=tbl_rawmaterialbooking.objects.filter(staff=customerdata,booking_status=0).count()
        if bcount>0:    
            book=tbl_rawmaterialbooking.objects.get(staff=customerdata,booking_status=0)
            bid=book.id
            request.session["bookingid"]=bid
            bkid=tbl_rawmaterialbooking.objects.get(id=bid)
            cartdata=tbl_cart.objects.filter(booking=bkid)
            return render(request,"Staff/MyCart.html",{'data':cartdata})
        else:
            return render(request,"Staff/MyCart.html")
    
def DelCart(request,did):
   tbl_cart.objects.get(id=did).delete()
   return redirect("Staff:mycart")

def CartQty(request):
   qty=request.GET.get('QTY')
   cartid=request.GET.get('ALT')
   cartdata=tbl_cart.objects.get(id=cartid)
   cartdata.cart_qty=qty
   cartdata.save()
   return redirect("Staff:mycart")

def payment(request):
    if request.method=="POST":
        bookingdata=tbl_rawmaterialbooking.objects.get(id=request.session["bookingid"])
        bookingdata.booking_status=2
        bookingdata.save()
        return render(request,"Staff/Bill.html",{'msg':'Payment Completed',"id":bookingdata.id})
    else: 
        return render(request,"Staff/Payment.html")

def purchaseInsertSelect(request):
    supplier = tbl_supplier.objects.all()
    rawmaterial=tbl_rawmaterial.objects.all()
    data=tbl_purchase.objects.all()
    if request.method=="POST":
        
        date=request.POST.get('txtdate')
        qty=request.POST.get('txtquantity')
        amt=request.POST.get('txtamt')
        sup = tbl_supplier.objects.get(id=request.POST.get('sel_supplier_name'))
        raw = tbl_rawmaterial.objects.get(id=request.POST.get('sel_rawmaterial'))
        tbl_purchase.objects.create(date=date,quantity=qty,amount=amt,supplier_name=sup,rawmaterial=raw)
        
        return render(request,"Staff/Rawmaterialpurchasereport.html",{'data':data})
    else:
        return render(request,"Staff/Rawmaterialpurchasereport.html",{'data':data,"supplierdata":supplier,"rawmaterialdata":rawmaterial})

def delpurchase(request,pid):
    tbl_purchase.objects.get(id=pid).delete()
    return redirect("Staff:purchaseInsertSelect")


def purchaseupdate(request,pid):    
    supplier = tbl_supplier.objects.all()
    rawmaterial=tbl_rawmaterial.objects.all()
    editdata=tbl_purchase.objects.get(id=pid)
    if request.method=="POST":
        editdata.date=request.POST.get("txtdate")
        editdata.quantity=request.POST.get("txtquantity")
        editdata.amount=request.POST.get("txtamt")
        sup = tbl_supplier.objects.get(id=request.POST.get('sel_supplier_name'))
        editdata.supplier = sup
        raw= tbl_rawmaterial.objects.get(id=request.POST.get('sel_rawmaterial'))
        editdata.rawmaterial = raw
        editdata.save()
        return redirect("Staff:purchaseInsertSelect")
    else:
        return render(request,"Staff/Rawmaterialpurchasereport.html",{"editdata":editdata,"supplierdata":supplier,"rawmaterialdata":rawmaterial})

def purchasereport(request):
    data=tbl_purchase.objects.all()
    return render(request,"Staff/Viewpurchasereport.html",{'data':data}) 


def logout(request):
    del request.session["sid"]
    return redirect("Guest:Logininsertselect")


def myorder(request):
    staff=tbl_staff.objects.get(id=request.session["sid"])
    data=tbl_rawmaterialbooking.objects.filter(staff=staff,booking_status__gte=2)
    return render(request,"Staff/Myorder.html",{"data":data})    

def ViewProduct(request,id):
    bookingid=tbl_rawmaterialbooking.objects.get(id=id)
    data=tbl_cart.objects.filter(booking=bookingid)
    return render(request,"Staff/ViewProduct.html",{"data":data})


def Billing(request,id):
    billno=random.randint(10000,99999)
    today = datetime.now()
    today=today.strftime("%d-%m-%Y")
    bookingid=tbl_rawmaterialbooking.objects.get(id=id)
    data=tbl_cart.objects.filter(booking=bookingid)
    return render(request,"Staff/Bill.html",{'billno':billno,'today':today,'data':data,'booking':bookingid})  


def Purchasereport(request):
    if request.method=="POST":
        fromdate=request.POST.get('txtfdate')
        todate=request.POST.get('txtdate')
        data=tbl_cart.objects.filter(booking__booking_date__gte=fromdate,booking__booking_date__lte=todate)
        bill = []
        for i in data:
            bill.append(random.randint(10000,99999))
        datas = zip(data,bill)
        return render(request,"Staff/Purchasereport.html",{'data':datas})
    else:
        return render(request,"Staff/Purchasereport.html")  