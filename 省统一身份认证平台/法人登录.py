from selenium import webdriver
#from selenium.webdriver.common.action_chains import ActionChains
#入参定义
case_name=${case_name}
moudle_name=${moudle_name}
detect_address=${detect_address}
#打开浏览器
#open_url('about:blank')
#detect_address='https://zwfw.sd.gov.cn/JIS/front/login.do'
driver = get_driver()
#打开网址
#driver.get("https://"+detect_address+"/JIS/front/login.do")
open_url("https://tysfrz.isdapp.shandong.gov.cn/jis-web/login")
#点击弹出框确定按钮
#sleep(4)
#try:
    #Element(loc = '//*[@id="rbbox"]/a',l_type = 'XPATH').click()
#except:
    #pass
#try:
Element(loc = '//*[@id="cloud1"]/div',l_type = 'XPATH').click()
#except:
    #pass
#判断法人登录是否出现
if Element(loc = '//*[@id="app"]/div/div/div/div/div[2]/div/div[2]/div[1]/div/div/div/div/div[1]/div[2]',l_type = 'XPATH').wait():
    #开始计时
    starttime=time.time()
    #点击法人登录
    Element(loc = '//*[@id="app"]/div/div/div/div/div[2]/div/div[2]/div[1]/div/div/div/div/div[1]/div[2]',l_type = 'XPATH').click()
    #点击弹出框确定按钮//*[@id="cloud1"]/div
    #Element(loc = '//*[@id="cloud1"]/div',l_type = 'XPATH').click()
    #判断检查点出现   //*[@id="frloginform"]/div[5]/span/a[3]
    if Element(loc = '//*[@id="app"]/div/div/div/div/div[2]/div/div[2]/div[3]/div[2]/div[2]/div/div[2]/a[3]/p',l_type = 'XPATH').wait():
        #获取检查点
        checkpoint = Element(loc = '//*[@id="app"]/div/div/div/div/div[2]/div/div[2]/div[3]/div[2]/div[2]/div/div[2]/a[3]/p',l_type = 'XPATH').value()
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
        raise Exception(case_name+"2页面打开失败！")
        #关闭浏览器
        close_url()
else:
    #记录异常日志
    add_oper_log('RESULT',case_name,value='0',operator='1',expect_value=moudle_name)
    #抛出异常
    raise Exception(case_name+"页面打开失败！")
    #关闭浏览器
    close_url()