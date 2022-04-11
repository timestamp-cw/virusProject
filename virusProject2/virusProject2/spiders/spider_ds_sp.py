import scrapy
import json
from ..items import dsSpTableItem
import re

class SpiderDsSpSpider(scrapy.Spider):
    name = 'spider_ds_sp'
    allowed_domains = ['disease.sh']
    start_urls = ['https://disease.sh/v3/covid-19/historical/china?lastdays=all']
    date = "4/9/22"
    pattern = re.compile(r"(\d+)/(\d+)/(\d+)")

    custom_settings = {
        # # 设置下载器中间件
        # 'DOWNLOADER_MIDDLEWARES': {
        #     'virusProject2.middlewares.SpiderDsDownloaderMiddleware': 543,
        # },
        # # 设置管道下载
        'ITEM_PIPELINES': {
            'virusProject2.pipelines.MysqlPipeline': 300,
        },
        # # 设置log日志
        # 'LOG_LEVEL': 'INFO',
        # 'LOG_FILE': r'../virusProject2/logs/spider_ds.log'
    }

    def parse(self, response):
        print(response.url)
        data = json.loads(response.body.decode("utf8"))
        # province url
        provinceList = data["province"]
        url = "https://disease.sh/v3/covid-19/historical/china/{0}?lastdays=all"
        for province in provinceList:
            province_url = url.format(province)
            yield scrapy.Request(url=province_url, callback=self.parse_province_json, encoding="utf8",meta={"date":self.date})

    def parse_province_json(self, response):
        data = json.loads(response.body.decode("utf8"))
        # print(data["province"])
        date = response.meta.get("date")
        res = self.pattern.search(date)
        date2 = "{0:0>2d}{1:0>2d}{2:0>2d}".format(int(res.group(3)), int(res.group(1)), int(res.group(2)))
        province = data["province"]
        casesDict = dict(data["timeline"]["cases"])
        recoveredDict = dict(data["timeline"]["recovered"])
        deathDict = dict(data["timeline"]["deaths"])
        item = dsSpTableItem()
        item['date'] = date2
        item['province'] = province
        item['cases'] = casesDict.get(date)
        item['recovered'] = recoveredDict.get(date)
        item['death'] = deathDict.get(date)
        yield item
