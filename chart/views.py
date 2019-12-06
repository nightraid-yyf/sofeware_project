from django.shortcuts import render
from django.http import HttpResponse
from django.http.response import JsonResponse
import chart.mysql
import chart.alert
import hashlib


# Create your views here.
mymap=[]
mychart1data=[]
mychart2data=[]
mychart3data=[]
def is_login(request):
    name = request.session.get("user", None)
    if name == None:
        return 0
    hash = request.session.get("login", None)
    if hash == None:
        request.session["login"]="null"
        return 0
    if hash != hashlib.md5(name.encode(encoding='utf-8')).hexdigest():
        request.session["login"]="null"
        return 0
    return 1

def chart_mymap(request):
    if request.session.get("login")=="null":
        alert = 1
        print(request.session.get("login"))
        del request.session["login"]
    else:
        alert = 0
    if request.method == "POST":
        if(request.POST.get("reset_but",None)=="reset"):
            request.session["start_time"]="2018-02-08"
            request.session["end_time"]="2018-12-01"
            request.session["time_request"]=1
        else:
            type=request.POST.get("submit_btn",None)
            if type=="day":
                request.session["start_time"]=request.POST.get("start_time",None)
                request.session["end_time"]=request.POST.get("end_time",None)
                request.session["time_request"]=1
            elif type=="month":
                start_time=request.POST.get("start_time",None)
                request.session["start_time"]=start_time
                start_time=start_time.split("-",2)
                start_time[1]=int(start_time[1])+1
                if start_time[1]<10:
                    start_time[1]="0"+str(start_time[1])
                elif start_time[1]>12:
                    start_time[1]=start_time[1]-12
                    if start_time[1]<10:
                        start_time[1]="0"+str(start_time[1])
                    start_time[0]=str((int(start_time[0])+1))
                else:
                    start_time[1]=str(start_time[1])
                end_time=start_time[0]+"-"+start_time[1]+"-"+start_time[2]
                request.session["end_time"]=end_time
                request.session["time_request"]=1
            else:
                start_time=request.POST.get("start_time",None)
                request.session["start_time"]=start_time
                start_time=start_time.split("-",2)
                start_time[1]=int(start_time[1])+3
                if start_time[1]<10:
                    start_time[1]="0"+str(start_time[1])
                elif start_time[1]>12:
                    start_time[1]=start_time[1]-12
                    if start_time[1]<10:
                        start_time[1]="0"+str(start_time[1])
                    start_time[0]=str((int(start_time[0])+1))
                else:
                    start_time[1]=str(start_time[1])
                end_time=start_time[0]+"-"+start_time[1]+"-"+start_time[2]
                request.session["end_time"]=end_time
                request.session["time_request"]=1
    if(request.session.get("start_time")==None):
        request.session["start_time"]="2018-02-08"
        request.session["end_time"]="2018-12-01"
    if (request.session.get("from")==None):
        request.session["from"]="chart_mymap"
    else:
        if(request.session.get("from")!="chart_mymap"):
            request.session["from"]="chart_mymap"
            try:
                if(request.session.get("mymapdata")[0]["start_time"]!=request.session.get("start_time")) or (request.session.get("mymapdata")[0]["end_time"]!=request.session.get("end_time")):
                    request.session["time_request"]=1
            except:
                request.session["time_request"]=0
    start_time=request.session.get("start_time")
    end_time=request.session.get("end_time")
    lv=is_login(request)
    if lv==1:
        username=request.session.get("user")
        maincolor=request.session.get("maincolor")
        maincolor="/static/chart/datatable/css/maincolor_"+maincolor+".css"
        alertmsg=chart.alert.get_alertInfo(10)
    return render(request,"chart/chart_mymap.html",locals())


