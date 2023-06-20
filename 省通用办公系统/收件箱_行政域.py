from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

# 入参定义
case_name =${case_name}
moudle_name =${moudle_name}
detect_address =${detect_address}
name =${name}
password =${password}
# 打开浏览器
open_url('about:blank')
# detect_address='http://15.208.0.78/Default.aspx'
driver = get_driver()
# 打开网址
driver.get('http://' + detect_address)
# 判断OA用户名是否出现
if Element(loc='//*[@id="userId"]', l_type='XPATH').wait():
    # 清除用户名框内信息
    Element(loc='//*[@id="userId"]', l_type='XPATH').clear()
    # 输入用户名
    Element(loc='//*[@id="userId"]', l_type='XPATH').input(name)
    # 输入密码
    Element(loc='//*[@id="userPass"]', l_type='XPATH').input(password)
    # 点击登录
    Element(loc='//*[@id="check"]/img', l_type='XPATH').click()
    # 判断检查点出现 个人工作台
    if Element(loc='/html/body/section/section/section/aside/div/div[1]/div/ul/li[1]/div/span', l_type='XPATH').wait():
        # 点击更多/html/body/section/section/header/div[2]/ul/li[2]/div/span'
        Element(loc='/html/body/section/section/header/div[2]/ul/li[2]/div/span', l_type='XPATH').click()
        # 模拟鼠标悬停
        chain = ActionChains(driver)
        AAA = driver.find_element_by_xpath('/html/body/section/section/header/div[2]/ul/li[2]/div/span')
        chain.move_to_element(AAA).perform()
        # 点击收件箱
        # /html/body/div[2]/ul/div/div/div[1]/ul/li[1]/a
        if Element(loc='/html/body/div/ul/div/div/div[1]/ul/li[1]/a', l_type='XPATH').wait():
            starttime = time.time()
            # 偶尔点击不到收件箱，调用js点击
            # click_link=driver.find_element_by_link_text('公文传送')
            js = driver.find_element_by_xpath('/html/body/div/ul/div/div/div[1]/ul/li[1]/a')
            driver.execute_script("arguments[0].click()", js)

        else:
            add_oper_log('RESULT', case_name, value='0', operator='1', expect_value=moudle_name)
            close_url()
            raise Exception("未找到检查点，链接未找到！")
        # Element(loc = '//*[@text="收件箱"]',l_type = 'XPATH').click()
        # 设置检查点
        if Element(loc='/html/body/section/section/section/main/div/div[2]/div/div[2]/table/thead/tr/th[2]/div',
                   l_type='XPATH').wait():
            # 获取检查点 标题
            # find_element_by_xpath() got an unexpected keyword argument 'l_type'
            #                           /html/body/section/section/header/div[2]/ul/li[2]/div/span
            checkpoint = Element(
                loc='/html/body/section/section/section/main/div/div[2]/div/div[2]/table/thead/tr/th[2]/div',
                l_type='XPATH').value()
            # 输出检查点 标题
            put_out_data('checkpoint', checkpoint)
            # 记录结束时间
            endtime = time.time()
            # 计算耗时
            LogTime = endtime - starttime
            # 记录日志
            add_oper_log('RESULT', case_name, value=str(LogTime), operator='0', expect_value=moudle_name)
            # 关闭浏览器
            close_url()
        else:
            # 记录异常日志
            add_oper_log('RESULT', case_name, value='0', operator='1', expect_value=moudle_name)
            # 抛出异常
            raise Exception("未找到检查点，收件箱打开失败！")
            # 关闭浏览器
            try:
                close_url()
            except:
                pass
    else:
        # 记录异常日志
        add_oper_log('RESULT', case_name, value='0', operator='1', expect_value=moudle_name)
        # 抛出异常
        raise Exception("个人工作台打开失败！")
        # 关闭浏览器
        try:
            close_url()
        except:
            pass
else:
    # 记录异常日志
    add_oper_log('RESULT', case_name, value='0', operator='1', expect_value=moudle_name)
    # 抛出异常
    raise Exception("登录页面打开失败！")
    # 关闭浏览器
    try:
        close_url()
    except:
        pass