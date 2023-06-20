import requests

s = requests.session()
s.keep_alive = False
aaa=requests.get("http://172.30.224.2:38999/#/login")
aaa.encoding = "utf-8"
checkpoint=aaa.text
put_out_data('checkpoint',checkpoint)
close_url()