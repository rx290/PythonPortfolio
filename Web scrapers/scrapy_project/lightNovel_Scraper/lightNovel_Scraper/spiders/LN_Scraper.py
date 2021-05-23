import scrapy
# from  items import LightnovelScrapperItem
from lightNovel_Scraper.items import LightnovelScraperItem

class LnScraperSpider(scrapy.Spider):
    name = 'LN_Scraper'
    allowed_domains = ['https://readnovelfull.com/tensei-shitara-slime-datta-ken/prologue.html']
    start_urls = ['https://readnovelfull.com/tensei-shitara-slime-datta-ken/prologue.html']

    def parse(self, response):
        chapters = LightnovelScraperItem() 
        title= response.css('span.chr-text::text').get(),
        content= response.css('div.chr-c').get(),
        
        yield chapters
