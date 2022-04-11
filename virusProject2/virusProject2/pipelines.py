# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter

import pymysql
from itemadapter import ItemAdapter
from .items import tableItem
from .items import table2Item
from .items import table3Item
from .items import dsTable2Item
from .items import dsTableItem
from .items import dsSpTableItem


class MysqlPipeline():
    def __init__(self, host, database, user, password, port):
        self.host = host
        self.database = database
        self.user = user
        self.password = password
        self.port = port

    # 连接数据库
    @classmethod
    def from_crawler(cls, crawler):
        return cls(
            host=crawler.settings.get('MYSQL_HOST'),
            database=crawler.settings.get('MYSQL_DATABASE'),
            user=crawler.settings.get('MYSQL_USER'),
            password=crawler.settings.get('MYSQL_PASSWORD'),
            port=crawler.settings.get('MYSQL_PORT'),
        )

    def open_spider(self, spider):
        self.db = pymysql.connect(host=self.host, user=self.user, password=self.password, database=self.database,
                                  charset='utf8', port=self.port)
        self.cursor = self.db.cursor()

    def close_spider(self, spider):
        self.db.close()

    # 插入记录
    def process_item(self, item, spider):
        if isinstance(item, tableItem):
            table = "bd_table"
        if isinstance(item, table2Item):
            table = "bd_table2"
        if isinstance(item, table3Item):
            table = "bd_table3"
        if isinstance(item, dsTableItem):
            table = "ds_table"
        if isinstance(item, dsTable2Item):
            table = "ds_table2"
        if isinstance(item, dsSpTableItem):
            table = "ds_sp_table"

        data = dict(item)
        keys = ', '.join(data.keys())
        values = ', '.join(['%s'] * len(data))
        sql = 'insert into %s (%s) values (%s)' % (table, keys, values)
        self.cursor.execute(sql, tuple(data.values()))
        self.db.commit()
        return item
