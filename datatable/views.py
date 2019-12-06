from django.shortcuts import render
from django.shortcuts import redirect
from login.views import check_login,check_admin
from datatable.models import Userback
from login.models import User
from chart.alert import get_alertInfo,show_alertInfo
import chart.views
import time
import datetime
import chart.mysql 
import hashlib

@check_login
def datauser(request):
    if request.method == "POST":
        color=request.POST.get("color",None)
        username=request.session.get("user")
        db=User.objects.get(username=username)
        db.maincolor=color
        db.save()
        request.session["maincolor"]=color
    lv=chart.views.is_login(request)
    if lv==1:
        username=request.session.get("user")
        color=request.session.get("maincolor")
        maincolor="/static/datatable/css/maincolor_"+color+".css"
        maincolor_img="/static/datatable/img/"+color+".png"
        imgpath="/static/datatable/img/"+username+".jpg"
        alertmsg=get_alertInfo(10)
    return render(request,"datatable/datauser.html",locals())


@check_login
def datatable(request):
    lv=chart.views.is_login(request)
    if lv==1:
        username=request.session.get("user")
        maincolor=request.session.get("maincolor")
        maincolor="/static/datatable/css/maincolor_"+maincolor+".css"
    return render(request,"datatable/datatable.html",locals())

def databack(request):
    lv=chart.views.is_login(request)
    if lv==1:
        username=request.session.get("user")
        maincolor=request.session.get("maincolor")
        maincolor="/static/datatable/css/maincolor_"+maincolor+".css"
    if request.method == "POST":
        teltype=request.POST.get("teltype",None)
        tel=request.POST.get("tel",None)
        msg=request.POST.get("msg",None)
        questiontype=request.POST.get("questiontype",None)
        nowtime=time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
        Userback.objects.create(teltype=teltype,tel=tel,msg=msg,questiontype=questiontype,time=nowtime)
        len=Userback.objects.count()
        if len == 0:
            print("null")
        else:
            if len > 4:
                len=4
            databack=Userback.objects.all().order_by('time')[0:len]
            for i in range(0,len):
                print("teltype:"+databack[i].teltype+"\ntel:"+databack[i].tel+"\nmsg:"+databack[i].msg+"\nquestiontype:"+databack[i].questiontype+"\ntime:"+databack[i].time+"\nid:"+str(databack[i].id))
    return render(request,"datatable/databack.html",locals())

@check_login
def datainput(request):
    if request.method == "POST":
        event=request.POST.get("eventtype",None)
        timein=request.POST.get("time",None)
        timein=timein.replace("T"," ")
        timenow=datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        community=request.POST.get("community",None)
        unit=request.POST.get("unit",None)
        way=request.POST.get("way",None)
        src=request.POST.get("src",None)
        chart.mysql.data_insert(community,unit,way,src,event,timein)    

    lv=chart.views.is_login(request)
    if lv==1:
        maincolor=request.session.get("maincolor")
        username=request.session.get("user")
        maincolor="/static/datatable/css/maincolor_"+maincolor+".css"
    timenow=datetime.datetime.now().strftime('%Y-%m-%dT%H:%M:%S')
    return render(request,"datatable/datainput.html",locals())


@check_login
def dataalert(request):
    if request.method == "POST":
        event=request.POST.get("event",None)
        id=request.POST.get("id",None)
        id=id.split("_",1)[1]
        connection,db=chart.mysql.database_connect()
        if event=="deal":
            sql="Update data set OVERTIME_ARCHIVE_NUM=0,INTIME_ARCHIVE_NUM=1 where id="+id
            db.execute(sql)
            connection.close()        
        elif event=="over":
            sql="Update data set INTIME_TO_ARCHIVE_NUM=0,INTIME_ARCHIVE_NUM=1 where id="+id
            db.execute(sql)
            connection.close()        
        elif event=="timeout":
            sql="Update data set OVERTIME_ARCHIVE_NUM=1,INTIME_TO_ARCHIVE_NUM=0 where id="+id
            db.execute(sql)
            connection.close()
    lv=chart.views.is_login(request)
    if lv==1:
        maincolor=request.session.get("maincolor")
        username=request.session.get("user")
        maincolor="/static/datatable/css/maincolor_"+maincolor+".css"
        data=show_alertInfo(10)
    return render(request,"datatable/dataalert.html",locals())

@check_admin
def adminuser(request):
    if request.method == "POST":
        event=request.POST.get("event",None)
        id=request.POST.get("id",None)
        id=id.split("_",1)[1]
        print(event,id)
        connection,db=chart.mysql.database_connect()
        if event=="delete":
            sql="DELETE from user where id ="+id
            db.execute(sql)
            connection.close()
        if event=="pass":
            sql="Update user set checked=1 where id ="+id
            db.execute(sql)
            connection.close()
        if event=="changepsw":
            psw=request.POST.get("psw",None)
            psw = hashlib.md5(psw.encode(encoding='utf-8'))
            psw = psw.hexdigest()
            sql="Update user set password=\'"+psw+"\' where id ="+id
            db.execute(sql)
            connection.close()        
        if event=="changeusername":
            name=request.POST.get("name",None)
            sql="Update user set username=\'"+name+"\' where id ="+id
            db.execute(sql)
            connection.close()
    connection,db=chart.mysql.database_connect()
    sql="SELECT username,id FROM user WHERE checked=0"
    len=db.execute(sql)
    value=db.fetchall()
    data=[]
    if len>0:
        for mem in value:
            dic={}
            dic["username"]=mem[0]
            dic["id"]="user_"+str(mem[1])
            dic["type"]=0
            data.append(dic)
    sql="SELECT username,id FROM user WHERE checked=1"
    len=db.execute(sql)
    value=db.fetchall()
    if len>0:
        for mem in value:
            dic={}
            dic["username"]=mem[0]
            dic["id"]="user_"+str(mem[1])
            dic["type"]=1
            data.append(dic)
    connection.close()
    return render(request,"datatable/adminuser.html",locals())

def nofound(request):
    return render(request,"404.html",locals())
