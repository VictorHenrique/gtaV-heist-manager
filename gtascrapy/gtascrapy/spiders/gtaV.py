import scrapy
import re


class GtavSpider(scrapy.Spider):
    name = 'gtaV'
    allowed_domains = ['gta.fandom.com']
    start_urls = ['https://gta.fandom.com/wiki/Heists_in_GTA_Online']
    heists = set()

    def filter_links(self, links):
        for s in links:
            try: 
                # print("yey")
                self.heists.add(re.search(r'(.*\/wiki\/Casino_Heist.*)', s).group(0))
            except: 
                continue

    def parse(self, response):   
        # Heist Update and Doomsday Heist
        links = response.css('table[class="wikitable"] tbody tr a::attr(href)').getall()
        for link in links:
            if "wiki/" in link:
                self.heists.add(link)

        # Diamond Casino Heist
        links = self.filter_links(response.css('a::attr(href)').getall())