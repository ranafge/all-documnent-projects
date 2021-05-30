import requests
from bs4 import BeautifulSoup
import json
from tabulate import tabulate

filter_string = {
  "players": {
    "filterStatus": {
      "value": [
        "FREEAGENT",
        "WAIVERS"
      ]
    },
    "filterSlotIds": {
      "value": [
        0,
        1,
        2,
        3,
        4,
        5,
        6,
        7,
        8,
        9,
        10,
        11
      ]
    },
    "filterRanksForScoringPeriodIds": {
      "value": [
        1
      ]
    },
    "sortPercOwned": {
      "sortPriority": 2,
      "sortAsc": False
    },
    "sortDraftRanks": {
      "sortPriority": 100,
      "sortAsc": True,
      "value": "STANDARD"
    },
    "limit": 50,
    "offset": 0,
    "filterStatsForTopScoringPeriodIds": {
      "value": 5,
      "additionalValue": [
        "002021",
        "102021",
        "002020",
        "012021",
        "022021",
        "032021",
        "042021"
      ]
    }
  }
}


url = 'https://fantasy.espn.com/apis/v3/games/fba/seasons/2021/segments/0/leagues/133998?view=kona_player_info'

headers = {"players":{"filterStatus":{"value":["FREEAGENT","WAIVERS"]},"filterSlotIds":{"value":[0,1,2,3,4,5,6,7,8,9,10,11]},"filterRanksForScoringPeriodIds":{"value":[1]},"sortPercOwned":{"sortPriority":2,"sortAsc":False},"sortDraftRanks":{"sortPriority":100,"sortAsc":True,"value":"STANDARD"},"limit":50,"filterStatsForTopScoringPeriodIds":{"value":5,"additionalValue":["002021","102021","002020","012021","022021","032021","042021"]}}}
headers ={'x-fantasy-filter': json.dumps(headers)}

sample_table = []
response = requests.get(url, headers=headers).json()
print(response)
for data in response["players"]:
  sample_table.append(
    [
      data['player']['fullName'],
      data['player']['stats'][9]['appliedTotal'],

    ]


  )
print(tabulate(sample_table, headers=['name', 'average']))
