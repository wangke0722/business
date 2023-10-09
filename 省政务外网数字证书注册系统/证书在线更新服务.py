import requests

try:
    s = requests.session()
    s.keep_alive = False
    aaa=requests.get("http://59.206.243.244:8080/app/installCert/;jsessionid=13F5A5227BCC7226A8D7228E9A7EAEED")
    # 获取响应码
    status_code = aaa.status_code
    aaa.encoding = "utf-8"
    checkpoint=aaa.text
    checkpoint1=status_code
    put_out_data('checkpoint',checkpoint)
    put_out_data('checkpoint1',checkpoint1)
    close_url()
except:
    close_url()