import requests

try:
    s = requests.session()
    s.keep_alive = False
    aaa=requests.get("http://59.206.243.243:8080/login.do")
    # 获取响应码
    status_code = aaa.status_code
    aaa.encoding = "gbk"
    checkpoint=aaa.text.lstrip()
    checkpoint1=status_code
    put_out_data('checkpoint',checkpoint)
    put_out_data('checkpoint1',checkpoint1)
    close_url()
except:
    close_url()