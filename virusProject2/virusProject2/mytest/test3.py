# def crawl():
#     # 处理disease.sh接口数据
urlList = ["https://disease.sh/v3/covid-19/historical/china?lastdays=all",
           "https://disease.sh/v3/covid-19/all",
           "https://disease.sh/v3/covid-19/countries/usa",
           "https://disease.sh/v3/covid-19/vaccine/coverage/countries?lastdays=1"]

#     data = pandas.read_json(urlList[0])
#     [keyList, valueList] = dataFrame_to_KVList(data, "date")
#     tableName = "historicalTable"
#     mysql = Mysql()
#     typeList = default_typelist(keyList)
#     mysql.create_table(tableName, keyList, typeList)
#     for value in valueList:
#         mysql.insert(tableName, keyList, value)

import pandas
url = "https://disease.sh/v3/covid-19/historical/china?lastdays=all"
data = pandas.read_json(urlList[0])
print(data)