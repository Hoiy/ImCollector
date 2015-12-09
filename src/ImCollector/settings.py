# -*- coding: utf-8 -*-

# Scrapy settings for ImCollector project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'ImCollector'

SPIDER_MODULES = ['ImCollector.spiders']
NEWSPIDER_MODULE = 'ImCollector.spiders'

ITEM_PIPELINES = {'scrapy.contrib.pipeline.images.ImagesPipeline': 1}
IMAGES_STORE = 'ImStore'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'ImCollector (+http://www.yourdomain.com)'
