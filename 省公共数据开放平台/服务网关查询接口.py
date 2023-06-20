import time
import uuid
from hashlib import sha256
import hmac, base64
import http.client
import requests

def get_sha256(data, key):
    key = key.encode('utf-8')       # sha256加密的key
    message = data.encode('utf-8')  # 待sha256加密的内容
    sign = base64.b64encode(hmac.new(key, message, digestmod=sha256).digest()).decode()
    return sign


client_id = '8f394252558d43a4ad53f2d9ab3c04ba'
client_secret = '7f08cdb56f114a689558d6f7f2052e88'
#获取当前时间戳
timestamp = str(round(time.time() * 1000))
print(timestamp)
logging.info(timestamp)
#随机数
nonce = str(uuid.uuid4())
print(nonce)
logging.info(nonce)
#生成签名
textToSign = client_id + timestamp + nonce
signature = get_sha256(textToSign,client_secret)
print(signature)
logging.info(signature)
#cataLog_2598956f48bb4bc8abc4fcb8b60de00c
#conn = http.client.HTTPSConnection("https://data.sd.gov.cn/gateway/api/1.0/cataLog_7f08cdb56f114a689558d6f7f2052e88/get_data_count")
#conn.request("POST", headers={"X-Client-Id": client_id, "X-Timestamp": timestamp, "X-Nonce": nonce, "X-Signature": signature})
#resp = conn.getresponse()
headers={"Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9","Accept-Encoding":"gzip, deflate, br","Accept-Language":"zh-CN,zh;q=0.9","Cache-Control":"max-age=0","Connection":"keep-alive","Host":"data.sd.gov.cn","User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36","X-Client-Id": client_id, "X-Timestamp": timestamp, "X-Nonce": nonce, "X-Signature": signature}
r=requests.get("https://data.sd.gov.cn/gateway/api/1.0/cataLog_2598956f48bb4bc8abc4fcb8b60de00c/get_data_count",headers=headers,data="")
#print(resp.read().decode("UTF-8"))
#logging.info(resp.read().decode("UTF-8"))
logging.info(r.text)
#conn.close()
put_out_data('checkpoint',r.text)
close_url()