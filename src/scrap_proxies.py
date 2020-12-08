import requests
from bs4 import BeautifulSoup


class scrape_freeproxylists:
    def __init__(self):
        self.URL = "https://free-proxy-list.net/"

    def getProxies(self):
        r = requests.get( self.URL )
        soup = BeautifulSoup(r.content, 'html.parser')
        table = soup.find('tbody')
        proxies = []
        for row in table:
            if row.find_all('td')[4].text =='elite proxy':
                proxy = ':'.join([row.find_all('td')[0].text, row.find_all('td')[1].text])
                proxies.append(proxy)
            else:
                pass
        self.proxyList = proxies
        return self.proxyList

