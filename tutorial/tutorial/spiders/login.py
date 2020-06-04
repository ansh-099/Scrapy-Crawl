import scrapy
from ..items import TutorialItem
from scrapy.http import FormRequest

class Quotes(scrapy.Spider):
    name = 'quotes_login'
    start_urls = [
        'http://quotes.toscrape.com/login'
    ]

    def parse(self, response):
        token = response.css("form input::attr('value')").extract_first()
        print("TOKEN: ",token)
        return FormRequest.from_response(response, formdata= {
            'csrf_token': token,
            'username': 'dasdqwasda',
            'password': 'adzdcds'
        },callback= self.start_scraping)

    def start_scraping(self, response):
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
    

