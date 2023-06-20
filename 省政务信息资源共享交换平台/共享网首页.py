#打开网址case_namemoudle_name
case_name=${case_name}
moudle_name=${moudle_name}
detect_address=${detect_address}
#detect_address='http://59.206.218.150/portal/'
open_url('about:blank')
sleep(0.5)
driver = get_driver()
starttime=time.time()
driver.get(detect_address)
if Element(loc = '//*[@id="pDyna"]/a',l_type = 'XPATH').wait():
    checkpoint = Element(loc = '//*[@id="pDyna"]/a',l_type = 'XPATH').value()
    put_out_data('checkpoint',checkpoint)
    endtime=time.time()
    LogTime=endtime-starttime
    add_oper_log('RESULT',case_name,value=str(LogTime),operator='0',expect_value=moudle_name)
    close_url()
else:
    add_oper_log('RESULT',case_name,value='0',operator='1',expect_value=moudle_name)
    raise Exception(case_name+"打开失败！")