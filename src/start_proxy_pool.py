from scraping.scrap_proxies import scrape_freeproxylists
import requests
from itertools import cycle

print("Scrapping proxies...")
proxyScraper = scrape_freeproxylists()

list_of_proxies =  proxyScraper.get_valid_proxies()

proxy_pool = cycle( list_of_proxies )

print("Starting the requests...")
for i in range(0, 10):
    url = "https://httpbin.org/ip" 

    proxy = next(proxy_pool)
    try:
        response = requests.get(url,proxies={"http": proxy, "https": proxy}, timeout=5)
        print("Request Origin:", response.json() )
    except:
        # if the request fails, the proxy is removed from the pool
        list_of_proxies.remove(proxy)
