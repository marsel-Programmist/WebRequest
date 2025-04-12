import urllib3

def get(url):
    http = urllib3.PoolManager()
    site = http.request('GET', url)
    return site.data
def get(url, text):
    http = urllib3.PoolManager()
    site = http.request('POST', url, fields=text)
    return site.data
