#入参定义
case_name=${case_name}
moudle_name=${moudle_name}
detect_address=${detect_address}
#打开浏览器
open_url('about:blank')
driver = get_driver()
#开始计时
starttime=time.time()
#打开网址
#http://124.128.58.241/qingdao/index?siteCode=371000000000
try:
    driver.get("https://"+detect_address)
except:
    pass
sleep(1)
title = driver.title
i=1
while i<5:
    if "数据开放网" in title:
        break
    else:
        try:
            driver.get("https://"+detect_address)
        except:
            pass
        sleep(1)
        title = driver.title
        i=i+1
#判断
if "数据开放网" in title:
    #获取检查点
    checkpoint=title
    #输出检查点
    put_out_data('checkpoint',checkpoint)
    #记录结束时间
    endtime=time.time()
    #计算耗时
    LogTime=endtime-starttime
    #记录日志
    add_oper_log('RESULT',case_name,value=str(LogTime),operator='0',expect_value=moudle_name)
    #关闭浏览器
    close_url()
else:
    #记录异常日志
    add_oper_log('RESULT',case_name,value='0',operator='1',expect_value=moudle_name)
    #抛出异常
    raise Exception("系统页面打开失败！")
    #关闭浏览器
    close_url()