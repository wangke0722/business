import requests

url = "http://10.210.99.3:6070/openapi/serverListAll"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
}
params = {
    "appKey": "UFpXM25ilH",
    "appScrect":"eeb4194dc918d18f4d14f6dbb4757d3b"
}
response = requests.get(url, headers=headers,params=params)
json_data = response.text

data1 = json.loads(json_data)
service = data1['data']

ServerDesc = "开放服务时间戳节点1"
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