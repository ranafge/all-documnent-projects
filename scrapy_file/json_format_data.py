# The data is loaded in JSON format via sending a GET request to
#
# https://www.musimmas.com/presence/icof/
# You can extract the data with just the requests module, there's no need for BeautifulSoup
#
# import requests
#
#
# headers = {
#     "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36",
#     "referer": "https://www.musimmas.com/sustainability/traceability/",
# }
#
# response = requests.get(
#     "https://www.musimmas.com/presence/icof/", headers=headers,
# ).json()
#
# # To get all links try the following
# for data in response:
#     if data["reports"]:
#         reports = data["reports"]
#         for links in reports:
#             print(links["link"])
#         print("-" * 20)
# Partial output:
#
# https://www.musimmas.com/report/musim-mastika-oils-fats-johor-malaysia-july-september-2020/
# /report/musim-mastika-oils-fats-johor-malaysia-april-june-2020/
# /report/musim-mastika-oil-fats-johor-malaysia-january-march-2020/
# /report/musim-mastika-oil-fats-johor-malaysia-october-december-2019/
# /report/musim-mastika-oil-fats-johor-malaysia-july-september-2019/
# --------------------
# https://www.musimmas.com/report/musim-mas-pelalawan-riau-july-september-2020/
# /report/musim-mas-pelalawan-riau-april-june-2020/
# /report/musim-mas-pelalawan-riau-january-march-2020/
# /report/musim-mas-pelalawan-riau-october-december-2019/
# /report/musim-mas-pelalawan-riau-july-september-2019/
# /supply-chain-map/summary-report/musim-mas-pelalawan-riau/period-april-june-2019.html
# --------------------

