
from django.contrib import messages, auth
from django.core.mail import send_mail

from . models import Childens
from django.http import HttpResponse
from django.shortcuts import render, redirect
from . forms import CreateUserForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout as lgs

# Create your views here.
def homepage(request):
    return render(request,'authen/index.html')

def register(request):

    if request.method=='POST':
        name=request.POST["username"]
        email = request.POST["email"]
        password1= request.POST["password1"]
        password2= request.POST["password2"]
        if password1==password2:
            user=User.objects.create_user(username=name,email=email,password=password2)
            user.save()
            messages.success(request,"yours account has been created")
            return redirect('my_login')
        else:
            messages.warning(request,"Password Mismatch ...!!!")
            return redirect('register')
    else:
        form = CreateUserForm()
        return render(request, 'authen/register.html',{'form':form})

def my_login(request):
    if request.method=='POST':
        username = request.POST["username"]
        password = request.POST["password"]
        user= auth.authenticate(username=username,password=password)

        if user is not None:
            auth.login(request,user)
            return redirect('profile')
        else:
            messages.info(request,'invalid credentials')
            return redirect('my_login')
    else:
        return render(request, 'authen/my-login.html')



@login_required
def profile(request):
    mydata = Childens.objects.all()
    if(mydata!=""):
        return render(request, 'authen/profile.html',{"datas":mydata})
    else:
        return render(request,'authen/profile.html')

def addData(request):
    if request.method=="POST":
        name=request.POST['name']
        rollnumber=request.POST['rollnumber']
        email=request.POST['email']
        atten = request.POST['atten']
        kannada = request.POST['kannada']
        english=request.POST['english']
        maths = request.POST['maths']
        science = request.POST['science']
        social = request.POST['social']
        total=int(kannada)+int(english)+int(maths)+int(science)+int(social)


        obj=Childens()
        obj.name=name
        obj.rollnumber=rollnumber
        obj.email=email
        obj.atten =atten
        obj.kannada = kannada
        obj.english = english
        obj.maths = maths
        obj.science = science
        obj.social = social
        obj.total=total
        obj.save()

        mydata=Childens.objects.all()
        p=total/500 *100
        result=""
        if (int(kannada)>35 and int(english)>35 and int(maths)>35 and int(science)>35 and int(social)>35):
            result="PASS"
        else:
            result="FAIL"
        subject ='HI '+name
        message = f"""Marks obtained in KANNADA= {kannada}\n
        Marks obtained in ENGLISH= {english}\n
        Marks obtained in MATHAMETICS= {maths}\n
        Marks obtained in SCIENCE= {science}\n
        Marks obtained in SOICAL STUDIES= {social}\n
        Total Marks Obtained ={total}\n
        Percentage Obtained ={p}%\n
        Result={result}
        You have attended for {atten} days if that is less than 90 Days you have to submit your Medical Report to your conserned HOD"""
        from_email ='rvd12091998@gmail.com'
        recipient_list = [email]
        send_mail(subject, message, from_email, recipient_list,fail_silently=False)
        return redirect('profile')
    return render(request, 'authen/profile.html')

def updateData(request,rollnumber):
    mydata=Childens.objects.get(rollnumber=rollnumber)
    if request.method=="POST":
        name = request.POST['name']
        rollnumber = request.POST['rollnumber']
        email = request.POST['email']
        atten = request.POST['atten']
        kannada = request.POST['kannada']
        english = request.POST['english']
        maths = request.POST['maths']
        science = request.POST['science']
        social = request.POST['social']
        total = int(kannada) + int(english) + int(maths) + int(science) + int(social)

        mydata.name=name
        mydata.rollnumber=rollnumber
        mydata.email=email
        mydata.atten = atten
        mydata.kannada = kannada
        mydata.english = english
        mydata.maths = maths
        mydata.science = science
        mydata.social = social
        mydata.total=total
        mydata.save()
        return redirect('profile')
    return render(request, 'authen/update.html',{'data':mydata})

def deleteData(request,rollnumber):
    mydata=Childens.objects.get(rollnumber=rollnumber)
    mydata.delete()
    return redirect('profile')

def student(request):
    mydata = Childens.objects.all()
    return render(request,'authen/student.html',{"datas":mydata})

def viewData(request,rollnumber):
    mydata=Childens.objects.get(rollnumber=rollnumber)
    return render(request, 'authen/stdlogin.html',{'datas':mydata})

def stdlogin(request,rollnumber):
    mydata = Childens.objects.get(rollnumber=rollnumber)
    if request.method=='POST':
        email = request.POST["email"]
        if mydata.email==email:
            return render(request,'authen/view.html',{'datas':mydata})
        else:
            messages.warning(request,"Password Mismatch ...!!!")
            return redirect('stdlogin',rollnumber=rollnumber)
    else:
        return render(request, 'authen/stdlogin.html',{'datas':mydata})

def logout(request):
    if request.method=="POST":
        lgs(request)
        return redirect('homepage')

def teacher(request):
    p="admin"
    if request.method == 'POST':
        password = request.POST["password"]
        if p == password:
            return render(request, 'authen/my-login.html')
        else:
            messages.warning(request, "Password Mismatch ...!!!")
            return redirect('teacher')
    else:
        return render(request, 'authen/teacher.html')