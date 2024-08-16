from django.urls import path,include
from Administrator import views
#from Guest import views
app_name="Administrator"
urlpatterns = [

    # path('HomePage/',views.LoadingHomePage,name="LoadingHomePage"),

    path('District/',views.districtInsertSelect,name= "districtInsertSelect"),
    path('delDistrict/<int:did>', views.delDistrict,name="delDistrict"),
    path('districtupdate/<int:eid>',views.districtupdate,name="districtupdate"),



    path('Category/',views.categoryInsertSelect,name= "categoryInsertSelect"),
    path('delcategory/<int:cid>', views.delcategory,name="delcategory"),
    path('updatecategory/<int:eid>',views.updatecategory,name="updatecategory"),


    path('Department/',views.departmentInsertSelect,name="departmentInsertSelect"),
    path('deldepartment/<int:did>', views.deldepartment,name="deldepartment"),
    path('updatedepartment/<int:eid>',views.updatedepartment,name="updatedepartment"),

    path('Designation/',views.designationInsertSelect,name="designationInsertSelect"),
    path('deldesignation/<int:did>', views.deldesignation,name="deldesignation"),
    path('updatedesignation/<int:eid>',views.updatedesignation,name="updatedesignation"),




    path('Place/', views.placeInsertSelect,name="placeInsertSelect"),
    path('delPlace/<int:did>', views.delPlace,name="delPlace"),
    path('placeupdate/<int:eid>',views.placeupdate,name="placeupdate"),

    path('Place/', views.placeInsertSelect,name="placeInsertSelect"),
    path('delPlace/<int:did>', views.delPlace,name="delPlace"),
    path('placeupdate/<int:eid>',views.placeupdate,name="placeupdate"),

    path('employee/', views.employeeInsertSelect,name="employeeInsertSelect"),
    path('delemployee/<int:eid>', views.delemployee,name="delemployee"),
    path('employeeupdate/<int:eid>',views.employeeupdate,name="employeeupdate"),


    path('course/', views.courseInsertSelect,name="courseInsertSelect"),
    path('delcourse/<int:cid>', views.delcourse,name="delcourse"),
    path('courseupdate/<int:cid>',views.courseupdate,name="courseupdate"),

    
   path('Subject/',views.subjectInsertSelect,name="subjectInsertSelect"),
   path('delsubject/<int:sid>', views.delsubject,name="delsubject"),
   path('subjectupdate/<int:sid>',views.subjectupdate,name="subjectupdate"),


   path('Semester/',views.semesterInsertSelect,name="semesterInsertSelect"),
   path('delsemester/<int:sid>', views.delsemester,name="delsemester"),
   path('semesterupdate/<int:sid>',views.semesterupdate,name="semesterupdate"),


   path('Syllabus/', views.syllabusInsertSelect,name="syllabusInsertSelect"),
   path('delsyllabus/<int:sid>', views.delsyllabus,name="delsyllabus"),
   path('syllabusupdate/<int:sid>',views.syllabusupdate,name="syllabusupdate"),

  
 path('Admin/',views.AdminInsertSelect,name="AdminInsertSelect"),
   path('delAdmin/<int:aid>', views.delAdmin,name="delAdmin"),
   path('Adminupdate/<int:aid>',views.Adminupdate,name="Adminupdate"),
   
   path('Newuserlist/',views.newuserlist,name="newuserlist"),

   path('subcategory/', views.subcategoryInsertSelect,name="subcategoryInsertSelect"),
   path('delsubcategory/<int:sid>', views.delsubcategory,name="delsubcategory"),
   path('subcategoryupdate/<int:sid>',views.subcategoryupdate,name="subcategoryupdate"),

   
    path('Product/',views.productInsertSelect,name="productInsertSelect"),
    path('ajaxsubcategory/',views.ajaxsubcategory,name="ajaxsubcategory"),

    path('Gallery/',views.galleryInsertSelect,name="galleryInsertSelect"),
    path('ajaxproduct/',views.ajaxproduct,name="ajaxproduct"),

    path('ComplaintView/',views.complaintSelect,name="complaintSelect"), 
    path('ComplaintReply/<int:cid>',views.complaintreplayInsert,name="complaintreplayInsert"),
    path('ComplaintSolvedView/',views.complaintsolvedSelect,name="complaintsolvedSelect"),

    path('FeedbackView/',views.feedbackSelect,name="feedbackSelect"),
    path('FeedbackView/<int:cid>',views.feedbackDelete,name="feedbackDelete"),
    
    path('role/',views.roleInsertSelect,name= "roleInsertSelect"),
    path('delrole/<int:rid>', views.delrole,name="delrole"),
    path('updaterole/<int:rid>',views.updaterole,name="updaterole"),

    path('staff/',views.staffInsertSelect,name="staffInsertSelect"),
    path('delstaff/<int:sid>', views.delstaff,name="delstaff"),
    path('staffupdate/<int:sid>',views.staffupdate,name="staffupdate"),  

    path('Admin_dashboard/',views.Dashboard,name="Dashboard"),

    path('Rawmaterial/',views.rawmaterialInsertSelect,name= "rawmaterialInsertSelect"),
    path('delrawmaterial/<int:rid>', views.delrawmaterial,name="delrawmaterial"),
    path('rawmaterialupdate/<int:rid>',views.rawmaterialupdate,name="rawmaterialupdate"),

    path('Unit/',views.unitInsertSelect,name= "unitInsertSelect"),
    path('delunit/<int:uid>', views.delunit,name="delunit"),
    path('unitupdate/<int:uid>',views.unitupdate,name="unitupdate"),

    path('Newproduct/',views.newproductInsertSelect,name= "newproductInsertSelect"),
    path('delnewproduct/<int:pid>', views.delnewproduct,name="delnewproduct"),
    path('newproductupdate/<int:pid>',views.newproductupdate,name="newproductupdate"),

    path('homepage/',views.homepage,name="homepage"),
    path('My_profile/',views.my_pro,name="my_pro"),
    path('Editprofile/',views.editprofile,name="editprofile"),
    path('changepassword/',views.changepassword,name="changepassword"),

    path('supplier/',views.suppliersInsertSelect,name= "suppliersInsertSelect"),
    path('delsupplier/<int:vid>', views.delsupplier,name="delsupplier"),
    path('updatesupplier/<int:vid>',views.updatesupplier,name="updatesupplier"),

    path('rawmaterialcons/',views.rawmaterialconsInsertSelect,name= "rawmaterialconsInsertSelect"),
    path('delrawmaterialcons/<int:vid>', views.delrawmaterialcons,name="delrawmaterialcons"),
    path('rawmaterialconsupdate/<int:vid>',views.rawmaterialconsupdate,name="rawmaterialconsupdate"),

    path('production/',views.productionInsertSelect,name= "productionInsertSelect"),
    path('delproduction/<int:pid>', views.delproduction,name="delproduction"),
    path('updateproduction/<int:pid>',views.updateproduction,name="updateproduction"),

    path('supplierrawmaterial/',views.supplierrawmaterial,name="supplierrawmaterial"),
    path('supplierdetails/',views.supplierdetails,name="supplierdetails"),

    path('Addstock/<int:did>', views.addstock,name="addstock"),
    path('delstock/<int:did>', views.delstock,name="delstock"),
    path('vieworder', views.vieworder,name="vieworder"),
    path('details/<int:did>', views.details,name="details"),
    path('updateproductbooking/<int:bid>', views.updateproductbooking,name="updateproductbooking"),
    
    path('logout/',views.logout,name="logout"),

    
    path('viewcustomer/',views.viewcustomer,name="viewcustomer"),
    path('adminsreport/',views.adminsreport,name="adminsreport"),

    path('AddStock/<int:did>', views.addstock,name="addstock"),
    path('delstock/<int:did>', views.delstock,name="delstock"),
  
]  
