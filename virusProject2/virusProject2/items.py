# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


# class Virusproject2Item(scrapy.Item):
#     # define the fields for your item here like:
#     # name = scrapy.Field()
#     pass
# main page

class tableItem(scrapy.Item):
    date = scrapy.Field()
    confirmAdd = scrapy.Field()
    mainlandAdd = scrapy.Field()
    overseaAdd = scrapy.Field()
    asymptomaticAdd = scrapy.Field()
    confirmNow = scrapy.Field()
    mainlandNow = scrapy.Field()
    overseaNow = scrapy.Field()
    asymptomaticNow = scrapy.Field()
    confirmSum = scrapy.Field()
    overseaSum = scrapy.Field()
    cureSum = scrapy.Field()
    deathSum = scrapy.Field()


# sub page
class table2Item(scrapy.Item):
    date = scrapy.Field()
    province = scrapy.Field()
    city = scrapy.Field()
    mainlandAdd = scrapy.Field()
    asymptomaticAdd = scrapy.Field()
    confirmAdd = scrapy.Field()
    confirmSum = scrapy.Field()
    cureSum = scrapy.Field()
    deathSum = scrapy.Field()


class table3Item(scrapy.Item):
    date = scrapy.Field()
    province = scrapy.Field()
    confirmAdd = scrapy.Field()
    confirmSum = scrapy.Field()
    cureSum = scrapy.Field()
    deathSum = scrapy.Field()


class dsTableItem(scrapy.Item):
    date = scrapy.Field()
    cases = scrapy.Field()
    death = scrapy.Field()
    recovered = scrapy.Field()


class dsTable2Item(scrapy.Item):
    date = scrapy.Field()
    province = scrapy.Field()
    cases = scrapy.Field()
    death = scrapy.Field()
    recovered = scrapy.Field()

class dsSpTableItem(scrapy.Item):
    date = scrapy.Field()
    province = scrapy.Field()
    cases = scrapy.Field()
    death = scrapy.Field()
    recovered = scrapy.Field()
