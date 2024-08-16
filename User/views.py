from django.shortcuts import render,redirect
from Guest.models import *
from User.models import *

# Create your views here.
def homepage(request):
    return render(request,"User/HomePage.html")

def my_pro(request):
    data=tbl_newuser.objects.get(id=request.session["uid"])
    return render(request,"User/MyProfile.html",{'data':data})

def editprofile(request):
    prodata=tbl_newuser.objects.get(id=request.session["uid"])
    if request.method=="POST":
        prodata.newuser_name=request.POST.get('txtname')
        prodata.newuser_contact=request.POST.get('txtcontact')
        prodata.newuser_email=request.POST.get('txtemail')
        prodata.save()
        return render(request,"User/EditProfile.html",{'msg':"Profile Updated"})
    else:
        return render(request,"User/EditProfile.html",{'prodata':prodata})

def changepassword(request):
    if request.method=="POST":
        ccount=tbl_newuser.objects.filter(id=request.session["uid"],newuser_password=request.POST.get('txtcurpass')).count()
        if ccount>0:
            if request.POST.get('txtnewpass')==request.POST.get('txtconpass'):
                userdata=tbl_newuser.objects.get(id=request.session["uid"],newuser_password=request.POST.get('txtcurpass'))
                userdata.newuser_password=request.POST.get('txtnewpass')
                userdata.save()
                return render(request,"User/ChangePassword.html",{'msg':"Password Updated"})
            else:
                return render(request,"User/ChangePassword.html",{'msg1':"Error in confirm Password"})
        else:
            return render(request,"User/ChangePassword.html",{'msg1':"Error in current password"})
    else:
        return render(request,"User/ChangePassword.html")


def POSTComplaint(request):
    data=tbl_complaint.objects.filter(user=request.session["uid"])
    userID=tbl_newuser.objects.get(id=request.session["uid"])
    if request.method=="POST":
        title=request.POST.get('title')
        details=request.POST.get('complaint')
        tbl_complaint.objects.create(complaint_title=title,complaint_details=details,user=userID)
        return redirect("User:POSTComplaint")
    else:
        return render(request,"User/Complaint.html",{"data":data})
    
def delComplaint(request,did):
    tbl_complaint.objects.get(id=did).delete()
    return redirect("User:POSTComplaint")   

def feedbackInsert(request):
    if request.method=="POST":
        Subject=request.POST.get('txttitle')
        Content=request.POST.get('txtdetails')
        User=tbl_newuser.objects.get(id=request.session["uid"])
        tbl_feedback.objects.create(feedback_subject=Subject,feedback_details=Content,user=User)
        return render(request,"User/FeedbackPost.html")
    else:
        return render(request,"User/FeedbackPost.html")
  