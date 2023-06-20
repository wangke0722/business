import requests
from requests.structures import CaseInsensitiveDict

url = "http://59.206.205.214:28082/MessageTransSvc.svc"

headers = CaseInsensitiveDict()
headers['Content-Type'] = 'text/xml;charset=UTF-8'
headers['SOAPAction'] = 'http://tempuri.org/IMessageTransSvc/getIncrementOrganizeInfo'

#http://15.208.0.128:80/MessageTransSvc.svc?wsdl    DownLoadMessage
data = '''
<soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:tem="http://tempuri.org/">
   <soapenv:Header/>
   <soapenv:Body>
      <tem:getIncrementOrganizeInfo>
         <!--Optional:-->
         <tem:transCode>TEM2022092201</tem:transCode>
         <!--Optional:-->
         <tem:startDate>2022-12-22</tem:startDate>
         <!--Optional:-->
         <tem:endDate>2022-12-23</tem:endDate>
         <!--Optional:-->
         <tem:opFlag>all</tem:opFlag>
      </tem:getIncrementOrganizeInfo>
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