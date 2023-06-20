from selenium import webdriver
#入参定义
region=${region}
#打开网址 http://124.128.58.241/qingdao/index
try:
    open_url("http://124.128.58.241/"+region+"/index")
except:
    pass

sleep(1)
driver = get_driver()
title = driver.title
i=1
while i<5:
    if "数据开放网" in title:
        break
    else:
        try:
            driver.get("http://124.128.58.241/"+region+"/index")
        except:
            pass
        sleep(1)
        title = driver.title
        i=i+1

checkpoint= driver.title
put_out_data('checkpoint',checkpoint)
close_url()