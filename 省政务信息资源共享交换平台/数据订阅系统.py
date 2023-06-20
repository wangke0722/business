from selenium import webdriver
#打开网址case_namemoudle_name
case_name=${case_name}
moudle_name=${moudle_name}
#detect_address='http://59.206.218.150/portal/'/portal/
open_url('about:blank')
try:
    driver = get_driver()
    driver.get("http://data.sd.cegn.cn/ucenter/")
except:
    driver = get_driver()
    driver.refresh()
    driver.get("http://data.sd.cegn.cn/ucenter/")
sleep(0.5)
if Element(loc = '//*[@id="i-username"]',l_type = 'XPATH').wait():
    Element(loc = '//*[@id="i-username"]',l_type = 'XPATH').clear()
    Element(loc = '//*[@id="i-username"]',l_type = 'XPATH').input(${name})
    Element(loc = '//*[@id="i-password"]',l_type = 'XPATH').input(${pass})
    Element(loc = '//*[@id="dzzw-igp-form-login"]/button/strong',l_type = 'XPATH').click()
else:
    add_oper_log('RESULT',case_name,value='0',operator='1',expect_value=moudle_name)
    close_url()
    raise Exception(case_name+"用户名未找到！")
#登录结果判断，是否登录成功，综合运维管理
if Element(loc = '/html/body/header/div/ul[2]/li[3]/a',l_type = 'XPATH').wait():
    checkpoint = Element(loc = '/html/body/header/div/ul[2]/li[3]/a',l_type = 'XPATH').value()
else:
    close_url()
    add_oper_log('RESULT',case_name,value='0',operator='1',expect_value=moudle_name)
    raise Exception(case_name+"一体化大数据平台登录失败！")
starttime=time.time()
try:
    driver.get("http://data.sd.cegn.cn/pipelines/")
except:
    driver.refresh()
    driver.get("http://data.sd.cegn.cn/pipelines/")
try:
    switch_to_window("数据交换系统")
except:
    driver.refresh()
    switch_to_window("数据交换系统")
try:
    switch_to_window("数据交换系统")
    #if Element(loc = '//*[@id="nav-breadcrumb"]/li[2]/span',l_type = 'XPATH').wait():
    if Element(loc = '/html/body/div[2]/div[2]/div/div[2]/div/h4',l_type = 'XPATH').wait():
        print("111")
    else:
        print("222")
except:
    switch_to_window("数据交换系统")
    #if Element(loc = '//*[@id="nav-breadcrumb"]/li[2]/span',l_type = 'XPATH').wait():
    if Element(loc = '/html/body/div[2]/div[2]/div/div[2]/div/h4',l_type = 'XPATH').wait():
        print("333")
    else:
        print("444")
#if Element(loc = '//*[@id="nav-breadcrumb"]/li[2]/span',l_type = 'XPATH').wait():
if Element(loc = '/html/body/div[2]/div[2]/div/div[2]/div/h4',l_type = 'XPATH').wait():
    #/html/body/div[2]/div[2]/div/div[2]/div/h4
    endtime=time.time()
    checkpoint = Element(loc = '/html/body/div[2]/div[2]/div/div[2]/div/h4',l_type = 'XPATH').value()
    put_out_data('checkpoint',checkpoint)
    LogTime=endtime-starttime
    add_oper_log('RESULT',case_name,value=str(LogTime),operator='0',expect_value=moudle_name)
    close_url()
else:
    add_oper_log('RESULT',case_name,value='0',operator='1',expect_value=moudle_name)
    raise Exception(case_name+"打开失败")
    close_url()