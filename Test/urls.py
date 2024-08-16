from django.urls import path,include
from Test import views
app_name="Test"

urlpatterns = [
   path('team/',views.teamInsertSelect,name="teamInsertSelect"),
   path('delteam/<int:tid>', views.delteam,name="delteam"),
   path('updateteam/<int:tid>',views.updateteam,name="update"),


   path('playercategory/',views.playercategoryInsertSelect,name="playercategoryInsertSelect"),
   path('delplayercategory/<int:pid>', views.delplayercategory,name="delplayercategory"),
   path('updateplayercategory/<int:pid>',views.updateplayercategory,name="updateplayercategory"),

   
   path('playerdetails/',views.PlayerdetailsInsertSelect,name="playerdetailsInsertSelect"),
   path('delplayerdetails/<int:pid>', views.delplayerdetails,name="delplayerdetails"),
   path('playerdetailsupdate/<int:pid>',views.playerdetailsupdate,name="playerdetailsupdate"),

   path('Matchschedule/',views.matchscheduleInsertSelect,name="matchscheduleInsertSelect"),
   path('delmatchschedule/<int:mid>', views.delmatchschedule,name="delmatchschedule"),
   path('matchscheduleupdate/<int:mid>',views.matchscheduleupdate,name="matchscheduleupdate"),


    path('Playereleven/',views.playerEleveninsertSelect,name="playerEleveninsertSelect"),
    path('AjaxPlayerdetails/',views.ajaxplayerdetails,name="ajaxplayerdetails"),
    path('scheduleview/',views.scheduleview,name="scheduleview"),
    path('ViewXI/<int:id>',views.ViewXI,name="ViewXI")    
]
