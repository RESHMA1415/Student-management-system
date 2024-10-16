"""
URL configuration for Student1 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path
from studentapp.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path("home/",home),
    path("adminhome/",adminhome),
    path("teachhome/",teacherhome),
    path("studenthome/",studenthome),
    path("login/",logins),

    path("register/",student_register),
    path("teacher_reg/",teacher),

    path("view_teacher_profile",view_teacher_profile),
    path("view_stud_profile",view_stud_profile),

    path("view_teachers",view_teachers),
    path("view_student",view_student),

    path("view_teacher",view_teacher),
    path("view_students",view_students),

    path("delete_student/<int:id>", delete_student),
    path("delete_teacher/<int:id>", delete_teacher),

    path("edit_teacher", edit_teacher),
    path("update_teacher/<int:id>", update_teacher),
    path("edit_student",edit_student),
    path("update_student/<int:id>",update_student),

    path("logout",logouts),
    path("approve_student/<int:id>",approve_student),
]
