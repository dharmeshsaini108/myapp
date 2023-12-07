from django.contrib import admin
from django.urls import path,include
from .views import*  

urlpatterns = [
   path("home/",emp_home),
   path("add-emp/",add_emp),
   path("delete-emp/<int:emp_id>",delete_emp),     #for deleting in table
   path("update-emp/<int:emp_id>",update_emp),     #for updating table
   path("do-update-emp/<int:emp_id>",do_update_emp),     
   path("testimonials/",testimonials),     
   path("feedback/",feedback),     
]
