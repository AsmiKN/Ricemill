from django.shortcuts import render,redirect
from Guest.models import *
from Administrator.models import *
from Customer.models import *
from datetime import datetime
import random

# Create your views here.
def homepage(request):
    return render(request,"Customer/Homepage.html")

def my_pro(request):
    data=tbl_customer.objects.get(id=request.session["cid"])
    return render(request,"Customer/Myprofile.html",{'data':data})

def editprofile(request):
    prodata=tbl_customer.objects.get(id=request.session["cid"])
    if request.method=="POST":
        prodata.customer_name=request.POST.get('txtname')
        prodata.customer_phone=request.POST.get('txtphone')
        prodata.customer_email=request.POST.get('txtemail')
        prodata.save()
        return render(request,"Customer/Editprofile.html",{'msg':"Profile Updated"})
    else:
        return render(request,"Customer/Editprofile.html",{'prodata':prodata})

def changepassword(request):
    if request.method=="POST":
        ccount=tbl_customer.objects.filter(id=request.session["cid"],customer_password=request.POST.get('txtcurpass')).count()
        if ccount>0:
            if request.POST.get('txtnewpass')==request.POST.get('txtconpass'):
                userdata=tbl_customer.objects.get(id=request.session["cid"],customer_password=request.POST.get('txtcurpass'))
                userdata.customer_password=request.POST.get('txtnewpass')
                userdata.save()
                return render(request,"Customer/ChangePassword.html",{'msg':"Password Updated"})
            else:
                return render(request,"Customer/ChangePassword.html",{'msg1':"Error in confirm Password"})
        else:
            return render(request,"Customer/ChangePassword.html",{'msg1':"Error in current password"})
    else:
        return render(request,"Customer/ChangePassword.html")


def productdetails(request):
    data=tbl_newproduct.objects.all()
    return render(request,"Customer/Viewproductdetail.html",{'data':data})  

def Addcart(request,pid):
    productdata=tbl_newproduct.objects.get(id=pid)
    custdata=tbl_customer.objects.get(id=request.session["cid"])
    bookingcount=tbl_productbooking.objects.filter(customer=custdata,booking_status=0).count()
    if bookingcount>0:
        bookingdata=tbl_productbooking.objects.get(customer=custdata,booking_status=0)
        cartcount=tbl_pcart.objects.filter(booking=bookingdata,product=productdata).count()
        if cartcount>0:
            msg="Already added"
            return render(request,"Customer/Viewproductdetail.html",{'msg':msg})
        else:
            tbl_pcart.objects.create(booking=bookingdata,product=productdata,cart_qty=1)
            msg="Added to cart"
            return render(request,"Customer/Viewproductdetail.html",{'msg':msg})
    else:
        tbl_productbooking.objects.create(customer=custdata)
        bookingcount=tbl_productbooking.objects.filter(booking_status=0,customer=custdata).count()
        if bookingcount>0:
            bookingdata=tbl_productbooking.objects.get(customer=custdata,booking_status=0)
            cartcount=tbl_pcart.objects.filter(booking=bookingdata,product=productdata).count()
            if cartcount>0:
                msg="Already added"
                return render(request,"Customer/Viewproductdetail.html",{'msg':msg})
            else:
                tbl_pcart.objects.create(booking=bookingdata,product=productdata,cart_qty=1)
                msg="Added to cart"
                return render(request,"Customer/Viewproductdetail.html",{'msg':msg})
            
    

def Mycart(request):
    if request.method=="POST":
        bookingdata=tbl_productbooking.objects.get(id=request.session["bookingid"])
        bookingdata.price=request.POST.get("carttotalamt")
        bookingdata.booking_status=1
        bookingdata.save()
        return redirect("Customer:payment")
    else:
        customerdata=tbl_customer.objects.get(id=request.session["cid"])
        bcount=tbl_productbooking.objects.filter(customer=customerdata,booking_status=0).count()
        if bcount>0:    
            book=tbl_productbooking.objects.get(customer=customerdata,booking_status=0)
            bid=book.id
            request.session["bookingid"]=bid
            bkid=tbl_productbooking.objects.get(id=bid)
            cartdata=tbl_pcart.objects.filter(booking=bkid)
            return render(request,"Customer/Mycart.html",{'data':cartdata})
        else:
            return render(request,"Customer/MyCart.html")
    
def DelCart(request,did):
   tbl_pcart.objects.get(id=did).delete()
   return redirect("Customer:mycart")

def CartQty(request):
   qty=request.GET.get('QTY')
   cartid=request.GET.get('ALT')
   cartdata=tbl_pcart.objects.get(id=cartid)
   cartdata.cart_qty=qty
   cartdata.save()
   return redirect("Customer:mycart")

def payment(request):
    if request.method=="POST":
        bookingdata=tbl_productbooking.objects.get(id=request.session["bookingid"])
        cart=tbl_pcart.objects.filter(booking=bookingdata)
        for i in cart:
            i.cart_status=1
            i.save()
        bookingdata.booking_status=2
        bookingdata.save()
        return render(request,"Customer/Bill.html",{"msg":"Payment Completed..."})
    else: 
        return render(request,"Customer/Payment.html")

def Billing(request):
    billno = random.randint(10000, 99999)
    today = datetime.now().strftime("%d-%m-%Y")
    cust = tbl_customer.objects.get(id=request.session["cid"])
    
    latest_booking = tbl_productbooking.objects.filter(customer=cust, booking_status=2).latest('booking_date')
    
    data = tbl_pcart.objects.filter(booking=latest_booking)
    total=latest_booking.price
    return render(request,"Customer/Bill.html",{'billno':billno,'today':today,'userdata':cust,'data':data,'total':total})
 

def logout(request):
    del request.session["cid"]
    return redirect("Guest:Logininsertselect")

def myorder(request):
    customer = tbl_customer.objects.get(id=request.session["cid"])
    data1 = tbl_productbooking.objects.filter(customer=customer)
    data = tbl_pcart.objects.filter(booking__in=data1)
    return render(request, "Customer/Myorder.html",{"Data":data})

def cancel(request,cid):
    data=tbl_pcart.objects.get(id=cid) 
    data.cart_status=2
    data.save()
    return render(request,"Customer/Myorder.html")

def POSTComplaint(request,did):
    data=tbl_complaint.objects.filter(user=request.session["cid"])
    userID=tbl_customer.objects.get(id=request.session["cid"])
    if request.method=="POST":
        title=request.POST.get('title')
        details=request.POST.get('complaint')
        tbl_complaint.objects.create(complaint_title=title,complaint_details=details,user=userID)
        return redirect("Customer:homepage")
    else:
        return render(request,"Customer/Complaint.html",{"data":data})
    
def delComplaint(request,did):
    tbl_complaint.objects.get(id=did).delete()
    return redirect("Customer:viewcomplaint") 

def FeedbackPost(request,did):
    if request.method=="POST":
        Subject=request.POST.get('txttitle')
        Content=request.POST.get('txtdetails')
        User=tbl_customer.objects.get(id=request.session["cid"])
        tbl_feedback.objects.create(feedback_subject=Subject,feedback_details=Content,user=User)
        return render(request,"Customer/FeedbackPost.html")
    else:
        return render(request,"Customer/FeedbackPost.html")


def viewcomplaint(request):
    data=tbl_complaint.objects.all()
    return render(request,"Customer/Viewcomplaint.html",{'data':data}) 