from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
import scrapy.spiderloader
import scrapy.logformatter
import scrapy
import os
import requests
from urllib.parse import urlparse

process = CrawlerProcess(get_project_settings())
process.crawl('hanime1')  # 替换为实际爬虫名称
process.start()