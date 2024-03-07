from django.shortcuts import render
from django.core.mail import message
from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
# below import is done for sending emails
from django.conf import settings
from django.core.mail import send_mail
from django.core import mail
from django.core.mail.message import EmailMessage

from .models import Entry1
from django.contrib.auth.decorators import login_required


# Create your views here.
def index(request):
    return render(request,'index.html')

def about(request):
    return render(request,'about.html')

def contact(request):
    return render(request,'contact.html')

def form(request):
    return render(request,'form.html')

def Signin(request):
    if request.method=="POST":
        uname=request.POST.get("username")
        email=request.POST.get("email")
        password=request.POST.get("pass1")
        confirmpassword=request.POST.get("pass2")
        # print(uname,email,password,confirmpassword)
        if password!=confirmpassword:
            messages.warning(request,"Password is Incorrect")
            return redirect('/Signin')


        try:
            if User.objects.get(username=uname):
                messages.info(request,"UserName Is Taken")
                return redirect('/Signin')
        except:
            pass
        try:
            if User.objects.get(email=email):
                messages.info(request,"Email Is Taken")
                return redirect('/Signin')
        except:
            pass
    
        myuser=User.objects.create_user(uname,email,password)
        myuser.save()
        messages.success(request,"Signup Success Please login!")
        return redirect('/login')
    return render(request,'Signin.html')

def handlelogin(request):
    if request.method=="POST":
        uname=request.POST.get("username")
        pass1=request.POST.get("pass1")
        myuser=authenticate(username=uname,password=pass1)
        if myuser is not None:
            login(request,myuser)
            messages.success(request,"Login Success")
            return redirect('/welcome')
        else:
            messages.error(request,"Invalid Credentails")
            return redirect('/login')
    return render(request,'login.html')

@login_required
def projects(request):
    user = request.user
    projects = Entry1.objects.filter(author=user)  # Filter by logged-in user

    context = {'projects': projects}
    return render(request, 'welcome.html', context)

def submit_project(request):
    if request.method == 'POST':
        #form = EntryForm(request.POST, request.FILES)
        name = request.POST.get('title')
        desc = request.POST.get('description')
        author1 = request.user
        if name and desc:
            model_instance = Entry1(title=name, description=desc,author=author1)
            model_instance.save()
            messages.success(request,"Published Succeessfully")
            return redirect('projects')
        #if form.is_valid():
            #form.save()
            #return redirect('/')  # Replace with your success URL
        else:
            messages.error(request,"Please fill all the fields")
    
    #context = {'form': form}
    return render(request, 'form.html')