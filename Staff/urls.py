from django.urls import path,include
from Staff import views


app_name="Staff"
urlpatterns = [

    path('homepage/',views.homepage,name="homepage"),
    path('My_profile/',views.my_pro,name="my_pro"),
    path('editprofile/',views.editprofile,name="editprofile"),
    path('changepassword/',views.changepassword,name="changepassword"),
    
    path('supplierdetails/',views.supplierdetails,name="supplierdetails"),
    path('supplierrawmaterial/',views.supplierrawmaterial,name="supplierrawmaterial"),
    
    path('Addcart/<int:pid>',views.Addcart,name="Addcart"),
    path('Mycart/',views.Mycart,name="mycart"),
    path('DelCart/<int:did>',views.DelCart,name="delcart"),
    path('CartQty/',views.CartQty,name="cartqty"),
    path('Payment/',views.payment,name="payment"),


    path('purchase/', views.purchaseInsertSelect,name="purchaseInsertSelect"),
    path('delpurchase/<int:pid>', views.delpurchase,name="delpurchase"),
    path('purchaseupdate/<int:pid>',views.purchaseupdate,name="purchaseupdate"),
  
    path('Purchasereport/',views.Purchasereport,name="Purchasereport"),
   

    path('logout/',views.logout,name="logout"),

    path('myorder/',views.myorder,name="myorder"),
    path('ViewProduct/<int:id>',views.ViewProduct,name="ViewProduct"),

    path('Billing/<int:id>',views.Billing,name="Billing"),
]