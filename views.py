from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView

#from myproject.myfirstapp.forms import FeedbackForm


# Create your views here.
def index(request):
    return HttpResponse("Hello")

def about(request):
    return HttpResponse("this is the about page")

def sum(request,a,b):
    return HttpResponse(a+b)

def introduction(request,name,age):
    return HttpResponse("Hello" + name +"your age is " + str(age))

def myfirstpage(request):
    return render(request,'index.html')

def mysecondpage(request):
    return render(request,'second.html')

def mythirdpage(request):
    name = "Ram"
    animals = ["Dog","Cat","Cow"]
    num1=10
    num2=20
    flag = num1>num2
    mydictionary = {"name":name,"animals":animals,"flag":flag,"num1":num1,"num2":
                    num2}

    return render(request,'third.html',context=mydictionary)

def myimagepage(request):
    return render (request,'imagefile.html')

def myimagepage2(request):
    return render (request,'imagefile2.html')

def myimagepage3(request):
    return render (request,'imagefile3.html')

def myimagepage4(request):
    return render (request,'imagefile4.html')

def myimagepage5(request,imagename):
    img_name = str(imagename).lower()
    if img_name == "django":
        flag = True
    elif img_name == "python":
        flag = False
    mydictionary ={
        "flag":flag
    }
    return render (request,'imagefile5.html',context=mydictionary)

def myform(request):
    return render(request,'myform.html')




def submitform(request):
    if request.method == "GET":
        mydictionary = {
            "method": request.method,
            "mytext": request.GET['mytext'],
            "mytextarea": request.GET['mytextarea']


        }
    else:
        mydictionary = {
            "method": request.method,
            "mytext": request.POST['mytext'],
            "mytextarea": request.POST['mytextarea']
        }


    return JsonResponse(mydictionary)


def myform2(request):
    if request.method == "GET":
        form = FeedbackForm()
        mydictionary={
            "form":form}
    elif request.method == "POST":
        pass

    return render('myform2.html',context=mydictionary)







