from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
#入参定义
case_name=${case_name}
moudle_name=${moudle_name}
detect_address=${detect_address}
name=${name}
password=${password}
#打开浏览器
open_url('about:blank')
#detect_address='http://15.208.0.78/Default.aspx'
driver = get_driver()
#打开网址
driver.get('http://59.206.205.208/login')
#开始计时
starttime=time.time()
#判断OA用户名是否出现
if Element(loc = '//*[@id="userId"]',l_type = 'XPATH').wait():
    #清除用户名框内信息
    Element(loc = '//*[@id="userId"]',l_type = 'XPATH').clear()
    #输入用户名
    Element(loc = '//*[@id="userId"]',l_type = 'XPATH').input(name)
    #输入密码
    Element(loc = '//*[@id="userPass"]',l_type = 'XPATH').input(password)
    #点击登录
    Element(loc = '//*[@id="check"]/img',l_type = 'XPATH').click()
    #//*[@id="Ticketform"]/div[3]/div/div[2]/div[3]/input[1]  登录按钮
    #[@id="Ticketform"]/div[3]/div/div[2]/div[3]/input[1]
    sleep(10)
    driver.refresh()
    if Element(loc='/html/body/section/section/header/div[2]/ul/li[1]/span', l_type='XPATH').wait():
        pass
    else:
        Element(loc = '//*[@id="userId"]',l_type = 'XPATH').clear()
        Element(loc = '//*[@id="userId"]',l_type = 'XPATH').input(name)
        sleep(0.5)
        Element(loc = '//*[@id="userPass"]',l_type = 'XPATH').clear()
        Element(loc = '//*[@id="userPass"]',l_type = 'XPATH').input(password)
        Element(loc = '//*[@id="check"]/img',l_type = 'XPATH').click()
    sleep(10)
    #判断检查点出现 个人工作台
    if Element(loc = '/html/body/section/section/section/aside/div/div[1]/div/ul/li[1]/div/span',l_type = 'XPATH').wait():
        #获取检查点
        checkpoint = Element(loc = '/html/body/section/section/section/aside/div/div[1]/div/ul/li[1]/div/span',l_type = 'XPATH').value()
        #输出检查点
        put_out_data('checkpoint',checkpoint)
        sleep(5)
        #注销账号，退出登录
        Element(loc = '/html/body/section/section/header/div[4]/div/div/span',l_type = 'XPATH').click()
        #/html/body/section/section/header/div[4]/div/div/span/i
        jl=driver.find_element_by_xpath('/html/body/ul/li[2]/i')
        driver.execute_script("arguments[0].click()",jl)
        #/html/body/div[2]/div/div[3]/button[2]/span
        Element(loc = '/html/body/div[1]/div/div[3]/button[2]/span',l_type = 'XPATH').click()
        sleep(3)
        #记录结束时间
        endtime=time.time()
        #计算耗时
        LogTime=endtime-starttime
        #记录日志
        add_oper_log('RESULT',case_name,value=str(LogTime),operator='0',expect_value=moudle_name)
        #关闭浏览器
        try:
            close_url()
        except:
            pass
    else:
        #记录异常日志
        add_oper_log('RESULT',case_name,value='0',operator='1',expect_value=moudle_name)
        #抛出异常
        raise Exception("登录失败！")
        #关闭浏览器
        try:
            close_url()
        except:
            pass
else:
    #记录异常日志
    add_oper_log('RESULT',case_name,value='0',operator='1',expect_value=moudle_name)
    #抛出异常
    raise Exception("登录页面打开失败！")
    #关闭浏览器
    try:
        close_url()
    except:
        pass