def myMap(request):
    global mymap
    connection,db = chart.mysql.database_connect()
    db=chart.mysql.Testconnect(db,connection)
    if (mymap==[]) or (request.session.get("mymapdata")!=None and (mymap[0]['version']!=chart.mysql.GetVersion(db))):
        sql = "SELECT COMMUNITY_NAME FROM website.data Group by COMMUNITY_NAME"
        len=db.execute(sql)
        name = db.fetchall()
        mymap=[{'version':chart.mysql.GetVersion(db),'time_request':0,'start_time':request.session.get("start_time"),'end_time':request.session.get("end_time")}]
        for i in range(0,len):
            sql = "SELECT COMMUNITY_NAME FROM website.data Where COMMUNITY_NAME=\""+name[i][0]+"\""
            value = db.execute(sql)
            mymap.append({'name':name[i][0],'value':value})
            request.session["time_request"]=1
    if request.session.get("mymapdata")==None:
        request.session["mymapdata"]=mymap
    if request.session.get("time_request")==1:
        start_time=request.session.get("start_time")
        end_time=request.session.get("end_time")
        end_time=end_time.split("-",2)
        end_time[2]=int(end_time[2])+1
        if(end_time[2]<10):
            end_time[2]="0"+str(end_time[2])
        else:
            end_time[2]=str(end_time[2])
        end_time=end_time[0]+"-"+end_time[1]+"-"+end_time[2]
        request.session["time_request"]=2
        sql = "SELECT COMMUNITY_NAME FROM website.data where COMMUNITY_NAME IN (SELECT COMMUNITY_NAME FROM website.data WHere CREATE_TIME > \""+start_time+"\" and CREATE_TIME < \""+end_time+"\") Group by COMMUNITY_NAME"
        len=db.execute(sql)
        name = db.fetchall()
        mymap2=[{'version':chart.mysql.GetVersion(db),'time_request':1,'start_time':request.session.get("start_time"),'end_time':request.session.get("end_time")}]
        for i in range(0,len):
            sql = "SELECT COMMUNITY_NAME FROM website.data Where COMMUNITY_NAME=\""+name[i][0]+"\" and id IN (SELECT id FROM website.data WHere CREATE_TIME > \""+start_time+"\" and CREATE_TIME < \""+end_time+"\")"
            value = db.execute(sql)
            mymap2.append({'name':name[i][0],'value':value})
        request.session["mymapdata"]=mymap2
        chart.mysql.database_close(connection,db)
        return JsonResponse(request.session.get("mymapdata"),safe=False)
    if request.session.get("time_request")==2:
        request.session["time_request"]=0
        mymap2 = request.session.get("mymapdata")
        mymap2[0]['time_request']=0
        request.session["mymapdata"]=mymap2
    chart.mysql.database_close(connection,db)
    return JsonResponse(request.session.get("mymapdata"),safe=False)

