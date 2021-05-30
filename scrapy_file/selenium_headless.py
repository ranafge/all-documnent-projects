from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
sol = 'https://news.detik.com/berita/d-5259113/anies-usai-diklarifikasi-polisi-penjelasan-saya-jadi-laporan-23-halaman'

options = Options()
options.add_argument('--headless')
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')

driver = webdriver.Chrome(options=options)
driver.get(sol)
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);var lenOfPage=document.body.scrollHeight;return lenOfPage;")

html2 = driver.page_source
soupa = BeautifulSoup(html2, 'lxml')

element = driver.find_element_by_css_selector('a.komentar')
WebDriverWait(driver, 10).until(lambda driver: element.text != '0 komentar')
print(element.text.rstrip(' komentar'))

