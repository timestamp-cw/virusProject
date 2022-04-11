import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from urllib.parse import unquote
import re
from ..items import tableItem
from ..items import table2Item
from ..items import table3Item


class SpiderBdSpider(scrapy.Spider):
    name = 'spider_bd'
    allowed_domains = ['voice.baidu.com']
    start_urls = ['https://voice.baidu.com/act/newpneumonia/newpneumonia']

    custom_settings = {
        # 设置下载器中间件
        'DOWNLOADER_MIDDLEWARES':{
            'virusProject2.middlewares.SpiderBdDownloaderMiddleware': 543,
        },
        # 设置管道下载
        'ITEM_PIPELINES': {
            'virusProject2.pipelines.MysqlPipeline': 300,
        },
        # 设置log日志
        'LOG_LEVEL':'INFO',
        'LOG_FILE':r'../virusProject2/logs/spider_bd.log'
    }

    pattern = re.compile(r"\d+.\d+.\d+")
    pattern2 = re.compile(r"=(.*)-(.*)")

    def parse(self, response):
        print(response.url)
        print("主页面: " + response.url)
        base_url = self.start_urls[0]
        # item
        strList = response.xpath('//div[@id="ptab-0"]/div[1]//text()').getall()
        strList = [z.replace(",", "") for z in strList]
        date = self.pattern.search(strList[1])[0].replace(".", "")
        confirmAdd = strList[4]
        mainlandAdd = strList[6]
        overseaAdd = strList[8]
        asymptomaticAdd = strList[10]
        confirmNow = strList[12]
        mainlandNow = strList[14]
        overseaNow = strList[16]
        asymptomaticNow = strList[18]
        confirmSum = strList[20]
        overseaSum = strList[24]
        cureSum = strList[28]
        deathSum = strList[32]
        # tableItem
        item = tableItem()
        item['date'] = int(date)
        item['confirmAdd'] = int(confirmAdd)
        item['mainlandAdd'] = int(mainlandAdd)
        item['overseaAdd'] = int(overseaAdd)
        item['asymptomaticAdd'] = int(asymptomaticAdd)
        item['confirmNow'] = int(confirmNow)
        item['mainlandNow'] = int(mainlandNow)
        item['overseaNow'] = int(overseaNow)
        item['asymptomaticNow'] = int(asymptomaticNow)
        item['confirmSum'] = int(confirmSum)
        item['overseaSum'] = int(overseaSum)
        item['cureSum'] = int(cureSum)
        item['deathSum'] = int(deathSum)
        yield item

        # table3Item
        strList3 = response.xpath('//div[@id="nationTable"]/table/tbody/tr[contains(@class,"Virus")]//text()').getall()
        # print(strList3)
        item3 = table3Item()
        date3 = date
        for i in range(1, int(len(strList3) / 5) + 1):
            province3 = strList3[5 * i - 5]
            confirmAdd3 = strList3[5 * i - 4]
            confirmSum3 = strList3[5 * i - 3]
            cureSum3 = strList3[5 * i - 2]
            deathSum3 = strList3[5 * i - 1]
            item3['date'] = int(date3)
            item3['province'] = province3
            item3['confirmAdd'] = int(confirmAdd3)
            item3['confirmSum'] = int(confirmSum3)
            item3['cureSum'] = int(cureSum3)
            item3['deathSum'] = int(deathSum3)
            yield item3
        # sub page links
        urlList = response.xpath('//div[@id="nationTable"]/table/tbody//a/@href').getall()
        # print(urlList)
        for url in urlList:
            full_url = base_url + url
            yield scrapy.Request(url=full_url, callback=self.parse_sub_page, encoding="utf8")

    def parse_sub_page(self, response):
        print("子页面: " + response.url)
        res = self.pattern2.search(unquote(response.url))
        print(res.group(1) + " : " + res.group(2))
        # item
        strList = response.xpath('//div[@id="ptab-0"]//text()').getall()
        # print(strList)
        strList = [z.replace(",", "") for z in strList]
        province = res.group(1)
        city = res.group(2)
        date = self.pattern.search(strList[1])[0].replace(".", "")
        mainlandAdd = strList[4]
        asymptomaticAdd = strList[6]
        confirmAdd = strList[8]
        confirmSum = strList[10]
        cureSum = strList[12]
        deathSum = strList[14]
        # table2Item
        item = table2Item()
        item['province'] = province
        item['city'] = city
        item['date'] = int(date)
        item['mainlandAdd'] = int(mainlandAdd)
        item['asymptomaticAdd'] = int(asymptomaticAdd)
        item['confirmAdd'] = int(confirmAdd)
        item['confirmSum'] = int(confirmSum)
        item['cureSum'] = int(cureSum)
        item['deathSum'] = int(deathSum)
        yield item


