from selenium.common.exceptions import ElementClickInterceptedException

from virusProject3.virusProject3.mytool.driver import handle_driver
from selenium import webdriver
from lxml import etree
driver_path = r"D:\ProgramApp\edgedriver_win64\msedgedriver.exe"
target_url = "https://voice.baidu.com/act/newpneumonia/newpneumonia"
driver = webdriver.Edge(driver_path)
handle_driver(driver,target_url)
html = etree.HTML(driver.page_source)
res = html.xpath('//div[@id="nationTable"]/table/tbody/tr//a/@href')
print(res)