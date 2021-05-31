import scrapy

class BballSpider(scrapy.Spider):
    # name the spider
    name = "basketball"
    
    # URLs to scrape
    start_urls = [
        "https://www.basketball-reference.com/players"
    ]

    def __init__(self):

        self.links=[]

    def parse(self, response):
        # Look at seedURLs
        if response.url in self.links:
            pass
        else:
            self.links.append(response.url)
               # Obtain HTMLcontent
            page = response.url.split('/')[-1]
            filename = 'posts-%s.html' % page
            with open('webcrawler/files/%s' %filename, 'wb') as f:
                f.write(response.body)
            for href in response.css('a::attr(href)'):
                yield response.follow(href, self.parse)
        # extract URLs to put onto queue and continuously look at queue to find next url to crawl

        