from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponse
from login.models import User
import pymysql
import hashlib
import os
import re

def check_login(func):
    def inner(*args, **kwargs):
        #判断是否登录
        name = args[0].session.get("user", None)
        if name == None:
            args[0].session["login"]="null"
            return redirect('login')
        hash = args[0].session.get("login", None)
        if hash == None:
            args[0].session["login"]="null"
            return redirect('login')
        if hash != hashlib.md5(name.encode(encoding='utf-8')).hexdigest():
            args[0].session["login"]="null"
            return redirect('login')
        return func(*args, **kwargs)

    return inner



def check_admin(func):
    def inner(*args, **kwargs):
        #判断是否登录
        admin = args[0].session.get("admin", None)
        psw="root_mysql"
        psw = hashlib.md5(psw.encode(encoding='utf-8'))
        psw = psw.hexdigest()
        if admin!=psw:
            args[0].session["admin"]="null"
            return redirect('useradmin_login')
        return func(*args, **kwargs)

    return inner



# Create your views here.
def login(request):
    if request.method == "POST":
        name = request.POST.get("username",None)
        psw = request.POST.get("password",None)
        code= request.POST.get("code",None)
        if code == "":
            return render(request,"login/login.html",locals())
        psw = hashlib.md5(psw.encode(encoding='utf-8'))
        psw = psw.hexdigest()
        try:
            db = User.objects.get(username=name)
        except:
            msg = "用户不存在"
            return render(request,"login/login.html",locals())
        if db.checked == 0:
            msg = "请等待管理员审核您的账号"
            return render(request,"login/login.html",locals())
        if db.password == psw:
            msg = "Welcome"
            request.session["login"] = hashlib.md5(name.encode(encoding='utf-8')).hexdigest()
            request.session["user"] = name

            maincolor = db.maincolor
            print(maincolor)
            if maincolor=="":
                maincolor="blue"
                db.maincolor=maincolor
                db.save()
            request.session["maincolor"]=maincolor
            return redirect(r"/chart_mymap")
        msg = "密码错误"
    if request.session.get("login")=="null":
        del request.session["login"]
        msg = "尚未登录，请先登陆后再访问"    
    if request.session.get("login")=="changepsw":
        del request.session["login"]
        msg = "修改密码成功,请重新登录！"    
    if request.session.get("login")=="success":
        del request.session["login"]
        msg = "注册成功,请登录！"
    return render(request,"login/login.html",locals())



def register(request):
    if request.method == "POST":
        name = request.POST.get("username",None)
        psw = request.POST.get("password",None)
        psw2 = request.POST.get("password_check",None)
        code = request.POST.get("code",None)
        if code == "":
            return render(request,"login/register.html",locals())
        count = User.objects.filter(username=name).count()
        if count != 0:
            msg="用户已存在"
            return render(request,"login/register.html",locals())

        if len(psw)<6:
            print("err 01")
            msg="密码中必须有数字，英文字母，数字键上符号，长度不低于6，您的密码长度小于6"
            return render(request,"login/register.html",locals())
        if (re.search("[a-z]",psw) == None and re.search("[A-Z]",psw) == None) or re.search("[1-9]",psw) == None:
            msg="密码中必须有数字，英文字母，长度不低于6，您的密码没有满足限制"
            return render(request,"login/register.html",locals())

        if psw!=psw2:
            msg="两次输入的密码不相同"
            return render(request,"login/register.html",locals())

        psw = hashlib.md5(psw.encode(encoding='utf-8'))
        psw = psw.hexdigest()
        User.objects.create(username=name,password=psw,checked=0)
        request.session["login"]="success"
        return redirect(r"login")
    return render(request,"login/register.html",locals())


@check_login
def changepsw(request):
    name = request.session.get("user")
    if request.method == "POST":
        psw0 = request.POST.get("password_old",None)
        psw = request.POST.get("password",None)
        psw2 = request.POST.get("password_check",None)
        code = request.POST.get("code",None)
        if code == "":
            return render(request,"login/changepsw.html",locals())
        db = User.objects.get(username=name)
        psw0 = hashlib.md5(psw0.encode(encoding='utf-8'))
        psw0 = psw0.hexdigest()
        if db.password != psw0:
            msg = "原始密码错误，如忘记密码请联系管理员"
            return render(request,"login/changepsw.html",locals())
        if len(psw)<6:
            print("err 01")
            msg="密码中必须有数字，英文字母，数字键上符号，长度不低于6，您的密码长度小于6"
            return render(request,"login/changepsw.html",locals())
        if (re.search("[a-z]",psw) == None and re.search("[A-Z]",psw) == None) or re.search("[1-9]",psw) == None:
            msg="密码中必须有数字，英文字母，长度不低于6，您的密码没有满足限制"
            return render(request,"login/changepsw.html",locals())
        if psw!=psw2:
            msg = "两次密码输入不同"
            return render(request,"login/changepsw.html",locals())
        psw = hashlib.md5(psw.encode(encoding='utf-8'))
        psw = psw.hexdigest()
        db.password=psw
        db.save()
        request.session.flush()
        request.session["login"]="changepsw"
        return redirect("login")
    return render(request,"login/changepsw.html",locals())


def logout(request):
    request.session.flush()
    return redirect(r"/")


def adminlogin(request):
    if request.method == "POST":
        name = request.POST.get("username",None)
        psw = request.POST.get("password",None)
        code= request.POST.get("code",None)
        if code == "":
            return render(request,"login/adminlogin.html",locals())
        if name!="root" or psw != "19990610YYF@mysql":
            msg="用户名或密码错误"
            return render(request,"login/adminlogin.html",locals())
        psw="root_mysql"
        psw = hashlib.md5(psw.encode(encoding='utf-8'))
        psw = psw.hexdigest()
        request.session["admin"]=psw
        return redirect("adminuser")
    if request.session.get("admin")=="null":
        del request.session["admin"]
        msg = "尚未登录，请先登陆后再访问"    
    return render(request,"login/adminlogin.html",locals())



def nofound(request):
    return render(request,"404.html",locals())