from selenium import webdriver

#打开网址 http://124.128.58.241/qingdao/index
driver = get_driver()
try:
    open_url("http://124.128.58.240/portal/index")
except:
    pass

checkpoint = driver.title
put_out_data('checkpoint',checkpoint)
close_url()