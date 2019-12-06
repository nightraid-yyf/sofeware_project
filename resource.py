import sys
print("程序启动")
i=1
while 1:
    try:
        name=sys.argv[i]
        print("开始处理文件:"+name)
        chr = ["\"js/","\"css/","\"img/","\"{% static \'"," %}\"",".css\"",".js\"",".png\"",".jpg\""]
        with open(name,"r") as f:
            msg = f.read()
            msg = msg.replace(chr[0],chr[0].replace("\"",chr[3]))
            msg = msg.replace(chr[1],chr[1].replace("\"",chr[3]))
            msg = msg.replace(chr[2],chr[2].replace("\"",chr[3]))
            msg = msg.replace(chr[5],chr[5].replace("\"","\'"+chr[4]))
            msg = msg.replace(chr[6],chr[6].replace("\"","\'"+chr[4]))
            msg = msg.replace(chr[7],chr[7].replace("\"","\'"+chr[4]))
            msg = msg.replace(chr[8],chr[8].replace("\"","\'"+chr[4]))
        with open(name,"w") as f:
            f.write("{% load staticfiles %}\n")
            f.write(msg)
            f.close()
            print("修改完成")
        i=i+1
    except:
        print("文件处理完成")
        break

