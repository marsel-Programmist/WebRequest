import urllib3

def get(url):
    http = urllib3.PoolManager()
    site = http.request('GET', url)
    return site
def post(url, fields):
    http = urllib3.PoolManager()
    site = http.request('POST', url, fields=fields)
    return site
