from selenium import webdriver
#from selenium.webdriver.common.action_chains import ActionChains
#入参定义
case_name=${case_name}
moudle_name=${moudle_name}
detect_address=${detect_address}
#打开空白页
#open_url('about:blank')
#detect_address='https://zwfw.sd.gov.cn/JIS/front/login.do'
driver = get_driver()
#耗时记录开始
starttime=time.time()
#打开网站网址
#driver.get("https://"+detect_address+"/JIS/front/login.do")
open_url("https://"+detect_address+"/JIS/front/login.do")
#点击弹出窗口的确定按钮  //*[@id="cloud"]/div
#//*[@id="grloginform"]/div[3]/div/span[3]/a[2]
Element(loc = '//*[@id="cloud"]/div',l_type = 'XPATH').click()
#点击注册按钮 //*[@id="grloginform"]/div[5]/div/span[3]/a[2]
Element(loc = '//*[@id="grloginform"]/div[3]/div/span[3]/a[2]',l_type = 'XPATH').click()
#判断检查点出现：//*[@id="mobile1"]/span    手机号码：
if Element(loc = '//*[@id="mobile1"]/span',l_type = 'XPATH').wait():
    #获取检查点值
    checkpoint = Element(loc = '//*[@id="mobile1"]/span',l_type = 'XPATH').value()
    #输出检查点
    put_out_data('checkpoint',checkpoint)
    #结束计时
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