#http://59.206.205.214:28082/MessageTransSvc.svc?wsdlgetOrgXmlEsbWebService
import requests
from requests.structures import CaseInsensitiveDict

url = "http://59.206.205.214:28082/MessageTransSvc.svc"

headers = CaseInsensitiveDict()
headers['Content-Type'] = 'text/xml;charset=UTF-8'
headers['SOAPAction'] = 'http://tempuri.org/IMessageTransSvc/GetOrgXmlEsbWebService'

data = '''
<soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:tem="http://tempuri.org/">
   <soapenv:Header/>
   <soapenv:Body>
      <tem:GetOrgXmlEsbWebService>
         <!--Optional:-->
         <tem:transCode>TEM2022092201</tem:transCode>
         <!--Optional:-->
         <tem:organizeId>86191984</tem:organizeId>
      </tem:GetOrgXmlEsbWebService>
   </soapenv:Body>
</soapenv:Envelope>
'''
requests.DEFAULT_RETRIES = 5
s = requests.session()
s.keep_alive = False
response = requests.post(url=url, headers=headers, data=data.encode())
response.encoding = "utf-8"
checkpoint=response.text[200:300]
put_out_data('checkpoint',checkpoint)
close_url()