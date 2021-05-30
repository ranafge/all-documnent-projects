import pandas as pd
import requests
url ="https://www.tatrabanka.sk/sk/personal/kurzovy-listok/01.01.2016-00:00"

r = requests.get(url)

# df = pd.read_json(url).drop(0).drop(columns=[])
#
# print(df)

