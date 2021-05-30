from selenium import webdriver

url = 'https://data.europa.eu/euodp/pl/data/dataset/covid-19-coronavirus-data'
driver = webdriver.Firefox(executable_path='/geckodriver')
profile = webdriver.FirefoxProfile()
profile.set_preference("browser.download.panel.shown", False)
profile.set_preference("browser.helperApps.neverAsk.openFile","text/csv,application/vnd.ms-excel,application/octet-stream")
profile.set_preference("browser.helperApps.neverAsk.saveToDisk", "CSV File,text/csv,application/vnd.ms-excel")
profile.set_preference("browser.download.folderList", 2);
profile.set_preference("browser.download.dir", "/home/rana/Documents/allproject/scrapy_projt/")
driver = webdriver.Firefox(firefox_profile=profile)

driver.get(url)

item = driver.find_element_by_xpath('//div[@id="dataset-resources"]//li[2]//a')
print('text:', item.text)
print('href:', item.get_attribute('href'))
item.click()