def chart_mychart1(request):
    if request.method == "POST":
        if(request.POST.get("reset_but",None)=="reset"):
            request.session["start_time"]="2018-02-08"
            request.session["end_time"]="2018-12-01"
            request.session["time_request"]=1
        else:
            type=request.POST.get("submit_btn",None)
            if type=="day":
                request.session["start_time"]=request.POST.get("start_time",None)
                request.session["end_time"]=request.POST.get("end_time",None)
                request.session["time_request"]=1
            elif type=="month":
                start_time=request.POST.get("start_time",None)
                request.session["start_time"]=start_time
                start_time=start_time.split("-",2)
                start_time[1]=int(start_time[1])+1
                if start_time[1]<10:
                    start_time[1]="0"+str(start_time[1])
                elif start_time[1]>12:
                    start_time[1]=start_time[1]-12
                    if start_time[1]<10:
                        start_time[1]="0"+str(start_time[1])
                    start_time[0]=str((int(start_time[0])+1))
                else:
                    start_time[1]=str(start_time[1])
                end_time=start_time[0]+"-"+start_time[1]+"-"+start_time[2]
                request.session["end_time"]=end_time
                request.session["time_request"]=1
            else:
                start_time=request.POST.get("start_time",None)
                request.session["start_time"]=start_time
                start_time=start_time.split("-",2)
                start_time[1]=int(start_time[1])+3
                if start_time[1]<10:
                    start_time[1]="0"+str(start_time[1])
                elif start_time[1]>12:
                    start_time[1]=start_time[1]-12
                    if start_time[1]<10:
                        start_time[1]="0"+str(start_time[1])
                    start_time[0]=str((int(start_time[0])+1))
                else:
                    start_time[1]=str(start_time[1])
                end_time=start_time[0]+"-"+start_time[1]+"-"+start_time[2]
                request.session["end_time"]=end_time
                request.session["time_request"]=1

    if(request.session.get("start_time")==None):
        request.session["start_time"]="2018-02-08"
        request.session["end_time"]="2018-12-01"
    if (request.session.get("from")==None):
        request.session["from"]="chart_mychart1"
    else:
        if(request.session.get("from")!="chart_mychart1"):
            request.session["from"]="chart_mychart1"
            try:
                if(request.session.get("mychart1data")[0]["start_time"]!=request.session.get("start_time")) or (request.session.get("mychart1data")[0]["end_time"]!=request.session.get("end_time")):
                    request.session["time_request"]=1
            except:
                request.session["time_request"]=0
    start_time=request.session.get("start_time")
    end_time=request.session.get("end_time")
    lv=is_login(request)
    if lv==1:
        username=request.session.get("user")
        maincolor=request.session.get("maincolor")
        maincolor="/static/chart/datatable/css/maincolor_"+maincolor+".css"
        alertmsg=chart.alert.get_alertInfo(10)
    return render(request,"chart/chart_mychart1.html",locals())

def mychart1(request):
    global mychart1data
    connection,db = chart.mysql.database_connect()
    db=chart.mysql.Testconnect(db,connection)
    if (mychart1data==[]) or (request.session.get("mychart1data")!=None and (mychart1data[0]['version']!=chart.mysql.GetVersion(db))):
        sql = "SELECT MAIN_TYPE_NAME FROM website.data Group by MAIN_TYPE_NAME"
        len = db.execute(sql)
        name = db.fetchall()
        sql = "SELECT STREET_NAME FROM website.data Group by STREET_NAME"
        len_street = db.execute(sql)
        street = db.fetchall()
        mychart1data=[{'version':chart.mysql.GetVersion(db),'time_request':1,'start_time':request.session.get("start_time"),'end_time':request.session.get("end_time")}]
        for i in range(0,len):
            sql = "SELECT EVENT_TYPE_NAME FROM website.data Where MAIN_TYPE_NAME=\""+name[i][0]+"\" group by EVENT_TYPE_NAME"
            db.execute(sql)
            stack=db.fetchall()
            value=[]
            for j in range(0,len_street):
                sql = "SELECT MAIN_TYPE_NAME FROM website.data Where MAIN_TYPE_NAME=\""+name[i][0]+"\" and STREET_NAME=\""+street[j][0]+"\""
                value.append(db.execute(sql))
            mychart1data.append({'name':name[i][0],'type':'bar','stack':stack[0][0],'data':value})
            request.session["time_request"]=1

    if request.session.get("mychart1data")==None:
        request.session["mychart1data"]=mychart1data

    if request.session.get("time_request")==1:
        start_time=request.session.get("start_time")
        end_time=request.session.get("end_time")
        end_time=end_time.split("-",2)
        end_time[2]=int(end_time[2])+1
        if(end_time[2]<10):
            end_time[2]="0"+str(end_time[2])
        else:
            end_time[2]=str(end_time[2])
        end_time=end_time[0]+"-"+end_time[1]+"-"+end_time[2]
        request.session["time_request"]=2
        sql = "SELECT MAIN_TYPE_NAME FROM website.data where MAIN_TYPE_NAME IN (SELECT MAIN_TYPE_NAME FROM website.data WHere CREATE_TIME > \""+start_time+"\" and CREATE_TIME < \""+end_time+"\") Group by MAIN_TYPE_NAME"
        len = db.execute(sql)
        name = db.fetchall()
        sql = "SELECT STREET_NAME FROM website.data where STREET_NAME IN (SELECT STREET_NAME FROM website.data WHere CREATE_TIME > \""+start_time+"\" and CREATE_TIME < \""+end_time+"\") Group by STREET_NAME"
        len_street = db.execute(sql)
        street = db.fetchall()
        mychart1data2=[{'version':chart.mysql.GetVersion(db),'time_request':1,'start_time':request.session.get("start_time"),'end_time':request.session.get("end_time")}]
        for i in range(0,len):
            sql = "SELECT EVENT_TYPE_NAME FROM website.data Where MAIN_TYPE_NAME=\""+name[i][0]+"\" group by EVENT_TYPE_NAME"
            db.execute(sql)
            stack=db.fetchall()
            value=[]
            for j in range(0,len_street):
                sql = "SELECT MAIN_TYPE_NAME FROM website.data Where MAIN_TYPE_NAME=\""+name[i][0]+"\" and STREET_NAME=\""+street[j][0]+"\" and id IN (SELECT id FROM website.data WHere CREATE_TIME > \""+start_time+"\" and CREATE_TIME < \""+end_time+"\")"
                value.append(db.execute(sql))
            mychart1data2.append({'name':name[i][0],'type':'bar','stack':stack[0][0],'data':value})
            request.session["mychart1data"]=mychart1data2

    if request.session.get("time_request")==2:
        request.session["time_request"]=0
        mychart1data2 = request.session.get("mychart1data")
        mychart1data2[0]['time_request']=0
        request.session["mychart1data"]=mychart1data2
        request.session["mychart1data"]=mychart1data2
    chart.mysql.database_close(connection,db)
    return JsonResponse(request.session.get("mychart1data"),safe=False)

