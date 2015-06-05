import scrapy

from ImCollector.items import ImageItem

class GoogleImageSpider(scrapy.Spider):
    name = 'google'
    allowed_domains = ['google.com']

    def __init__(self, key="eyes", max_count=100):
        self.key = key.replace(" ", "+")
        self.ijn = 0
        self.cur_count = 0
        self.max_count = int(max_count)
        self.start_urls = [
                "https://www.google.com/search?q={0}&tbm=isch&ijn={1}&start={2}".format(self.key, self.ijn, self.ijn*100),
                ]
    
    def parse(self, response):
        item = ImageItem()
        item['image_urls'] = response.xpath('//img/@data-src').extract()[:self.max_count - self.cur_count]
        c = len(item['image_urls'])
        if c == 0:
            print "No more results!"
            return
        self.cur_count = self.cur_count + c
        yield item
        if self.cur_count < self.max_count:
            self.ijn = self.ijn + 1
            yield scrapy.Request("https://www.google.com/search?q={0}&tbm=isch&ijn={1}&start={2}".format(self.key, self.ijn, self.ijn*100))
