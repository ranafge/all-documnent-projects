from bs4 import BeautifulSoup  
import requests  
def opening_url(link):  
    print(f"Selected website: {link}")  
    website = requests.get(link)  
    soup = BeautifulSoup(website.text, "html.parser")  
    print(soup.prettify())  
    return soup  

opening_url("https://www.nasdaq.com/market-activity/stocks/aapl/financials")