def chart_mychart2(request):
    if request.method == "POST":
        if(request.POST.get("reset_but",None)=="reset"):
            request.session["start_time"]="2018-02-08"
            request.session["end_time"]="2018-12-01"
            request.session["time_request"]=1
        else:
            type=request.POST.get("submit_btn",None)
            if type=="day":
                request.session["start_time"]=request.POST.get("start_time",None)
                request.session["end_time"]=request.POST.get("end_time",None)
                request.session["time_request"]=1
            elif type=="month":
                start_time=request.POST.get("start_time",None)
                request.session["start_time"]=start_time
                start_time=start_time.split("-",2)
                start_time[1]=int(start_time[1])+1
                if start_time[1]<10:
                    start_time[1]="0"+str(start_time[1])
                elif start_time[1]>12:
                    start_time[1]=start_time[1]-12
                    if start_time[1]<10:
                        start_time[1]="0"+str(start_time[1])
                    start_time[0]=str((int(start_time[0])+1))
                else:
                    start_time[1]=str(start_time[1])
                end_time=start_time[0]+"-"+start_time[1]+"-"+start_time[2]
                request.session["end_time"]=end_time
                request.session["time_request"]=1
            else:
                start_time=request.POST.get("start_time",None)
                request.session["start_time"]=start_time
                start_time=start_time.split("-",2)
                start_time[1]=int(start_time[1])+3
                if start_time[1]<10:
                    start_time[1]="0"+str(start_time[1])
                elif start_time[1]>12:
                    start_time[1]=start_time[1]-12
                    if start_time[1]<10:
                        start_time[1]="0"+str(start_time[1])
                    start_time[0]=str((int(start_time[0])+1))
                else:
                    start_time[1]=str(start_time[1])
                end_time=start_time[0]+"-"+start_time[1]+"-"+start_time[2]
                request.session["end_time"]=end_time
                request.session["time_request"]=1
    if(request.session.get("start_time")==None):
        request.session["start_time"]="2018-02-08"
        request.session["end_time"]="2018-12-01"
    if (request.session.get("from")==None):
        request.session["from"]="chart_mychart2"
    else:
        if(request.session.get("from")!="chart_mychart2"):
            request.session["from"]="chart_mychart2"
            try:
                if(request.session.get("mychart2data")[0]["start_time"]!=request.session.get("start_time")) or (request.session.get("mychart2data")[0]["end_time"]!=request.session.get("end_time")):
                    request.session["time_request"]=1
            except:
                request.session["time_request"]=0
    start_time=request.session.get("start_time")
    end_time=request.session.get("end_time")
    lv=is_login(request)
    if lv==1:
        username=request.session.get("user")
        maincolor=request.session.get("maincolor")
        maincolor="/static/chart/datatable/css/maincolor_"+maincolor+".css"
        alertmsg=chart.alert.get_alertInfo(10)
    return render(request,"chart/chart_mychart2.html",locals())

