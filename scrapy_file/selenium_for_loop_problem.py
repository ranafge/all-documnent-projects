from selenium import webdriver
url="https://www.up-rera.in/frm_sanitize_prj_search.aspx?regid=918"
driver=webdriver.Chrome("/Users/prakhargarg/Desktop/chromedriver")
driver.get(url)
link = driver.find_element_by_link_text("Click Here To View Complete Project Details")
link.click()
window_after = driver.window_handles[1]
driver.switch_to.window(window_after)
driver.implicitly_wait(5)
rows=len(driver.find_elements_by_xpath('//*[@id="ShowTableApartment"]/tr'))
cols=len(driver.find_elements_by_xpath('//*[@id="ShowTableApartment"]/tr[1]/th'))
print(rows)
print(cols)
for r in range(2,rows+1):
    for c in range(1,cols+1):
        value=driver.find_element_by_xpath('//*[@id="ShowTableApartment"]/tr["+str(r)+"]/td["+str(c)+"]').text
        print(value, end='   ')
driver.quit()
