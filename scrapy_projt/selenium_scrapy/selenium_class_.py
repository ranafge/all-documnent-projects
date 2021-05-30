import sys
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def element(driver, by_x, html_element):
    try:
        element = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((by_x, html_element))
        )
        return element
    except:
        print("Element not found")

def get_numbers(string):
    numbers_list = [string[i] for i in range(len(string)) if string[i].isnumeric()]
    number = "".join(numbers_list)
    return number

class movieRatingScraper:
    def __init__(self, film):
        options = webdriver.ChromeOptions()
        options.add_experimental_option("excludeSwitches", ["enable-logging"])
        self.driver = webdriver.Chrome( options=options)
        self.film = film
        self.driver.get(f"https://search.yahoo.com/search?p={self.film}")

    def info(self):
        # THE PROBLEM
        element(self.driver, By.XPATH, "//*[@id='yui_3_10_0_1_1609677350466_629']").click()

    def rt_rating(self):
        WebDriverWait(self.driver,     10).until(EC.element_to_be_clickable((By.NAME,"agree"))).click()
        rt_string = element(self.driver, By.CLASS_NAME, "rottenTomatoes")
        rt_rating = get_numbers(rt_string.text)
        print(rt_rating)
        return rt_rating

    def get_current_url(self):
        return self.driver.current_url

    def quit(self):
        self.driver.quit()

movie = movieRatingScraper("tenet")
ratings = movie.rt_rating()
movie.info()
movie.get_current_url()
