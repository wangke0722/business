import requests
from requests.structures import CaseInsensitiveDict

url = "http://15.208.0.128/MessageTransSvc.svc"

headers = CaseInsensitiveDict()
headers['Content-Type'] = 'text/xml;charset=UTF-8'
headers['SOAPAction'] = 'http://tempuri.org/IMessageTransSvc/receiveXmlEsbWebService'

data = '''
<soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:tem="http://tempuri.org/">
   <soapenv:Header/>
   <soapenv:Body>
      <tem:receiveXmlEsbWebService>
         <!--Optional:-->
         <tem:transCode>TEM2022092201</tem:transCode>
         <!--Optional:-->
         <tem:receiveType>00</tem:receiveType>
      </tem:receiveXmlEsbWebService>
   </soapenv:Body>
</soapenv:Envelope>
'''
requests.DEFAULT_RETRIES = 5
s = requests.session()
s.keep_alive = False
response = requests.post(url=url, headers=headers, data=data.encode())
print(response.text)
response.encoding = "utf-8"
checkpoint=response.text
put_out_data('checkpoint',checkpoint)
close_url()