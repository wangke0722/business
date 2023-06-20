import datetime
import time
from appium.webdriver.common.touch_action import TouchAction

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
    Button(driver, loc="//*[@resource-id='username']", l_type="XPATH").input("18369905485")
    Button(driver, loc="//*[@resource-id='password']", l_type="XPATH").input("iam500623")
    Button(driver, loc="//*[@resource-id='loginBtn']", l_type="XPATH").click()
time.sleep(20)
tap(driver,[(655,2034)],0,0)
tap(driver,[(655,2034)],0,0)
tap(driver,[(655,2034)],0,0)
tap(driver,[(655,2034)],0,0)
#if Button(driver, loc="//*[@text='工作台']", l_type="XPATH").wait():
#    Button(driver, loc="//*[@text='工作台']", l_type="XPATH").click()
time.sleep(40)
    # tap(driver,[(750,450)],0,0)
    # time.sleep(2)
    # tap(driver,[(750,450)],0,0)
    # time.sleep(2)
tap(driver,[(160,480)],0,0)
tap(driver,[(160,480)],0,0)
tap(driver,[(160,480)],0,0)
tap(driver,[(160,480)],0,0)
tap(driver,[(160,480)],0,0)
time.sleep(20)
curr_time = datetime.datetime.now()
time_str = datetime.datetime.strftime(curr_time,'%Y%m%d%H%M%S')
a=time.strftime("YYYYmmddHHMM",time.localtime(time.time()))
bbb="autotest"+time_str
if Button(driver, loc="//*[@instance='12']", l_type="XPATH").wait():
    Button(driver, loc="//*[@instance='12']", l_type="XPATH").input(bbb)
    tap(driver,[(1041,1200)],0,0)
if Button(driver, loc="//*[@text='单位通讯录']", l_type="XPATH").wait():
    Button(driver, loc="//*[@text='单位通讯录']", l_type="XPATH").click()
    Button(driver, loc="//*[@text='综合运维管理']", l_type="XPATH").click()
    Button(driver, loc="//*[@text='李世龙']", l_type="XPATH").click()
    Button(driver, loc="//*[@text='确定·1']", l_type="XPATH").click()
    if Button(driver, loc="//*[@text='确 定']", l_type="XPATH").wait():
        Button(driver, loc="//*[@text='确 定']", l_type="XPATH").click()
        if Button(driver, loc="//*[@text='暂不']", l_type="XPATH").wait():
            Button(driver, loc="//*[@text='暂不']", l_type="XPATH").click()
time.sleep(10)
if Button(driver, loc="//*[@text='我的日程']", l_type="XPATH").wait():
    Button(driver, loc="//*[@text='我的日程']", l_type="XPATH").click()
    if Button(driver, loc="//*[@text='"+bbb+"']", l_type="XPATH").wait():
        Button(driver, loc="//*[@text='"+bbb+"']", l_type="XPATH").click()
        if Button(driver, loc="//*[@text='参 会']", l_type="XPATH").wait():
            Button(driver, loc="//*[@text='参 会']", l_type="XPATH").click()
        tap(driver,[(50,50)],0,0)
        # data = str(driver.page_source)
        # logging.info(data)
#tap(driver,[(200,200)],0,0)
time.sleep(5)
Button(driver, loc="//*[@text='挂断']", l_type="XPATH").click()
time.sleep(10)
tap(driver,[(199,134)],0,0)
tap(driver,[(199,134)],0,0)
tap(driver,[(108,134)],0,0)
tap(driver,[(108,134)],0,0)
#driver.keyevent(4)
#driver.keyevent(4)
#aaa = str(driver.page_source)
#logging.info(aaa)
if Button(driver, loc="//*[@text='我']", l_type="XPATH").wait():
    Button(driver, loc="//*[@text='我']", l_type="XPATH").click()
    if Button(driver, loc="//*[@text='设置']", l_type="XPATH").wait():
        Button(driver, loc="//*[@text='设置']", l_type="XPATH").click()
        if Button(driver, loc="//*[@text='退出登录']", l_type="XPATH").wait():
            Button(driver, loc="//*[@text='退出登录']", l_type="XPATH").click()
            if Button(driver, loc="//*[@text='退出当前帐号']", l_type="XPATH").wait():
                Button(driver, loc="//*[@text='退出当前帐号']", l_type="XPATH").click()
                if Button(driver, loc="//*[@text='确定']", l_type="XPATH").wait():
                    Button(driver, loc="//*[@text='确定']", l_type="XPATH").click()