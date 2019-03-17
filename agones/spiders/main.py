import scrapy as sp
import itertools as it

class Agones(sp.Spider):
    name = "agones"

    start_urls = ['https://agones.gr']

    def parse(self, response):

        teams = response.xpath('//td[@class="column-green2"]/a[text()[re:test(., "^[α-ωίϊΐόάέύϋΰήώΑ-ΩΆΊΌΎΉΏ.\s]*$")]]/text()').getall()
        
        #teams_space = [' '.join(x) for x in zip(teams[0::2], teams[1::2])]
        
        hosts, away = teams[::2], teams[1::2]

        for h, a in  zip(hosts, away):
            yield {
                'host': h,
                'guest':a 
            }

