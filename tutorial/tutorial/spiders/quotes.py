import scrapy
from ..items import TutorialItem

class Quotes(scrapy.Spider):
    name = 'quotes'
    start_urls = [
        'http://quotes.toscrape.com/'
    ]

    def parse(self, response):

        items = TutorialItem()

        # fetch title
        title = response.css('title::text').extract()
        print("TITLE:",title)
        print()

        # fetch all 
        all = response.css("div.quote")
        print("ALL:", all)
        print()

        for i in all:
            # get names
            names = i.css("span.text::text").extract()
            print("NAMES:", names)
            print()

            author = i.css('span small.author::text').extract()
            print('AUTHOR:',author)
            print()

            items['title'] = title
            items['author'] = author
            items['names'] = names

            yield items
        
        next_page = response.css('li.next a::attr(href)').get()

        if next_page is not None:
            yield response.follow(next_page, callback= self.parse)
        

