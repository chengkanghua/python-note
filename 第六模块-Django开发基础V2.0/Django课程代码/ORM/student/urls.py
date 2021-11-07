from django.contrib import admin
from django.urls import path,include

from student.views import add_student,select_student,select2_student,select3_student,update_student,delete_student


urlpatterns = [
   path("add/",add_student),
   path("select/",select_student),
   path("select2/",select2_student),
   path("select3/",select3_student),
   path("update/",update_student),
   path("delete/",delete_student),

]
