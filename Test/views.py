from django.shortcuts import render,redirect
from Test.models import *

# Create your views here.

def teamInsertSelect(request):
    data=tbl_team.objects.all()
    if request.method=="POST":
        teamName=request.POST.get('txtname')
        tbl_team.objects.create(team_name=teamName)
        return render(request,"Test/Team.html",{'data':data})
    else:
        return render(request,"Test/Team.html",{'data':data})

def delteam(request,tid):
    tbl_team.objects.get(id=tid).delete()
    return redirect("Test:teamInsertSelect")


def updateteam(request,tid):
    editdata=tbl_team.objects.get(id=tid)
    if request.method=="POST":
        editdata.team_name=request.POST.get("txtname")
        editdata.save()
        return redirect("Test:teamInsertSelect")
    else:
        return render(request,"Test\Team.html",{"editdata":editdata})


def playercategoryInsertSelect(request):
    data=tbl_playercategory.objects.all()
    if request.method=="POST":
        placatName=request.POST.get('txtname')
        tbl_playercategory.objects.create(playercategory_name=placatName)
        return render(request,"Test/Playercategory.html",{'data':data})
    else:
        return render(request,"Test/Playercategory.html",{'data':data})

def delplayercategory(request,pid):
    tbl_playercategory.objects.get(id=pid).delete()
    return redirect("Test:playercategoryInsertSelect")


def updateplayercategory(request,pid):
    editdata=tbl_playercategory.objects.get(id=pid)
    if request.method=="POST":
        editdata.playercategory_name=request.POST.get("txtname")
        editdata.save()
        return redirect("Test:playercategoryInsertSelect")
    else:
        return render(request,"Test\playercategory.html",{"editdata":editdata})


def PlayerdetailsInsertSelect(request):
    data=tbl_playerdetails.objects.all()
    team=tbl_team.objects.all()
    playercategory=tbl_playercategory.objects.all()
    if request.method=="POST":
        pc=tbl_playercategory.objects.get(id=request.POST.get('sel_playercategory'))
        playerdetails_Name=request.POST.get('txtname')
        playerdetails_Dob=request.POST.get('txtdob')
        playerdetails_Photo=request.FILES.get('fileImage')
        team=tbl_team.objects.get(id=request.POST.get('sel_team'))
        tbl_playerdetails.objects.create(playerdetails_name=playerdetails_Name,playerdetails_dob=playerdetails_Dob,playerdetails_photo=playerdetails_Photo,team=team,playercategory=pc)
        return render(request,"Test/Playerdetails.html",{'data':data})
    else:
       return render(request,"Test/Playerdetails.html",{'teamdata':team,'playercategorydata':playercategory,'data':data})

def delplayerdetails(request,pid):
    tbl_playerdetails.objects.get(id=pid).delete()
    return redirect("Test:PlayerdetailsInsertSelect")


def playerdetailsupdate(request,pid):
    editdata=tbl_playerdetails.objects.get(id=pid)
    if request.method=="POST":
        editdata.playerdetails_name=request.POST.get("txtname")
        editdata.save()
        return redirect("Test:playerdetailsInsertSelect")
    else:
        return render(request,"Test/Playerdetails.html",{"editdata":editdata})

def matchscheduleInsertSelect(request):
    data=tbl_matchschedule.objects.all()
    
    if request.method=="POST":
        
        match_Name=request.POST.get('txtname')
        match_Todate=request.POST.get('txttodate')
        match_Fromdate=request.POST.get('txtdate')
        match_Venue=request.POST.get('txtvenue')
        tbl_matchschedule.objects.create(match_name=match_Name,match_todate=match_Todate,match_fromdate=match_Fromdate,match_venue=match_Venue)
        return render(request,"Test/Matchschedule.html",{'data':data})
    else:
       return render(request,"Test/Matchschedule.html",{'data':data})

def delmatchschedule(request,mid):
    tbl_matchschedule.objects.get(id=mid).delete()
    return redirect("Test:matchscheduleInsertSelect")


def matchscheduleupdate(request,mid):
    editdata=tbl_matchschedule.objects.get(id=mid)
    if request.method=="POST":
        editdata.playerdetails_name=request.POST.get("txtname")
        editdata.save()
        return redirect("Test:matchscheduleInsertSelect")
    else:
        return render(request,"Test/Matchschedule.html",{"editdata":editdata})

def playerEleveninsertSelect(request):
    Team = tbl_team.objects.all()
    shedule=tbl_matchschedule.objects.all()
    data=tbl_playerxi.objects.all()
    if request.method=="POST":
        player = tbl_playerdetails.objects.get(id=request.POST.get('sel_playerdetails'))
        shedule =tbl_matchschedule.objects.get(id=request.POST.get('sel_matchshedule'))
        tbl_playerxi.objects.create(playerdetails=player,matchschedule=shedule)
        return redirect("Test:playerEleveninsertSelect")
    else:
        return render(request,"Test/Playereleven.html",{"data":data,"teamdata":Team,"sheduledata":shedule})

def ajaxplayerdetails(request):
    team = tbl_team.objects.get(id=request.GET.get("did"))
    playerdetails = tbl_playerdetails.objects.filter(team=team)
    return render(request,"Test/Ajaxplayerdetails.html",{"playerdetailsdata":playerdetails})


def scheduleview(request):
    data=tbl_matchshedule.objects.all()
    return render(request,"Test/ScheduleView.html",{'data':data})


def ViewXI(request,id):
    data=tbl_playerxi.objects.filter(shedule=id)
    return render(request,"Test/PlayingXI.html",{'data':data})