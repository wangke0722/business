import requests

aaa=requests.get("http://localhost:38081/verifyFile?path=C:\dianziyinzhang/test1.pdf&type=pdf")
aaa.encoding = "utf-8"
checkpoint=aaa.text
put_out_data('checkpoint',checkpoint)
close_url()