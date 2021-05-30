from selenium import webdriver

url = 'https://stackoverflow.com/questions/65931008/unable-to-interact-with-this-dynamic-drop-down-using-python-selenium'

driver = webdriver.Firefox(executable_path='./geckodriver')
driver.get(url)

all_items = driver.find_elements_by_xpath('//img')
for item in all_items:
    print(item.text)
    print(driver.execute_script('arguments[1]', item))
    #driver.execute_script("arguments[0].click()", item)
    driver.execute_script("arguments[0].style.display = 'none';", item)
