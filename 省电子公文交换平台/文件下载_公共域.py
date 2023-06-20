import requests
from requests.structures import CaseInsensitiveDict

url = "http://59.206.205.214:28082/MessageTransSvc.svc"

headers = CaseInsensitiveDict()
headers['Content-Type'] = 'text/xml;charset=UTF-8'
headers['SOAPAction'] = 'http://tempuri.org/IMessageTransSvc/DownLoadMessage'

#http://15.208.0.128:80/MessageTransSvc.svc?wsdl    DownLoadMessage
data = '''
<soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:tem="http://tempuri.org/">
   <soapenv:Header/>
   <soapenv:Body>
      <tem:DownLoadMessage>
         <!--Optional:-->
         <tem:transCode>TEM2022092201</tem:transCode>
         <!--Optional:-->
         <tem:fileId>6692fbc6-8960-41c2-9eca-6efd70f1dab9</tem:fileId>
      </tem:DownLoadMessage>
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