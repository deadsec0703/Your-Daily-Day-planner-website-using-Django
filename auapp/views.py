from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from auth_email_project.settings import EMAIL_HOST_USER
from django.core.mail import send_mail
from random import randrange

def user_signup(request):
    if request.method == "POST":
        loc = request.POST.get("loc")
        na = request.POST.get("na")
        un = request.POST.get("un")
        em = request.POST.get("em")
        try:
            usr = User.objects.get(username=un)
            return render(request, "user_signup.html", {"msg":"username already registered"})
        
        except User.DoesNotExist:
            try:
                usr = User.objects.get(email=em)
                return render(request,"user_signup.html",{"msg":"email already registered"})
            except User.DoesNotExist:
                pw = ""
                text = '123456789'
                for i in range(6):
                    pw = pw + text[randrange(len(text))]
                print(pw)
                msg = "your password is " + pw
                send_mail("welcome to QuickPlan by Soham Vaidya", msg, EMAIL_HOST_USER, [str(em)])
                usr = User.objects.create_user(username=un,password=pw,email=em)
                usr.save()
                return redirect("user_login")
    else:
        return render(request,"user_signup.html")


def user_login(request):
    if request.method == "POST":
        un = request.POST.get("un")
        pw = request.POST.get("pw")
        usr = authenticate(username=un, password=pw)
        if usr is None:
            return render(request, "user_login.html",{"msg":"login denied"})
        else:
            login(request,usr)
            return redirect("home")
    else:
        return render(request,"user_login.html")

def user_logout(request):
    logout(request)
    return redirect("user_login")

def user_rp(request):
    if request.method == "POST":
        un = request.POST.get("un")
        em = request.POST.get("em")
        try:
            usr = User.objects.get(username=un) and User.objects.get(email=em)
            pw = ""
            text = "123456789"
            for i in range(6):
                pw = pw + text[randrange(len(text))]
            print(pw)
            msg = "your new password is " + pw
            send_mail("welcome to QuickPlan by Soham Vaidya",msg, EMAIL_HOST_USER,[str(em)])
            usr.set_password(pw)
            usr.save()
            return redirect("user_login")
        except User.DoesNotExist:
            return render(request, "user_rp.html", {"msg":"invalid info"})
    
    else:
        return render(request, "user_rp.html")

def main(request):
    return render(request,"main.html")
