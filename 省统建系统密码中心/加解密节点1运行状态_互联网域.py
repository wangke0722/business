import requests

url = "http://10.200.170.3:6070/openapi/serverListAll"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
}
params = {
    "appKey": "xO8uSB20hy",
    "appScrect":"b0a7d991f9eba9afb75bad6f770a6395"
}
response = requests.get(url, headers=headers,params=params)
json_data = response.text

data1 = json.loads(json_data)
service = data1['data']

ServerDesc = "开放服务加解密节点1"
matching_dict = None
for item in service:
    if item.get("ServerDesc") == ServerDesc:
        matching_dict = item
        break

if matching_dict:
    pass
else:
    raise Exception(f"返回报文中未找到 '{ServerDesc}',请检查接口是否正常")

name = matching_dict['ServerDesc']
status = matching_dict['RunStatus']

if status == 1:
    pass
else:
    raise Exception(f'{name}运行状态不为1,请检查')
put_out_data('checkpoint',json_data)

close_url()