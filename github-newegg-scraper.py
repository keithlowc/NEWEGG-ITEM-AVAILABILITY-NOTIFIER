import scrapy

## Created by Keith Low

##Scrapes any item from newegg. Takes the prices and characteristics

class newegg_gpus(scrapy.Spider):
	#DOWNLOAD_DELAY = 3
	name = 'newegg' ## Does not need to be changed
	link = 'https://www.newegg.com/Product/ProductList.aspx?Submit=ENE&N=-1&IsNodeId=1&Description=wifi%20dongle&bop=And&Page=2&PageSize=36&order=BESTMATCH' ## Should be changed to
	#desired link
	start_urls = [link]

	################### Anti-ban measurements ###################

	#Cookies are enabled True by default
	COOKIES_ENABLED = False
	#Download delay to not get banned
	DOWNLOAD_DELAY = 1.5
	AUTOTHROTTLE_ENABLED = True
	AUTOTHROTTLE_START_DELAY = 2
	AUTOTHROTTLE_TARGET_CONCURRENCY = 6

	################### Anti-ban measurements ###################

	def parse(self,response):
		SET_SELECTOR = '.item-container'
		for item in response.css(SET_SELECTOR):
			TITLE_SELECTOR = 'a.item-title ::text'
			LINK_SELECTOR = 'a.item-title ::attr(href)'
			PRICE_SELECTOR = 'li.price-current strong::text'
			yield{
				'title': item.css(TITLE_SELECTOR).extract_first(),
				'link': item.css(LINK_SELECTOR).extract_first(),
				'price': item.css(PRICE_SELECTOR).extract_first(),
			}
