import scrapy

class testSpider(scrapy.Spider):
    name = 'scraper'
    start_urls =[]

    def __init__(self, start_url=None, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if start_url:
            self.start_urls.append(start_url)

    if("manilatimes.net" in start_urls) :  
        def parse(self, response):
            test = response.css('div.wordpay-ad-original-content').get()
            return {
                'words': test
            }
    if("inquirer.net" in start_urls):
        def parse(self, response):
            test = response.css('div.article-content').get()
            return {
                'words': test
            }
    if("bworldonline.com" in start_urls ): 
        def parse(self, response):
            test = response.css('div.td-post-content').get()
            return {
                'words': test
            }
    if("eaglenews.ph" in start_urls):
        def parse(self, response):
            test = response.css('div.entry-content').get()
            return {
                'words': test
            }
    if("mb.com.ph" in start_urls):
        def parse(self, response):
            test = response.css('section.article-content').get()
            return {
                'words': test
            }
    if("bulatlat.com" in start_urls):
        def parse(self, response):
            test = response.css('div.entry-content').get()
            return {
                'words': test
            }
    if("philstar.com" in start_urls):
        def parse(self, response):
            test = response.css('div.sports_article_content').get()
            return {
                'words': test
            }
    if("sunstar.com.ph" in start_urls):
        def parse(self, response):
            test = response.css('div.article-body').get()
            return {
                'words': test
            }  
    if("malaya.com.ph" in start_urls):
        def parse(self, response):
            test = response.css('div.td-post-content').get()
            return {
                'words': test
            }
    if("journal.com.ph" in start_urls):
        def parse(self, response):
            test = response.css('div.entry-content').get()
            return {
                'words': test
            }
    if("rodsmann.github.io" in start_urls):
        def parse(self, response):
            test = response.css('div.paragraph').get()
            return {
                'words': test
            }
                    
    if("journal.com.ph" or "malaya.com.ph" or "sunstar.com.ph" or
         "philstar.com" or "bulatlat.com" or "mb.com.ph" or
         "eaglenews.ph" or "bworldonline.com" or "inquirer.net" or "manilatimes.net" or "rodsmann.github.io" not in start_urls):
        def parse(self, response):
            return {
                'message': "This Site is not supported"
            }