import requests

url = "http://10.200.170.3:6070/openapi/serverName"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
}
params = {
    "appKey": "xO8uSB20hy",
    "appScrect":"b0a7d991f9eba9afb75bad6f770a6395",
    "serverName":"cop-mg"
}
response = requests.get(url, headers=headers,params=params)
put_out_data('checkpoint',response.text)
#logging.info(data2)
close_url()