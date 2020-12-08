import requests
from bs4 import BeautifulSoup
import concurrent.futures


class scrape_freeproxylists:
    def __init__(self):
        self.URL = "https://free-proxy-list.net/"
        self.valid_proxies = []

    def get_proxies(self):
        r = requests.get(self.URL)
        soup = BeautifulSoup(r.content, 'html.parser')
        table = soup.find('tbody')
        proxies = []
        for row in table:
            if row.find_all('td')[4].text == 'elite proxy':
                proxy = ':'.join([row.find_all('td')[0].text,
                                  row.find_all('td')[1].text])
                proxies.append(proxy)
            else:
                pass
        self.proxyList = proxies
        return self.proxyList

    def validate_proxy(self, proxy):
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:80.0) Gecko/20100101 Firefox/80.0'}
        r = requests.get('https://httpbin.org/ip', headers=headers,
                         proxies={'http': proxy, 'https': proxy}, timeout=3)
        if r.status_code == 200:
            return proxy

    def get_valid_proxies(self):
        proxy_list = self.get_proxies()
        only_valid_proxies_list = []
        with concurrent.futures.ThreadPoolExecutor(max_workers=30) as executor:
            future_to_url = {executor.submit(
                self.validate_proxy, proxy): proxy for proxy in proxy_list}
            for future in concurrent.futures.as_completed(future_to_url):
                proxy = future_to_url[future]

                try:
                    valid_proxy = future.result()
                    self.valid_proxies.append(valid_proxy)
                except Exception as exc:
                    pass
        