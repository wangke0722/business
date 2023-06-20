# 识别验证码
# 调用exe识别验证码
# 配置文件路径，，，path为exe路径，，P1为需要识别的验证码图片
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from PIL import Image
import base64
import os

driver = get_driver()
driver.implicitly_wait(5)
driver.get('https://vc.sd-meeting.cn/console/management#/business/monitor/concurrence')
sleep(2)
point = Element(loc = '/html/body',l_type = 'XPATH').value()
aaa=0
if '综合运维' not in point:
    aaa=1
    open_url ('https://vc.sd-meeting.cn/')
    if Element(loc='//*[@id="root"]/div/div[2]/div/div[1]', l_type='XPATH').wait():
        Element(loc='//*[@id="account_username"]', l_type='XPATH').input("zhyw@sdt.cn")
        Element(loc='//*[@id="account_password"]', l_type='XPATH').input("zhyw1@SDT")
        Element(loc='//*[@id="root"]/div/div[2]/div/div[2]/div/form/span/button', l_type='XPATH').click()
    else:
        raise Exception("打开网址失败")
    #n = 1
    point = Element(loc = '/html/body',l_type = 'XPATH').value()
    #while '综合运维' not in point and n < 20:
    while '综合运维' not in point:
        #滑块
        #txt1 = Element(loc='//*[@id="xyv-image-slider"]/img', l_type='XPATH').value('src')
        #背景图
        #txt2 = Element(loc='//*[@id="xyv-validate"]/div[1]/div/div[1]/img', l_type='XPATH').value('src')
        #bg = "C:\\bg.png"
        #tp = "C:\\full.png"
        #with open(bg, 'wb') as f:
            #f.write(base64.b64decode(txt2.split("base64,")[1]))
        #with open(tp, 'wb') as f:
            #f.write(base64.b64decode(txt1.split("base64,")[1]))
        #path = r'C:\img_det.exe'
        #para = "%s" % (path)
        #f = os.popen(para)
        #result = int(f.read())-56
        result = 225#196
        result1 = random.randint(1,100)
        Element(loc='//*[@id="xyv-sliderbar"]', l_type='XPATH').click_and_hold()
        Element(loc='//*[@id="xyv-sliderbar"]', l_type='XPATH').move_to_element_with_offset(x=result1,y=0)
        Element(loc='//*[@id="xyv-sliderbar"]', l_type='XPATH').move_to_element_with_offset(x=result-result1,y=0)
        Element(loc='//*[@id="xyv-sliderbar"]', l_type='XPATH').release()
        sleep(2)
        # try:
        #     Element(loc='/html/body/div[1]/section/main/div/aside/div/ul/li[1]/span/span', l_type='XPATH').click()
        #     break
        # except:
        #     pass
        point = Element(loc = '/html/body',l_type = 'XPATH').value()
        #n = n + 1
if aaa == 1:
    driver.get('https://vc.sd-meeting.cn/console/management#/business/monitor/concurrence')
ele = driver.find_element_by_xpath('/html/body/div[1]/section/main/div/div/div/div[2]/div/div/div[2]/div[2]')
ActionChains(driver).move_to_element(ele).move_by_offset(690,100).click().perform()
ActionChains(driver).move_to_element(ele).move_by_offset(700,0).click().perform()
test1 = Element(loc = '/html/body/div[1]/section/main/div/div/div/div[2]/div/div/div[2]/div[2]/div[2]',l_type = 'XPATH').value()
if test1:
    checkpoint1 = test1.split("最大参会者并发: ")[0]
    c = test1.split("最大参会者并发: ")[1].split("最大云会议室共享参会者并发:")[0]
    printinfo = int(c.replace(',',''))
    #checkpoint2 = test1.split("最大参会者并发: ")[1].split("最大云会议室共享参会者并发:")[0]
    #checkpoint3 = int(test1.split("最大H323参会者并发:")[1].split("最大会议数并发: ")[0])
    bingfa = int(test1.split("最大H323参会者并发:")[1].split("最大会议数并发: ")[0])
    if bingfa > 11:
        checkpoint3="最大H323参会者并发当前为："+str(bingfa)+"11，发出告警"
    else:
        checkpoint3=bingfa
    if printinfo < 1000:
        checkpoint2=printinfo
    elif 1000 < printinfo < 2000:
        checkpoint2="最大参会者并发当前为："+str(printinfo)+"阈值超过1000，常规告警"
    elif 2000 < printinfo < 3500:
        checkpoint2="最大参会者并发当前为："+str(printinfo)+"阈值超过2000，重要告警"
    else:
        checkpoint2="最大参会者并发当前为："+str(printinfo)+"阈值超过3500，紧急告警"
else:
    checkpoint1=0
    checkpoint2=0
    checkpoint3=0
put_out_data('checkpoint1',checkpoint1)
put_out_data('checkpoint2',checkpoint2)
put_out_data('checkpoint3',checkpoint3)