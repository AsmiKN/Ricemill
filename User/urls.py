from django.urls import path,include
from User import views

app_name="User"
urlpatterns = [


    path('homepage/',views.homepage,name="homepage"),
    path('My_profile/',views.my_pro,name="my_pro"),
    path('editprofile/',views.editprofile,name="editprofile"),
    path('changepassword/',views.changepassword,name="changepassword"),
    
    path('Complaint/',views.POSTComplaint,name="POSTComplaint"),
    path('delComplaint/<int:did>',views.delComplaint,name="delComplaint"),  
    
    path('FeedbackView/',views.feedbackInsert,name="feedbackInsert"),

]