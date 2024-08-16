from django.urls import path,include
from Administrator import views
from Guest import views
app_name="Guest"

urlpatterns = [

    path('Newuser/',views.userInsertSelect,name="userInsertSelect"),
    
    path('ajaxplace/',views.ajaxplace,name="ajaxplace"),

    path('Login/',views.Logininsertselect,name="Logininsertselect"),


    path('',views.Index,name="Index"),

    path('Customer/',views.customerInsertSelect,name= "customerInsertSelect"),
    path('delcustomer/<int:cid>', views.delcustomer,name="delcustomer"),
   
    
    path('about/', views.about, name='about'),

    path('contactInsertSelect/', views.contactInsertSelect, name='contactInsertSelect'),

     
]

