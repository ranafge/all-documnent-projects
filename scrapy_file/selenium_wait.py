from selenium import webdriver
import time
from selenium.webdriver.support.ui import WebDriverWait

PATH = 'D:\webdriver\chromedriver.exe'

driver = webdriver.Chrome()

url2 = 'https://www.rad.cvm.gov.br/ENET/frmGerenciaPaginaFRE.aspx?NumeroSequencialDocumento={}&CodigoTipoInstituicao=1'.format('91514')

driver.get(url2)

time.sleep(2)
element = driver.find_element_by_css_selector('table#ctl00_cphPopUp_tbDados')
WebDriverWait(driver, 10)


print(element)
