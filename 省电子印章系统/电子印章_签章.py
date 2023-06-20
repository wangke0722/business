import requests

aaa=requests.get("http://10.200.56.125:38081/signPdf?path=C:\dianziyinzhang/test.pdf&type=position")
aaa.encoding = "utf-8"
checkpoint=aaa.text
put_out_data('checkpoint',checkpoint)
close_url()