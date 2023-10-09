import requests

url = "http://10.210.99.3:6070/openapi/serverName"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
}
params = {
    "appKey": "UFpXM25ilH",
    "appScrect":"eeb4194dc918d18f4d14f6dbb4757d3b",
    "serverName":"cop-mg"
}
response = requests.get(url, headers=headers,params=params)
put_out_data('checkpoint',response.text)
#logging.info(data2)
close_url()