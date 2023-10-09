import requests
import json

url1 = "http://10.200.198.170:31684/apisix/plugin/jwt/sign"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
}
params = {
    "key": "i9ybgzkq88tisj0d"
}
response = requests.get(url1, headers=headers,params=params)
token = response.text
put_out_data('checkpoint1',token)

url2 = "http://10.200.198.170:31684/tna-cipher/v1/resource/condition"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3",
    "Authorization": token
}

response = requests.get(url2, headers=headers)
json_data = response.text

data = json.loads(json_data)

name = "得安签名验签服务器"
matching_dict = None
for item in data:
    if item.get("DeviceName") == name:
        matching_dict = item
        break

if matching_dict:
    pass
else:
    raise Exception(f"返回报文中未找到'{name}',请检查接口是否正常")

name = matching_dict['DeviceName']
status = matching_dict['DeviceStatus']
if status == 1:
    pass
else:
    raise Exception(f'{name}状态显示异常，请检查')

put_out_data('checkpoint2',json_data)
#logging.info(data2)
close_url()