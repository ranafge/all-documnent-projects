import requests
import json
url ="https://www.tripadvisor.com/UserReviewController?a=fullTrans&r=468072896"
response = requests.get(url)
data = response.json()
print(data[0]['title'])
print(data[0]['body'])
