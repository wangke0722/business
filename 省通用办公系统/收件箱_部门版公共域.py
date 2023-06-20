from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
#入参定义
case_name=${case_name}
moudle_name=${moudle_name}
name=${name}
password=${password}
#打开浏览器
open_url('about:blank')
sleep(0.5)
#get直接返回，不再等待界面加载完成
#desired_capabilities = DesiredCapabilities.CHROME
#desired_capabilities["pageLoadStrategy"] = "none"
driver = get_driver()
#打开网址
driver.get("http://59.206.205.208/login")
#判断OA用户名是否出现
if Element(loc = '//*[@id="userId"]',l_type = 'XPATH').wait():
    #清除用户名框内信息
    Element(loc = '//*[@id="userId"]',l_type = 'XPATH').clear()
    #输入用户名
    Element(loc = '//*[@id="userId"]',l_type = 'XPATH').input(name)
    sleep(0.5)
    #清空密码框内信息
    Element(loc = '//*[@id="userPass"]',l_type = 'XPATH').clear()
    #输入密码
    Element(loc = '//*[@id="userPass"]',l_type = 'XPATH').input(password)
    #点击登录
    Element(loc = '//*[@id="check"]/img',l_type = 'XPATH').click()
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
    #验证工作台是否出现
    if Element(loc = '/html/body/section/section/section/aside/div/div[1]/div/ul/li[1]/div/span',l_type = 'XPATH').wait():
        sleep(2)
        #点击更多/html/body/section/section/header/div[2]/ul/li[2]/div/span'
        try:
            Element(loc = '/html/body/section/section/header/div[2]/ul/li[2]/div[1]/span',l_type = 'XPATH').click()
        except:
            driver.refresh()
            Element(loc = '/html/body/section/section/header/div[2]/ul/li[2]/div[1]/span',l_type = 'XPATH').click()
        #模拟鼠标悬停
        chain=ActionChains(driver)
        AAA=driver.find_element_by_xpath('/html/body/section/section/header/div[2]/ul/li[2]/div[1]/span')
        chain.move_to_element(AAA).perform()
        #点击收文管理
        if Element(loc = '/html/body/div/ul/div/div/div[1]/ul/li[1]/a',l_type = 'XPATH').wait():
            starttime=time.time()
            #偶尔点击不到收件箱，调用js点击
            #click_link=driver.find_element_by_link_text('公文传送')
            js=driver.find_element_by_xpath('/html/body/div/ul/div/div/div[1]/ul/li[1]/a')
            driver.execute_script("arguments[0].click()",js)
            #sleep(10)
        else:
            add_oper_log('RESULT',case_name,value='0',operator='1',expect_value=moudle_name)
            raise Exception("未找到检查点，链接未找到！")
            close_url()
        sleep(10)
        chain=ActionChains(driver)
        BBB=driver.find_element_by_xpath('/html/body/section/section/section/aside/div/div[1]/div/ul/li/ul/li[1]/span')
        chain.move_to_element(BBB).perform()
        #设置检查点
        if Element(loc = '/html/body/section/section/section/main/div/div[2]/div/div[2]/table/thead/tr/th[3]/div',l_type = 'XPATH').wait():
            #获取检查点 来文单位
            checkpoint = Element(loc = '/html/body/section/section/section/main/div/div[2]/div/div[2]/table/thead/tr/th[3]/div',l_type = 'XPATH').value()
            #输出检查点 标题
            put_out_data('checkpoint',checkpoint)
            sleep(5)
            Element(loc = '/html/body/section/section/header/div[4]/div/div/span',l_type = 'XPATH').click()
            #/html/body/section/section/header/div[4]/div/div/span/i
            #Element(loc = '/html/body/ul/li[2]/i',l_type = 'XPATH').click()
            jl=driver.find_element_by_xpath('/html/body/ul/li[2]/i')
            driver.execute_script("arguments[0].click()",jl)
            #/html/body/div[2]/div/div[3]/button[2]/span
            Element(loc = '/html/body/div[2]/div/div[3]/button[2]/span',l_type = 'XPATH').click()
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
            raise Exception("未找到检查点，收件箱打开失败！")
            #关闭浏览器
            try:
                close_url()
            except:
                pass
    else:
        #记录异常日志
        add_oper_log('RESULT',case_name,value='0',operator='1',expect_value=moudle_name)
        #抛出异常
        raise Exception("个人工作台打开失败！")
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