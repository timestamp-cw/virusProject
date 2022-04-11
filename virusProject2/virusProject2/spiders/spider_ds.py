import json

import pandas
import scrapy
from ..items import dsTableItem
from ..items import dsTable2Item
import re

class SpiderDsSpider(scrapy.Spider):
    name = 'spider_ds'
    allowed_domains = ['disease.sh']
    start_urls = ['https://disease.sh/v3/covid-19/historical/china?lastdays=all']

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
        'LOG_LEVEL': 'INFO',
        'LOG_FILE': r'../virusProject2/logs/spider_ds.log'
    }

    pattern = re.compile(r"(\d+)/(\d+)/(\d+)")

    def parse(self, response):
        print(response.url)
        data = json.loads(response.body.decode("utf8"))
        dateList = list(data["timeline"]["cases"].keys())
        # print(dateList)
        date2List = []
        for date in dateList:
            res = self.pattern.search(date)
            date = "{0:0>2d}{1:0>2d}{2:0>2d}".format(int(res.group(3)),int(res.group(1)),int(res.group(2)))
            date2List.append(date)
        casesList = list(data["timeline"]["cases"].values())
        deathList = list(data["timeline"]["deaths"].values())
        recoveredList = list(data["timeline"]["recovered"].values())
        item = dsTableItem()
        for i in range(len(dateList)):
            item["date"] = int(date2List[i])
            item["cases"] = int(casesList[i])
            item["death"] = int(deathList[i])
            item["recovered"] = int(recoveredList[i])
            yield item

        # province url
        provinceList = data["province"]
        url = "https://disease.sh/v3/covid-19/historical/china/{0}?lastdays=all"
        for province in provinceList:
            province_url = url.format(province)
            yield scrapy.Request(url=province_url,callback=self.parse_province_json,encoding="utf8")

    def parse_province_json(self, response):
        data = json.loads(response.body.decode("utf8"))
        # print(data["province"])
        province = data["province"]
        dateList = list(data["timeline"]["cases"].keys())
        date2List = []
        for date in dateList:
            res = self.pattern.search(date)
            date = "{0:0>2d}{1:0>2d}{2:0>2d}".format(int(res.group(3)),int(res.group(1)),int(res.group(2)))
            date2List.append(date)
        casesList = list(data["timeline"]["cases"].values())
        deathList = list(data["timeline"]["deaths"].values())
        recoveredList = list(data["timeline"]["recovered"].values())
        item = dsTable2Item()
        item["province"] = province
        for i in range(len(dateList)):
            item["date"] = int(date2List[i])
            item["cases"] = int(casesList[i])
            item["death"] = int(deathList[i])
            item["recovered"] = int(recoveredList[i])
            yield item



