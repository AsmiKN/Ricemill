from django.urls import path,include
from Supplier import views




app_name="Supplier"
urlpatterns = [

    path('homepage/',views.homepage,name="homepage"),
    path('My_profile/',views.my_pro,name="my_pro"),
    path('editprofile/',views.editprofile,name="editprofile"),
    path('changepassword/',views.changepassword,name="changepassword"),
    
   

    path('supraw/',views.suprawInsertSelect,name= "suprawInsertSelect"),
    path('delsupraw/<int:eid>', views.delsupraw,name="delsupraw"),
    path('updatesupraw/<int:eid>',views.updatesupraw,name="updatesupraw"),

    
    
    
  
    path('Report/',views.Report,name="Report"),

    path('logout/',views.logout,name="logout"),

]