from selenium import webdriver
#from selenium.webdriver.common.action_chains import ActionChains
#入参定义
case_name=${case_name}
moudle_name=${moudle_name}
detect_address=${detect_address}
#打开浏览器
#open_url('about:blank')
#detect_address='https://zwfw.sd.gov.cn/JIS/front/login.do'
#打开网址
driver = get_driver()
#driver.get("https://"+detect_address+"/JIS/front/login.do")
open_url("https://"+detect_address+"/JIS/front/login.do")
#点击弹出框确定按钮
Element(loc = '//*[@id="cloud"]/div',l_type = 'XPATH').click()
#判断法人登录是否出现
if Element(loc = '//*[@id="one2"]',l_type = 'XPATH').wait():
    #点击弹出框确定按钮
    Element(loc = '//*[@id="one2"]',l_type = 'XPATH').click()
    #点击法人登录
    Element(loc = '//*[@id="cloud1"]/div',l_type = 'XPATH').click()
    #判断注册按钮出现
    if Element(loc = '//*[@id="frloginform"]/div[3]/span/a[3]',l_type = 'XPATH').wait():
        #开始计时
        starttime=time.time()
        #点击注册按钮 //*[@id="frloginform"]/div[5]/span/a[3]
        #//*[@id="frloginform"]/div[3]/span/a[3]
        Element(loc = '//*[@id="frloginform"]/div[3]/span/a[3]',l_type = 'XPATH').click()
        if Element(loc = '/html/body/div[2]/div/div[1]/div/p[1]',l_type = 'XPATH').wait():
            #获取检查点
            checkpoint = Element(loc = '/html/body/div[2]/div/div[1]/div/p[1]',l_type = 'XPATH').value()
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
            raise Exception(case_name+"页面打开失败！")
            #关闭浏览器
            close_url()
    else:
        #记录异常日志
        add_oper_log('RESULT',case_name,value='0',operator='1',expect_value=moudle_name)
        #抛出异常
        raise Exception(case_name+"登录2页面打开失败！")
        #关闭浏览器
        close_url()
else:
    #记录异常日志
    add_oper_log('RESULT',case_name,value='0',operator='1',expect_value=moudle_name)
    #抛出异常
    raise Exception(case_name+"登录页面打开失败！")
    #关闭浏览器
    close_url()