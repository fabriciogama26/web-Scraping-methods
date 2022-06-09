import scrapy
from scrapy.crawler import CrawlerProcess

url = "https://www.ligamagic.com.br/?view=cards/search&card=ed%3Dclb"

class Cards(scrapy.Spider):
    name = "mtgcards"

    def start_requests(self):
        yield scrapy.Request(url)

    def parse(self, response):
        namecards = response.css('div.grid-cardsinput')
        for item in namecards:
            yield {
                'name': item.css('span.invisible-label::text').get(),
                'price': item.css('div.avgp-minprc::text').get()
            }

        #for x in range(1,20): #( caso tenha varias paginas)
            
            #yield (scrapy.Request(url"https://www.ligamagic.com.br/?view=cards/search&card=ed%3Dclb", callback=self.parse))

process = CrawlerProcess(settings={'FEEDS':{'mtgcards.csv': {'format': 'csv'}}})

process.crawl(Cards)
process.start()