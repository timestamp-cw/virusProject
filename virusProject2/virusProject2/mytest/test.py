from selenium.common.exceptions import ElementClickInterceptedException

from virusProject3.virusProject3.mytool.driver import handle_driver2
from selenium import webdriver
from lxml import etree

driver_path = r"D:\ProgramApp\edgedriver_win64\msedgedriver.exe"
target_url = "https://voice.baidu.com/act/newpneumonia/newpneumonia"
driver = webdriver.Edge(driver_path)
# 打开页面
driver.get(target_url)
# 点击展开全部
xpath = '//div[@id="nationTable"]/div'
e2 = driver.find_element_by_xpath(xpath)
e2.click()
# 统计有多少个省份
js = 'return document.getElementById("nationTable").children[0].children[1].childElementCount'
count = driver.execute_script(js)
# 点击各个省份
xpath3 = '//div[@id="nationTable"]/table/tbody/tr[1]'
xpath4 = './following-sibling::*[1]'
e = driver.find_element_by_xpath(xpath3)
eList = [e]
for i in range(1, 5):
    e = e.find_element_by_xpath(xpath4)
    eList.append(e)

for ee in eList:
    try:
        ee.click()
    except ElementClickInterceptedException:
        continue

html = etree.HTML(driver.page_source)
res = html.xpath('//div[@id="nationTable"]/table/tbody/tr//a/@href')
print(res)