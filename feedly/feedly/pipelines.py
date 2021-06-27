# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class FeedlyPipeline:
    def process_item(self, item, spider):
        print('***********++++++++++++++')
        import json
        import requests
        headers = {'Content-Type': 'application/json'}
        result = requests.post('http://127.0.0.1:8000/feed/scrapy', data=json.dumps(item), headers=headers)
        if result.status_code != 201:
            print("ERROR>>>> {}".format(json.loads(result.content)))
        return item