def mychart2(request):
    global mychart2data
    connection,db = chart.mysql.database_connect()
    db=chart.mysql.Testconnect(db,connection)
    if (mychart2data==[]) or (request.session.get("mychart2data")!=None and (mychart2data[0]['version']!=chart.mysql.GetVersion(db))):
        sql = "SELECT EVENT_PROPERTY_NAME FROM website.data Group by EVENT_PROPERTY_NAME"
        len = db.execute(sql)
        name = db.fetchall()
        mychart2data=[{'version':chart.mysql.GetVersion(db),'time_request':1,'start_time':request.session.get("start_time"),'end_time':request.session.get("end_time")}]
        for i in range(0,len):
            sql = "SELECT EVENT_PROPERTY_NAME FROM website.data Where EVENT_PROPERTY_NAME=\""+name[i][0]+"\""
            value=db.execute(sql)
            mychart2data.append({'name':name[i][0],'value':value})
            request.session["time_request"]=1

    if request.session.get("mychart2data")==None:
        request.session["mychart2data"]=mychart2data

    if request.session.get("time_request")==1:
        start_time=request.session.get("start_time")
        end_time=request.session.get("end_time")
        end_time=end_time.split("-",2)
        end_time[2]=int(end_time[2])+1
        if(end_time[2]<10):
            end_time[2]="0"+str(end_time[2])
        else:
            end_time[2]=str(end_time[2])
        end_time=end_time[0]+"-"+end_time[1]+"-"+end_time[2]
        request.session["time_request"]=2
        sql = "SELECT EVENT_PROPERTY_NAME FROM website.data where EVENT_PROPERTY_NAME IN (SELECT EVENT_PROPERTY_NAME FROM website.data WHere CREATE_TIME > \""+start_time+"\" and CREATE_TIME < \""+end_time+"\") Group by EVENT_PROPERTY_NAME"
        len = db.execute(sql)
        name = db.fetchall()
        mychart2data2=[{'version':chart.mysql.GetVersion(db),'time_request':1,'start_time':request.session.get("start_time"),'end_time':request.session.get("end_time")}]
        for i in range(0,len):
            sql = "SELECT EVENT_PROPERTY_NAME FROM website.data Where EVENT_PROPERTY_NAME=\""+name[i][0]+"\" and id IN (SELECT id FROM website.data WHere CREATE_TIME > \""+start_time+"\" and CREATE_TIME < \""+end_time+"\")"
            value=db.execute(sql)
            mychart2data2.append({'name':name[i][0],'value':value})
            request.session["mychart2data"]=mychart2data2

    if request.session.get("time_request")==2:
        request.session["time_request"]=0
        mychart2data2 = request.session.get("mychart2data")
        mychart2data2[0]['time_request']=0
        request.session["mychart2data"]=mychart2data2
    chart.mysql.database_close(connection,db)
    return JsonResponse(request.session.get("mychart2data"),safe=False)


