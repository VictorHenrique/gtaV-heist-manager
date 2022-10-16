import scrapy


class GtavSpider(scrapy.Spider):
    name = 'gtaV'
    allowed_domains = ['gta.fandom.com']
    start_urls = ['https://gta.fandom.com/wiki/Heists_in_GTA_Online']

    heists = []
    def parse(self, response):
        links = response.css('table[class="wikitable"] tbody tr a::attr(href)').getall()
        for link in links:
            if "wiki/" in link:
                print("Heist found!")
                self.heists.append(link)
        print(self.heists)
