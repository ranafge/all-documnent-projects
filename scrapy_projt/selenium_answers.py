The page is loaded dynamically, therefore `requests` won't support it. We can [Selenium][1] as an alternative to scrape the page.

Install it with: `pip install selenium`.

Download the correct ChromeDriver from [here][2].


    from time import sleep
    from selenium import webdriver
    from bs4 import BeautifulSoup

    URL = "https://nemsis.org/state-data-managers/state-map-v3/colorado"
    driver = webdriver.Chrome(r"c:\path\to\chromedriver.exe")
    driver.get(URL)
    # Wait for the page to fully render
    sleep(5)

    soup = BeautifulSoup(driver.page_source, "html.parser")
    print(soup.find("span", id="commitDate-refs/heads/release-3.4.0-3").text)

    driver.close()
Output:

    9/4/2019

  [1]: https://selenium-python.readthedocs.io/
  [2]: https://sites.google.com/a/chromium.org/chromedriver/downloads






