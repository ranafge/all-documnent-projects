from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

lnk = ('https://news.detik.com/berita/d-5297980/pemprov-dki-tegaskan-aturan-wfh-75-juga-berlaku-untuk-perusahaan-swasta')
lnk2 = lnk + '?single=1'
print(lnk2)

chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')

driver = webdriver.Chrome(executable_path='chromedriver.exe',chrome_options=chrome_options)
driver.get(lnk2)
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);var lenOfPage=document.body.scrollHeight;return lenOfPage;")

html = driver.page_source
beau = BeautifulSoup(html.content, 'lxml')
element = beau.find_element_by_css_selector('a.komentar > span')
WebDriverWait(soup2, 10).until(lambda driver: element.text != '0 komentar')
comment = element.text.rstrip(' komentar')
