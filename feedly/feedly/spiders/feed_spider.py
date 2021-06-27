import scrapy
import json


class FeedSpider(scrapy.Spider):
    name = "feeds"

    def start_requests(self):
        f = open('feeds_link.json', )
        feeds = json.load(f)
        for feed in feeds:
            yield scrapy.Request(url=feed['url'], callback=self.parse)

    def parse(self, response):
        feed = response.css('channel > title::text').get()
        for item in response.css('item'):
            content = item.xpath("./content:encoded",
                                 namespaces={'content': 'http://purl.org/rss/1.0/modules/content/'}).get()
            author = item.css('author::text').get()
            content = content if content else ''
            author = author if author else ''
            yield {
                "title": item.css('title::text').get(),
                "link": item.css('link::text').get(),
                "description": item.css('description::text').get(),
                "content": content,
                "author": author,
                "feed": feed
            }
