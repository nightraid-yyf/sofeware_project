import chart.mysql
import time
from datetime import datetime, timedelta

def get_alertInfo(maximum):
    connection,db=chart.mysql.database_connect()
    db=chart.mysql.Testconnect(db,connection)
    sql="SELECT CREATE_TIME,STREET_NAME,COMMUNITY_NAME,SUB_TYPE_NAME,DISPOSE_UNIT_NAME from data where INTIME_TO_ARCHIVE_NUM=1 order by CREATE_TIME"
    len=db.execute(sql)
    info=db.fetchall()
    if len<=0:
         msg=""
         i=0
    else:
        msg=""
        i=0
        for msg_de in info:
            msg=msg+"<span style=\"margin-left:10%;font:黑体;font-weight:bold;\"><span style=\"color:red;margin-top:1px;\">处置中事件:</span>"
            msg=msg+"时间:<span style=\"margin-right:0.5%;color:white;background-color:gray\">"+msg_de[0]+"</span>"
            msg=msg+"街道:<span style=\"margin-right:0.5%;color:white;background-color:#8080C0\">"+msg_de[1]+"</span>"
            msg=msg+"社区:<span style=\"margin-right:0.5%;color:white;background-color:red\">"+msg_de[2]+"</span>"
            msg=msg+"事件分类:<span style=\"margin-right:0.5%;color:white;background-color:#B45B3E\">"+msg_de[3]+"</span>"
            msg=msg+"提交单位:<span style=\"margin-right:0.5%;color:white;background-color:#00B271\">"+msg_de[4]+"</span></span>"
            i=i+1
            if i==maximum:
                connection.close()
                return msg
    sql="SELECT CREATE_TIME,STREET_NAME,COMMUNITY_NAME,SUB_TYPE_NAME,DISPOSE_UNIT_NAME from data where OVERTIME_ARCHIVE_NUM=1 order by CREATE_TIME"
    len=db.execute(sql)
    info=db.fetchall()
    if len+i<maximum:
        maximum=len+i
    if len+i<=0:
            msg="<span style=\"color:black;margin-top:1px;\">暂无报警事件</span>"
            connection.close()
            return msg
    for msg_de in info:
        msg=msg+"<span style=\"margin-left:10%;font:黑体;font-weight:bold;\"><span style=\"color:red;margin-top:1px;\">超期未结办事件:</span>"
        msg=msg+"时间:<span style=\"margin-right:0.5%;color:white;background-color:gray\">"+msg_de[0]+"</span>"
        msg=msg+"街道:<span style=\"margin-right:0.5%;color:white;background-color:#8080C0\">"+msg_de[1]+"</span>"
        msg=msg+"社区:<span style=\"margin-right:0.5%;color:white;background-color:red\">"+msg_de[2]+"</span>"
        msg=msg+"事件分类:<span style=\"margin-right:0.5%;color:white;background-color:#B45B3E\">"+msg_de[3]+"</span>"
        msg=msg+"提交单位:<span style=\"margin-right:0.5%;color:white;background-color:#00B271\">"+msg_de[4]+"</span></span>"
        i=i+1
        if i==maximum:
            connection.close()
            return msg
    connection.close()
    return msg


def show_alertInfo(maximum):
    connection,db=chart.mysql.database_connect()
    db=chart.mysql.Testconnect(db,connection)
    sql="SELECT CREATE_TIME,COMMUNITY_NAME,SUB_TYPE_NAME,id from data where INTIME_TO_ARCHIVE_NUM=1 order by CREATE_TIME"
    len=db.execute(sql)
    info=db.fetchall()
    if len<=0:
        data=[]
        i=0
    else:
        data=[]
        i=0
        for msg_de in info:
            dic={}
            dic["type"]=1
            dic["id"]="alert_"+str(msg_de[3])
            dic["community"]=msg_de[1]
            dic["time"]=msg_de[0]
            dic["event"]=msg_de[2]
            timein = datetime.strptime(msg_de[0],'%Y-%m-%d %H:%M:%S')
            timenow = datetime.now()
            timeout=timenow-timein
            total_seconds=timeout.total_seconds()
            days=int(total_seconds/(24*3600))
            total_seconds=total_seconds-(24*3600*days)
            hours=int(total_seconds/3600)
            total_seconds=total_seconds-(3600*hours)
            minutes=int(total_seconds/60)
            dic["delay"]=str(days)+"天-"+str(hours)+"小时-"+str(minutes)+"分钟"
            data.append(dic)
            i=i+1
            if i==maximum:
                connection.close()
                return data
    
    sql="SELECT CREATE_TIME,COMMUNITY_NAME,SUB_TYPE_NAME,id from data where OVERTIME_ARCHIVE_NUM=1 order by CREATE_TIME"
    len=db.execute(sql)
    info=db.fetchall()
    if (len+i)<maximum:
        maximum=len+i
    if len<=0:
        connection.close()
        return data
    for msg_de in info:
        dic={}
        dic["type"]=0
        dic["id"]="alert_"+str(msg_de[3])
        dic["community"]=msg_de[1]
        dic["time"]=msg_de[0]
        dic["event"]=msg_de[2]
        timein = datetime.strptime(msg_de[0],'%Y-%m-%d %H:%M:%S')
        timenow = datetime.now()
        timeout=timenow-timein
        total_seconds=timeout.total_seconds()
        days=int(total_seconds/(24*3600))
        total_seconds=total_seconds-(24*3600*days)
        hours=int(total_seconds/3600)
        total_seconds=total_seconds-(3600*hours)
        minutes=int(total_seconds/60)

        dic["delay"]=str(days)+"天-"+str(hours)+"小时-"+str(minutes)+"分钟"
        data.append(dic)
        i=i+1
        if i==maximum:
            connection.close()
            return data
    connection.close()
    return data