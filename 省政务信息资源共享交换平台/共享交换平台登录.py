#登录界面展示情况判断
if Element(loc = '//*[@id="i-username"]',l_type = 'XPATH').wait():
    Element(loc = '//*[@id="i-username"]',l_type = 'XPATH').clear()
    Element(loc = '//*[@id="i-username"]',l_type = 'XPATH').input(${name})
    Element(loc = '//*[@id="i-password"]',l_type = 'XPATH').input(${pass})
    starttime=time.time()
    Element(loc = '//*[@id="dzzw-igp-form-login"]/button/strong',l_type = 'XPATH').click()
else:
    add_oper_log('RESULT',case_name,value='0',operator='1',expect_value=moudle_name)
    raise Exception(case_name+"用户名未找到！")
    close_url()
#登录结果判断，是否登录成功，综合运维管理
if Element(loc = '/html/body/header/div/ul[2]/li[3]/a',l_type = 'XPATH').wait():
    endtime=time.time()
    checkpoint = Element(loc = '/html/body/header/div/ul[2]/li[3]/a',l_type = 'XPATH').value()
    put_out_data('checkpoint',checkpoint)
    LogTime=endtime-starttime
    add_oper_log('RESULT',case_name,value=str(LogTime),operator='0',expect_value=moudle_name)
    close_url()
else:
    add_oper_log('RESULT',case_name,value='0',operator='1',expect_value=moudle_name)
    raise Exception(case_name+"一体化大数据平台登录失败！")
    close_url()