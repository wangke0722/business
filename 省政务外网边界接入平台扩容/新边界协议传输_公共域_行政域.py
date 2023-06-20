import requests

try:
    s = requests.session()
    s.keep_alive = False
    aaa=requests.get("http://15.33.10.99:1003/#/login")
    aaa.encoding = "utf-8"
    checkpoint=aaa.text
    put_out_data('checkpoint',checkpoint)
    close_url()
except:
    close_url()