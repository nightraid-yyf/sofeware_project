import sys
print("程序启动")
i=1
while 1:
    try:
        name=sys.argv[i]
        print("开始处理文件:"+name)
        with open(name,"r") as f:
            msg = f.read()
            msg = msg.replace("\'chart/","\'chart/datatable/")
        with open(name,"w") as f:
            f.write(msg)
            f.close()
            print("修改完成")
        i=i+1
    except:
        print("文件处理完成")
        break

