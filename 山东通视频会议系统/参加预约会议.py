import datetime
import time
from appium.webdriver.common.touch_action import TouchAction
import re
from datetime import datetime
from datetime import datetime, timedelta

if Button(driver, loc="//*[@text='同意']", l_type="XPATH").wait():
    Button(driver, loc="//*[@text='同意']", l_type="XPATH").click()
    time.sleep(8)
    tap(driver,[(500,1400)],0,0)
    time.sleep(8)
    if Button(driver, loc="//*[@text='同意']", l_type="XPATH").wait():
        Button(driver, loc="//*[@text='同意']", l_type="XPATH").click()
time.sleep(8)
if Button(driver, loc="//*[@text='帐号登录']", l_type="XPATH").wait():
    Button(driver, loc="//*[@text='帐号登录']", l_type="XPATH").click()
    #Button(driver, loc="//*[@text='同意']", l_type="XPATH").click()
if Button(driver, loc="//*[@text='山东通统一认证']", l_type="XPATH").wait():
    Button(driver, loc="//*[@resource-id='username']", l_type="XPATH").input("13668805290")
    Button(driver, loc="//*[@resource-id='password']", l_type="XPATH").input("lishilong1234")
    Button(driver, loc="//*[@resource-id='loginBtn']", l_type="XPATH").click()
time.sleep(20)
#点击首页上的视频会议
#if Button(driver, loc="//*[@text='视频会议']", l_type="XPATH").wait():
#Button(driver, loc="//*[@text='视频会议']", l_type="XPATH").click()
tap(driver,[(365,419)],0,0)
tap(driver,[(365,419)],0,0)
tap(driver,[(365,419)],0,0)
#Button(driver, loc="//*[@text='视频会议']", l_type="XPATH").click()
time.sleep(10)
#点击最底层会议进行参会
#获取当前页面
xml_text = str(driver.page_source)
xml_text = xml_text.replace('<', '').replace('>', '').replace('?', '').replace(' ', '').replace('\n', '').replace('"', '')
#数据处理 取autotest后14位字符
prefix = "autotest"
length = 14
index = 0
while index < len(xml_text):
    if xml_text.startswith(prefix, index):
        start_index = index + len(prefix)
        end_index = start_index + length
        checkpointip = xml_text[start_index:end_index]
        index = end_index
    else:
        index += 1
print(checkpointip)
#获取现在时间
now=datetime.now()
formatted_date=now.strftime("%Y%m%d%H%M%S")
#将两个时间进行对比
# 将时间字符串转换为日期时间对象
time1 = datetime.strptime(checkpointip, "%Y%m%d%H%M%S")
time2 = datetime.strptime(formatted_date, "%Y%m%d%H%M%S")
#计算时间差
time_diff = abs(time1 - time2)
# 定义一个小时的时间间隔
half_hour = timedelta(minutes=40)
# 判断时间差是否在一个小时内
if time_diff <= half_hour:
    checkpoint="预约会议成功"
else:
    Button(driver, loc="//*[@text='未收到预约会议或预约会议失败，请检查预约会议是否正常']", l_type="XPATH").click()
theme='autotest'+checkpointip
if Button(driver, loc="//*[@text='"+theme+"']", l_type="XPATH").wait():
    Button(driver, loc="//*[@text='"+theme+"']", l_type="XPATH").click()
    if Button(driver, loc="//*[@text='参 会']", l_type="XPATH").wait():
        Button(driver, loc="//*[@text='参 会']", l_type="XPATH").click()
    tap(driver,[(50,50)],0,0)
        # data = str(driver.page_source)
        # logging.info(data)
#tap(driver,[(200,200)],0,0)
time.sleep(5)
Button(driver, loc="//*[@text='挂断']", l_type="XPATH").click()
#logging.info(checkpoint)
put_out_data('checkpoint',checkpoint)

