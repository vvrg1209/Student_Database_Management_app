from django.contrib import admin
from django.urls import path
from authen import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('register', views.register, name='register'),
    path('my_login', views.my_login, name='my_login'),
    path('profile', views.profile, name='profile'),
    path('addData', views.addData, name='addData'),
    path('updateData/<int:rollnumber>', views.updateData, name='updateData'),
    path('deleteData/<int:rollnumber>', views.deleteData, name='deleteData'),
    path('student', views.student, name='student'),
    path('viewData/<int:rollnumber>', views.viewData, name='viewData'),
    path('logout',views.logout,name='logout'),
    path('stdlogin/<int:rollnumber>', views.stdlogin, name='stdlogin'),
    path('teacher', views.teacher, name='teacher'),
]