def chart_mychart3(request):
    if request.method == "POST":
        if(request.POST.get("reset_but",None)=="reset"):
            request.session["start_time"]="2018-02-08"
            request.session["end_time"]="2018-12-01"
            request.session["time_request"]=1
        else:
            type=request.POST.get("submit_btn",None)
            if type=="day":
                request.session["start_time"]=request.POST.get("start_time",None)
                request.session["end_time"]=request.POST.get("end_time",None)
                request.session["time_request"]=1
            elif type=="month":
                start_time=request.POST.get("start_time",None)
                request.session["start_time"]=start_time
                start_time=start_time.split("-",2)
                start_time[1]=int(start_time[1])+1
                if start_time[1]<10:
                    start_time[1]="0"+str(start_time[1])
                elif start_time[1]>12:
                    start_time[1]=start_time[1]-12
                    if start_time[1]<10:
                        start_time[1]="0"+str(start_time[1])
                    start_time[0]=str((int(start_time[0])+1))
                else:
                    start_time[1]=str(start_time[1])
                end_time=start_time[0]+"-"+start_time[1]+"-"+start_time[2]
                request.session["end_time"]=end_time
                request.session["time_request"]=1
            else:
                start_time=request.POST.get("start_time",None)
                request.session["start_time"]=start_time
                start_time=start_time.split("-",2)
                start_time[1]=int(start_time[1])+3
                if start_time[1]<10:
                    start_time[1]="0"+str(start_time[1])
                elif start_time[1]>12:
                    start_time[1]=start_time[1]-12
                    if start_time[1]<10:
                        start_time[1]="0"+str(start_time[1])
                    start_time[0]=str((int(start_time[0])+1))
                else:
                    start_time[1]=str(start_time[1])
                end_time=start_time[0]+"-"+start_time[1]+"-"+start_time[2]
                request.session["end_time"]=end_time
                request.session["time_request"]=1
    if(request.session.get("start_time")==None):
        request.session["start_time"]="2018-02-08"
        request.session["end_time"]="2018-12-01"
    if (request.session.get("from")==None):
        request.session["from"]="chart_mychart3"
    else:
        if(request.session.get("from")!="chart_mychart3"):
            request.session["from"]="chart_mychart3"
            try:
                if(request.session.get("mychart3data")[0]["start_time"]!=request.session.get("start_time")) or (request.session.get("mychart3data")[0]["end_time"]!=request.session.get("end_time")):
                    request.session["time_request"]=1
            except:
                request.session["time_request"]=0
    start_time=request.session.get("start_time")
    end_time=request.session.get("end_time")
    lv=is_login(request)
    if lv==1:
        username=request.session.get("user")
        maincolor=request.session.get("maincolor")
        maincolor="/static/chart/datatable/css/maincolor_"+maincolor+".css"
        alertmsg=chart.alert.get_alertInfo(10)
    return render(request,"chart/chart_mychart3.html",locals())

