from scraping.scrap_proxies import scrape_freeproxylists

proxyScraper = scrape_freeproxylists()


list_of_proxies =  proxyScraper.get_valid_proxies()

print( list_of_proxies )