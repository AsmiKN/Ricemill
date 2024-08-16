from django.urls import path,include
from Customer import views

app_name="Customer"
urlpatterns = [

    path('homepage/',views.homepage,name="homepage"),
    path('My_profile/',views.my_pro,name="my_pro"),
    path('editprofile/',views.editprofile,name="editprofile"),
    path('changepassword/',views.changepassword,name="changepassword"),
    
    path('productdetails/',views.productdetails,name="productdetails"),

    path('Addcart/<int:pid>',views.Addcart,name="Addcart"),
    path('Mycart/',views.Mycart,name="mycart"),
    path('DelCart/<int:did>',views.DelCart,name="delcart"),
    path('CartQty/',views.CartQty,name="cartqty"),
    path('Payment/',views.payment,name="payment"),
    path('Billing/',views.Billing,name="Billing"),

    path('logout/',views.logout,name="logout"),

    
    path('myorder/',views.myorder,name="myorder"),
    path('cancel/<int:cid>',views.cancel,name="cancel"),
    path('Complaint/<int:did>',views.POSTComplaint,name="POSTComplaint"),
    path('delComplaint/<int:did>',views.delComplaint,name="delComplaint"),  
    path('FeedbackPost/<int:did>',views.FeedbackPost,name="FeedbackPost"),

    path('viewcomplaint/',views.viewcomplaint,name="viewcomplaint"),

]