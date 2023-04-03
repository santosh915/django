from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name="index"),
    path('about',views.about,name="about"),
    path('sum/<int:a>/<int:b>',views.sum,name='sum'),
    path('introduction/<str:name>/<int:age>',views.introduction,name="intoduction"),
    path('myfirstpage',views.myfirstpage,name="myfisrstpage"),
    path('mysecondpage',views.mysecondpage,name="mysecondpage"),
    path('mythirdpage', views.mythirdpage, name="mythirdpage"),
    path('myimagepage', views.myimagepage, name="myimagepage"),
    path('myimagepage2', views.myimagepage2, name="myimagepage2"),
    path('myimagepage3', views.myimagepage3, name="myimagepage4"),
    path('myimagepage4', views.myimagepage4, name="myimagepage4"),
    path('myimagepage5/<str:imagename>', views.myimagepage5, name="myimagepage5"),
    path('myform', views.myform, name="myform"),
    path('submitform', views.submitform, name="submitform"),
    path('myform2', views.myform2, name="myform2"),

]