def mychart3(request):
    global mychart3data
    connection,db = chart.mysql.database_connect()
    db=chart.mysql.Testconnect(db,connection)
    if (mychart3data==[]) or (request.session.get("mychart3data")!=None and (mychart3data[0]['version']!=chart.mysql.GetVersion(db))):
        sql = "SELECT EVENT_TYPE_NAME FROM website.data Group by EVENT_TYPE_NAME"
        len = db.execute(sql)
        name = db.fetchall()
        mychart3data=[{'version':chart.mysql.GetVersion(db),'time_request':1,'length1':3,'length2':len,'start_time':request.session.get("start_time"),'end_time':request.session.get("end_time")}]
        sql = "SELECT OVERTIME_ARCHIVE_NUM FROM website.data where OVERTIME_ARCHIVE_NUM=1"
        value = db.execute(sql)
        mychart3data.append({'name':'超期结办','value':value})
        sql = "SELECT INTIME_TO_ARCHIVE_NUM FROM website.data where INTIME_TO_ARCHIVE_NUM=1"
        value = db.execute(sql)
        mychart3data.append({'name':'处置中','value':value})
        sql = "SELECT INTIME_ARCHIVE_NUM FROM website.data where INTIME_ARCHIVE_NUM=1"
        value = db.execute(sql)
        mychart3data.append({'name':'按期结办','value':value})
        for i in range(0,len):
            sql = "SELECT EVENT_TYPE_NAME FROM website.data Where EVENT_TYPE_NAME=\""+name[i][0]+"\""
            value=db.execute(sql)
            mychart3data.append({'name':name[i][0],'value':value})
            request.session["time_request"]=1

    if request.session.get("mychart3data")==None:
        request.session["mychart3data"]=mychart3data

    if request.session.get("time_request")==1:
        start_time=request.session.get("start_time")
        end_time=request.session.get("end_time")
        end_time=end_time.split("-",2)
        end_time[2]=int(end_time[2])+1
        if(end_time[2]<10):
            end_time[2]="0"+str(end_time[2])
        else:
            end_time[2]=str(end_time[2])
        end_time=end_time[0]+"-"+end_time[1]+"-"+end_time[2]
        request.session["time_request"]=2
        sql = "SELECT EVENT_TYPE_NAME FROM website.data where EVENT_TYPE_NAME IN (SELECT EVENT_TYPE_NAME FROM website.data WHere CREATE_TIME > \""+start_time+"\" and CREATE_TIME < \""+end_time+"\") Group by EVENT_TYPE_NAME"
        len = db.execute(sql)
        name = db.fetchall()
        mychart3data2=[{'version':chart.mysql.GetVersion(db),'time_request':1,'length1':3,'length2':len,'start_time':request.session.get("start_time"),'end_time':request.session.get("end_time")}]
        sql = "SELECT OVERTIME_ARCHIVE_NUM FROM website.data where OVERTIME_ARCHIVE_NUM=1 and id IN (SELECT id FROM website.data WHere CREATE_TIME > \""+start_time+"\" and CREATE_TIME < \""+end_time+"\")"
        value = db.execute(sql)
        mychart3data2.append({'name':'超期结办','value':value})
        sql = "SELECT INTIME_TO_ARCHIVE_NUM FROM website.data where INTIME_TO_ARCHIVE_NUM=1 and id IN (SELECT id FROM website.data WHere CREATE_TIME > \""+start_time+"\" and CREATE_TIME < \""+end_time+"\")"
        value = db.execute(sql)
        mychart3data2.append({'name':'处置中','value':value})
        sql = "SELECT INTIME_ARCHIVE_NUM FROM website.data where INTIME_ARCHIVE_NUM=1 and id IN (SELECT id FROM website.data WHere CREATE_TIME > \""+start_time+"\" and CREATE_TIME < \""+end_time+"\")"
        value = db.execute(sql)
        mychart3data2.append({'name':'按期结办','value':value})

        for i in range(0,len):
            sql = "SELECT EVENT_TYPE_NAME FROM website.data Where EVENT_TYPE_NAME=\""+name[i][0]+"\" and id IN (SELECT id FROM website.data WHere CREATE_TIME > \""+start_time+"\" and CREATE_TIME < \""+end_time+"\")"
            value=db.execute(sql)
            mychart3data2.append({'name':name[i][0],'value':value})
            request.session["mychart3data"]=mychart3data2

    if request.session.get("time_request")==2:
        request.session["time_request"]=0
        mychart3data2 = request.session.get("mychart3data")
        mychart3data2[0]['time_request']=0
        request.session["mychart3data"]=mychart3data2
    chart.mysql.database_close(connection,db)
    return JsonResponse(request.session.get("mychart3data"),safe=False)


def nofound(request):
    return render(request,"404.html",locals())