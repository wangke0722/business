#打开网址case_namemoudle_name
case_name=${case_name}
moudle_name=${moudle_name}
#detect_address='http://59.206.218.150/portal/'
open_url('about:blank')
sleep(0.5)
driver = get_driver()
driver.get("http://59.206.218.150/portal/")
if Element(loc = '//*[@id="pDyna"]/a',l_type = 'XPATH').wait():
    checkpoint = Element(loc = '//*[@id="pDyna"]/a',l_type = 'XPATH').value()
    put_out_data('checkpoint',checkpoint)
else:
    add_oper_log('RESULT',case_name,value='0',operator='1',expect_value=moudle_name)
    raise Exception(case_name+"打开失败！")
#跳转到登录界面//*[@id="pDyna"]/a  /html/body/div[3]/div/div[3]/div[2]/ul/li[2]/a/span
sleep(10)
if Element(loc = '//*[@id="bounceIn"]',l_type = 'XPATH').wait():
    Element(loc = '//*[@id="bounceIn"]',l_type = 'XPATH').click()
else:
    add_oper_log('RESULT',case_name,value='0',operator='1',expect_value=moudle_name)
    raise Exception(case_name+"登录按钮未找到")
#zhywgl 123456aA?
#登录界面展示情况判断
sleep(0.5)
if Element(loc = '//*[@id="i-username"]',l_type = 'XPATH').wait():
    Element(loc = '//*[@id="i-username"]',l_type = 'XPATH').clear()
    Element(loc = '//*[@id="i-username"]',l_type = 'XPATH').input(${name})
    Element(loc = '//*[@id="i-password"]',l_type = 'XPATH').input(${pass})
    Element(loc = '//*[@id="dzzw-igp-form-login"]/button/strong',l_type = 'XPATH').click()
else:
    add_oper_log('RESULT',case_name,value='0',operator='1',expect_value=moudle_name)
    raise Exception(case_name+"用户名未找到！")
    close_url()
#关闭浮窗
#/html/body/div[12]/div[1]/span
sleep(5)
if Element(loc = '/html/body/div[12]/div[1]/span',l_type = 'XPATH').wait():
    Element(loc = '/html/body/div[12]/div[1]/span',l_type = 'XPATH').click()
else:
    print("未点击浮窗关闭按钮")
#登录结果判断，是否登录成功，综合运维管理 /html/body/div[1]/div[1]/div/div/span
if Element(loc = '/html/body/div[1]/div[1]/div/div/span',l_type = 'XPATH').wait():
    checkpoint1 = Element(loc = '/html/body/div[1]/div[1]/div/div/span',l_type = 'XPATH').value()
    put_out_data('checkpoint1',checkpoint1)
else:
    add_oper_log('RESULT',case_name,value='0',operator='1',expect_value=moudle_name)
    raise Exception(case_name+"一体化大数据平台登录失败！")
    close_url()
#登录子系统
#/html/body/div[3]/div/div[3]/div[2]/ul/li[1]/a/span
if Element(loc = '/html/body/div[3]/div/div[3]/div[2]/ul/li[5]/a/span',l_type = 'XPATH').wait():
    starttime=time.time()
    Element(loc = '/html/body/div[3]/div/div[3]/div[2]/ul/li[5]/a/span',l_type = 'XPATH').click()
else:
    print("未点击申请审核系统")
#转到子系统页面
try:
    switch_to_window("山东省一体化大数据平台 - 资源申请授权系统")
except:
    driver.refresh()
    switch_to_window("山东省一体化大数据平台 - 资源申请授权系统")
#打开是否成功，验证点设置
if Element(loc = '/html/body/div[2]/div[2]/div/div[2]/div/h4',l_type = 'XPATH').wait():
    endtime=time.time()
    checkpoint2 = Element(loc = '/html/body/div[2]/div[2]/div/div[2]/div/h4',l_type = 'XPATH').value()
    put_out_data('checkpoint2',checkpoint2)
    LogTime=endtime-starttime
    add_oper_log('RESULT',case_name,value=str(LogTime),operator='0',expect_value=moudle_name)
    close_url()
else:
    add_oper_log('RESULT',case_name,value='0',operator='1',expect_value=moudle_name)
    close_url()
    raise Exception(case_name+"打开失败")