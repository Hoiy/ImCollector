import scrapy

from ImCollector.items import ImageItem

class GoogleImageSpider(scrapy.Spider):
    name = 'google'
    allowed_domains = ['google.com']

    def __init__(self, key="eyes", max_count=100):
        self.key = key.replace(" ", "+")
        self.cur_count = 0
        self.max_count = int(max_count)
        self.start = 0
        self.start_urls = [self.createQuery(self.key, self.start)]

    def createQuery(self, key, start):
        link = "https://www.google.com/search?q={0}&tbm=isch&ijn=0&start={1}".format(key, start)
        return link

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
            self.start = self.start + c
            yield scrapy.Request(self.createQuery(self.key, self.start))
