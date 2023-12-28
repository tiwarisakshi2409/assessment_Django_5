from django.shortcuts import render,redirect
from .models import Signup,Event,Notice,Login
from django.conf import settings
from django.core.mail import send_mail
import random

# Create your views here.

def signup(request):
    if request.method=="POST":
        try:
            Signup.objects.get(email=request.POST['email'])
            msg="Email Already Registered"
            return render(request,'signup.html',{'msg':msg})
        except:
            
                Signup.objects.create(
                    name=request.POST['name'],
                    flatno=request.POST['flatno'],
                    members=request.POST['members'],
                    email=request.POST['email'],
                    mobile=request.POST['mobile'],
                    password=request.POST['password'],
                )
                msg="User SIGNUP Successfully"
                return render(request,'login.html',{'msg':msg})

    else:
        return render(request,'login.html')

def adminlogins(request):
    if request.method == "POST":
        email = request.POST['email']
        password = request.POST['password']
        try:
            user = Login.objects.get(email=email)
            if user.password == password:
                request.session['email'] = user.email
                return render(request, 'Adminpannel.html')
            else:
                return render(request, 'Adminlogin.html')
        except Login.DoesNotExist:
            return render(request, 'Adminlogin.html')
        except Exception as e:
            return render(request, 'Adminlogin.html')
    else:
        msg="sscasD"
        return render(request, 'Adminlogin.html')
    
def adminpannel(request):
    return render(request,'Adminpannel.html')

def userlogin(request):
    if request.method == "POST":
        try:
            user = Signup.objects.get(email=request.POST['email'])
            if user.password == request.POST['password']:
                request.session['email'] = user.email
                request.session['name'] = user.name

                return render(request, 'Welcome.html')
            else:
                msg="Incorrect Password"
                return render(request, 'login.html',{'msg':msg})
        except Signup.DoesNotExist:
            msg="Email Not Registered. Please Sign Up."
            return render(request, 'login.html',{'msg':msg})
    else:
        return render(request, 'login.html')
    
def userlogout(request):
        del request.session['email']
        del request.session['name']

        return render(request,'login.html')

def forgot_password(request):
    if request.method=="POST":
        try:
            user= Signup.objects.get(email=request.POST['email'])
            otp=random.randint(1000,9999)
            subject = 'OTP For Forgot Password'
            message = "Hello "+user.name+",Your OTP For Forogt Password Is "+str(otp)
            email_from = settings.EMAIL_HOST_USER
            recipient_list = [user.email,]
            send_mail( subject, message, email_from, recipient_list)
            return render(request,'otp.html',{'otp':otp,'email':user.email})
        except:
            msg="Email Not Registered"
            return render(request,'forgot-password.html',{'msg':msg})
    else:
        return render(request,'forgot-password.html')
    
def verify_otp(request):
    email=request.POST['email']
    otp=int(request.POST['otp'])
    uotp=int(request.POST['uotp'])

    if otp==uotp:
        return render(request,'new-password.html',{'email':email})
    else:
        msg="Invalid OTP"
        return render(request,'otp.html',{'otp':otp,'email':email,'msg':msg})
    
def new_password(request):
    email=request.POST['email']
    np=request.POST['new_password']
    cnp=request.POST['cnew_password']

    if np==cnp:
        user=Signup.objects.get(email=email)
        user.password=np
        user.save()
        msg="Password Updated Successfully"
        return render(request,'login.html',{'msg':msg})
    else:
        msg="Password & Confirm Password Does Not Matched"
        return render(request,'new-password.html',{'email':email,'msg':msg})

def welcome(request):
    return render(request,'Welcome.html')

def adminlogin(request):
    return render(request,'Adminlogin.html')

def notice(request):
    notices=Notice.objects.all()
    return render(request,'noticebrd.html',{'notices':notices})

def event(request):
    events=Event.objects.all()
    return render(request,'events.html',{'events':events})

def adminnotice(request):
    notices=Notice.objects.all()
    return render(request,'adminviewnotic.html',{'notices':notices})

def adminevent(request):
    events=Event.objects.all()
    return render(request,'adminviewevent.html',{'events':events})

def addnotice(request):
    if request.method=="POST":            
        Notice.objects.create(
            title=request.POST['nname'],
            content=request.POST['nmsg'],
        )
        msg="Notice Added Successfully"
        return render(request,'addnotice.html',{'msg':msg})

    else:
        return render(request,'addnotice.html')

def addevent(request):
    if request.method=="POST":            
        Event.objects.create(
            title=request.POST['ename'],
            description=request.POST['emsg'],
        )
        msg="Event Added Successfully"
        return render(request,'addnotice.html',{'msg':msg})
    return render(request,'addevent.html')

