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
#打开网站网址
#driver.get("https://"+detect_address+"/JIS/front/login.do")
open_url("https://tysfrz.isdapp.shandong.gov.cn/jis-web/login")
#点击弹出窗口的确定按钮 //*[@id="rbbox"]/a
#sleep(4)
#try:
    #Element(loc = '//*[@id="rbbox"]/a',l_type = 'XPATH').click()
#except:
    #pass
# try:
#     Element(loc = '//*[@id="cloud"]/div',l_type = 'XPATH').click()
# except:
#     pass
Element(loc = '//*[@id="cloud1"]/p[7]',l_type = 'XPATH').click()
#点击注册按钮 //*[@id="grloginform"]/div[5]/div/span[3]/a[2]
#//             //*[@id="grloginform"]/div[3]/div/span[3]/a[2] //*[@id="app"]/div/div/div/div/div[2]/div/div[2]/div[3]/div[1]/div[2]/form/div[5]/div/div/span/a[2]
Element(loc = '//*[@id="app"]/div/div/div/div/div[2]/div/div[2]/div[3]/div[1]/div[2]/form/div[5]/div/div/span/a[2]',l_type = 'XPATH').click()
# try:
#     Element(loc = '//*[@id="grloginform"]/div[5]/div/span[3]/a[2]',l_type = 'XPATH').click()
# except:
#     Element(loc = '//*[@id="app"]/div/div/div/div/div[2]/div/div[2]/div[3]/div[1]/div[2]/form/div[5]/div/div/span/a[2]',l_type = 'XPATH').click()
    #              //*[@id="app"]/div/div/div/div/div[2]/div/div[2]/div[3]/div[1]/div[2]/form/div[5]/div/div/span/a[2]
#判断检查点出现：//*[@id="mobile1"]/span    手机号码： //*[@id="app"]/div/div/div/div[2]/div/div[3]/form/div[6]/div[1]/label
if Element(loc = '//*[@id="app"]/div/div/div/div[2]/div/div[1]/div/div[1]/p/font',l_type = 'XPATH').wait():
    #获取检查点值
    checkpoint = Element(loc = '//*[@id="app"]/div/div/div/div[2]/div/div[1]/div/div[1]/p/font',l_type = 'XPATH').value()
# elif Element(loc = '//*[@id="app"]/div/div/div/div[2]/div/div[3]/form/div[6]/div[1]/label',l_type = 'XPATH').wait():
#     checkpoint = Element(loc = '//*[@id="app"]/div/div/div/div[2]/div/div[3]/form/div[6]/div[1]/label',l_type = 'XPATH').value()
else:
    #抛出异常
    raise Exception(case_name+"页面打开失败！")
    #关闭浏览器
    close_url()
#输出检查点
put_out_data('checkpoint',checkpoint)
#关闭浏览器
close_url()