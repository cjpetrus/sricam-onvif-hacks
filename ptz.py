import requests
XMAX = 1
XMIN = -1
YMAX = 1
YMIN = -1
class Camera:
    def __init__(self, ip='10.0.0.115', port='5000', user='', passwd=''):
        self.ptz_body = """<soap:Envelope xmlns:soap="http://www.w3.org/2003/05/soap-envelope" xmlns:wsdl="http://www.onvif.org/ver20/ptz/wsdl" xmlns:sch="http://www.onvif.org/ver10/schema">
   <soap:Header/>
   <soap:Body>
      <wsdl:ContinuousMove>
         <wsdl:Velocity>
            <!--Optional:-->
            <sch:PanTilt x="{}" y="{}" space="{}"/>
         </wsdl:Velocity>
         <!--Optional:-->
      </wsdl:ContinuousMove>
   </soap:Body>
</soap:Envelope>"""
        self.headers = {'content-type': 'text/xml', 'passwd': passwd, 'port': port, 'user': user}
        self.url = 'http://{}:{}/'.format(ip, port)


    def move_up(self,  timeout=1):
        print 'move up...'
        x = 0
        y = YMAX

        response = requests.post(self.url, data=self.ptz_body.format(x, y, '0'), headers=self.headers)
        print response

    def move_down(self,  timeout=1):
        print 'move down...'
        x = 0
        y = YMIN

        response = requests.post(self.url, data=self.ptz_body.format(x, y, '0'), headers=self.headers)
        print response

    def move_right(self,  timeout=1):
        print 'move right...'
        x = XMAX
        y = 0

        response = requests.post(self.url, data=self.ptz_body.format(x, y, '0'), headers=self.headers)
        print response

    def move_left(self,  timeout=1):
        print 'move left...'
        x = XMIN
        y = 0
        response = requests.post(self.url, data=self.ptz_body.format(x, y, '0'), headers=self.headers)
        print response


