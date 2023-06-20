import os,time
import datetime
from datetime import datetime, timedelta

case_name=${case_name}
moudle_name=${moudle_name}
#modifiedTime = time.ctime(os.stat("C:\FTP/test.txt.tump").st_mtime)
#modifiedTime = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(os.stat("C:\FTP/test.txt.tump").st_mtime))
try:
    file_dir="C:\FTPNEW\iftpnew"
    dir_list=os.listdir(file_dir)
    for cur_file in dir_list:
        path=os.path.join(file_dir,cur_file)
        if os.path.isfile(path):
            if format(cur_file).startswith("125"):
                if len(cur_file)==1:
                    aaa=format(cur_file)
                elif len(cur_file)==0:
                    print("111111111")
                else:
                    aaa=format(cur_file)
                    print("222222222222")
    print(aaa)
    modifiedTime = time.strftime('%Y%m%d%H%M%S', time.localtime(os.stat("C:\FTPNEW\iftpnew/"+aaa).st_mtime))
    f = open('C:\FTPNEW\iftpnew/'+aaa)
    readTime = f.read()
    f.close()
    print(modifiedTime)
    modiTime=str(modifiedTime)
    #转换“修改文件时间”时间格式
    time2 = datetime.strptime(modiTime, "%Y%m%d%H%M%S")
    #获取现在时间
    now=datetime.now()
    formatted_date=now.strftime("%Y%m%d%H%M%S")
    time1 = datetime.strptime(formatted_date, "%Y%m%d%H%M%S")
    # 计算时间差
    time_diff = abs(time1 - time2)
    # 定义7分钟的时间间隔
    half_hour = timedelta(minutes=8)
    # 判断时间差是否在8分钟内
    if time_diff <= half_hour:
        pass
    else:
        raise Exception(case_name+"8分钟内未传输文件、请检查")
    print(modiTime)
    print(readTime)
    #2021120622400003
    #2021 1206 2357 25
    print(int(modiTime)-int(readTime))
    #.strip('\n')
    #os.remove("C:\FTP/"+aaa)
    LogTime=(int(modiTime)-int(readTime.strip("/n")))
    print(LogTime)
    if LogTime>399999999:
        close_url()
        add_oper_log('RESULT',case_name,value='0',operator='1',expect_value=moudle_name)
        raise Exception(case_name+"未传输或者数据不一致")
    else:
        close_url()
        add_oper_log('RESULT',case_name,value=str(LogTime),operator='0',expect_value=moudle_name)
except:
    close_url()
    add_oper_log('RESULT',case_name,value='0',operator='1',expect_value=moudle_name)
    raise Exception(case_name+"运行失败！")