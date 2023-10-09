from selenium import webdriver

case_name=${case_name}
moudle_name=${moudle_name}
try:
    driver = get_driver()
    # 最大化浏览器窗口
    driver.maximize_window()
    driver.get("http://172.20.235.118:83/datastandard/")
except:
    pass
#页面展示情况
sleep(0.5)
if Element(loc = '/html/body/div/div[2]/div/form/div[3]/button',l_type = 'XPATH').wait():
    checkpoint = Element(loc = '/html/body/div/div[2]/div/form/div[3]/button',l_type = 'XPATH').value()
    put_out_data('checkpoint',checkpoint)
    close_url()
else:
    add_oper_log('RESULT',case_name,value='0',operator='1',expect_value=moudle_name)
    raise Exception("访问数据标准链接跳转登录界面失败！")
    close_url()