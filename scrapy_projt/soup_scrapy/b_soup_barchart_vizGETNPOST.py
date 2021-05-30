# from bs4 import BeautifulSoup
# import requests
# import sys
# import requests
#
# url = "https://viz.saude.gov.br/extensions/CobVac_MOV/CobVac_MOV.html"
#
# client = requests.session()
#
# client.get(url)
# import requests
#
# headers = {
#     'authority': 'maps.qlikcloud.com',
#     'sec-ch-ua': '"Chromium";v="88", "Google Chrome";v="88", ";Not A Brand";v="99"',
#     'ga-session': '1d87b2f8',
#     'sec-ch-ua-mobile': '?0',
#     'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.96 Safari/537.36',
#     'content-type': 'application/json;charset=UTF-8',
#     'accept': '*/*',
#     'origin': 'https://viz.saude.gov.br',
#     'sec-fetch-site': 'cross-site',
#     'sec-fetch-mode': 'cors',
#     'sec-fetch-dest': 'empty',
#     'referer': 'https://viz.saude.gov.br/',
#     'accept-language': 'en-US,en;q=0.9',
# }
#
# params = (
#     ('key', 'feb18-bxon0nKvbqJ8sn8'),
# )
#
# data = '{id:"1",names:["NaN,BR:AADM1","-H,BR:AADM1","-M,BR:AADM1","-P,BR:AADM1",".C,BR:AADM1",".N,BR:AADM1",".S,BR:AADM1","2,BR:AADM1","3,BR:AADM1","4,BR:AADM1","5,BR:AADM1","6,BR:AADM1","7,BR:AADM1","8,BR:AADM1","9,BR:AADM1","10,BR:AADM1","11,BR:AADM1","12,BR:AADM1","13,BR:AADM1","14,BR:AADM1","15,BR:AADM1","16,BR:AADM1","17,BR:AADM1","18,BR:AADM1","19,BR:AADM1","20,BR:AADM1","21,BR:AADM1","24,BR:AADM1","25,BR:AADM1","26,BR:AADM1","27,BR:AADM1","28,BR:AADM1","29,BR:AADM1","31,BR:AADM1","33,BR:AADM1","A.,BR:AADM1","AB,BR:AADM1","AC,BR:AADM1","AE,BR:AADM1","AF,BR:AADM1","AG,BR:AADM1","AL,BR:AADM1","AM,BR:AADM1","AN,BR:AADM1","AP,BR:AADM1","AR,BR:AADM1","AZ,BR:AADM1","B,BR:AADM1","B/,BR:AADM1","BA,BR:AADM1","BH,BR:AADM1","BJ,BR:AADM1","BM,BR:AADM1","BO,BR:AADM1","CA,BR:AADM1","CE,BR:AADM1","CM,BR:AADM1","CO,BR:AADM1","CR,BR:AADM1","DE,BR:AADM1","DF,BR:AADM1","DG,BR:AADM1","DI,BR:AADM1","DN,BR:AADM1","ED,BR:AADM1","EG,BR:AADM1","EL,BR:AADM1","EN,BR:AADM1","ER,BR:AADM1","ES,BR:AADM1","F,BR:AADM1","FL,BR:AADM1","FR,BR:AADM1","GA,BR:AADM1","GE,BR:AADM1","GO,BR:AADM1","GR,BR:AADM1","GV,BR:AADM1","HA,BR:AADM1","IA,BR:AADM1","ID,BR:AADM1","II,BR:AADM1","IN,BR:AADM1","IO,BR:AADM1","IP,BR:AADM1","IR,BR:AADM1","IT,BR:AADM1","JA,BR:AADM1","JB,BR:AADM1","JD,BR:AADM1","JF,BR:AADM1","JM,BR:AADM1","L,BR:AADM1","LA,BR:AADM1","LC,BR:AADM1","LE,BR:AADM1","LO,BR:AADM1","LT,BR:AADM1","LU,BR:AADM1","MA,BR:AADM1","MC,BR:AADM1","MG,BR:AADM1","MO,BR:AADM1","MS,BR:AADM1","MT,BR:AADM1","NA,BR:AADM1","NO,BR:AADM1","O,BR:AADM1","OA,BR:AADM1","OE,BR:AADM1","OI,BR:AADM1","ON,BR:AADM1","OO,BR:AADM1","PA,BR:AADM1","PB,BR:AADM1","PC,BR:AADM1","PE,BR:AADM1","PI,BR:AADM1","PN,BR:AADM1","PR,BR:AADM1","RA,BR:AADM1","RE,BR:AADM1","RI,BR:AADM1","RJ,BR:AADM1","RM,BR:AADM1","RN,BR:AADM1","RO,BR:AADM1","RP,BR:AADM1","RR,BR:AADM1","RS,BR:AADM1","S,BR:AADM1","S-,BR:AADM1","SA,BR:AADM1","SC,BR:AADM1","SE,BR:AADM1","SG,BR:AADM1","SI,BR:AADM1","SJ,BR:AADM1","SL,BR:AADM1","SP,BR:AADM1","SR,BR:AADM1","SS,BR:AADM1","SU,BR:AADM1","TA,BR:AADM1","TE,BR:AADM1","TO,BR:AADM1","UA,BR:AADM1","UB,BR:AADM1","UD,BR:AADM1","UI,BR:AADM1","UN,BR:AADM1","UR,BR:AADM1","VA,BR:AADM1","VC,BR:AADM1","VF,BR:AADM1","VL,BR:AADM1","VN,BR:AADM1","VP,BR:AADM1","XV,BR:AADM1"]}'
#
# response = requests.post('https://maps.qlikcloud.com/ravegeo/webmap5/areageom/default', headers=headers, params=params, data=data)
#
# # print(response.text) works very good
#
#
# import requests
#
# headers = {
#     'authority': 'translate.googleapis.com',
#     'sec-ch-ua': '"Chromium";v="88", "Google Chrome";v="88", ";Not A Brand";v="99"',
#     'sec-ch-ua-mobile': '?0',
#     'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.96 Safari/537.36',
#     'content-type': 'application/x-www-form-urlencoded',
#     'accept': '*/*',
#     'origin': 'https://viz.saude.gov.br',
#     'x-client-data': 'CJC2yQEIorbJAQipncoBCPjHygEIo83KAQjc1coBCMWcywEIqZ3LAQjencsB',
#     'sec-fetch-site': 'cross-site',
#     'sec-fetch-mode': 'cors',
#     'sec-fetch-dest': 'empty',
#     'referer': 'https://viz.saude.gov.br/',
#     'accept-language': 'en-US,en;q=0.9',
# }
#
# params = (
#     ('anno', '3'),
#     ('client', 'te_lib'),
#     ('format', 'html'),
#     ('v', '1.0'),
#     ('key', 'AIzaSyBOti4mM-6x9WDnZIjIeyEU21OpBXqWBgw'),
#     ('logld', 'vTE_20201130_00'),
#     ('sl', 'pt'),
#     ('tl', 'en'),
#     ('tc', '1'),
#     ('dom', '1'),
#     ('sr', '1'),
#     ('tk', '238900.356531'),
#     ('mode', '1'),
# )
#
# data = [
#   ('q', 'Data'),
#   ('q', 'UF'),
#   ('q', 'Doses enviadas aos Estados'),
#   ('q', 'Totais'),
#   ('q', '7.336.818'),
#   ('q', 'MG'),
#   ('q', '855.580'),
#   ('q', 'RJ'),
#   ('q', '758.120'),
#   ('q', 'BA'),
#   ('q', '550.700'),
#   ('q', 'SP'),
#   ('q', '517.090'),
#   ('q', 'RS'),
#   ('q', '511.200'),
#   ('q', 'AM'),
#   ('q', '459.420'),
#   ('q', 'PE'),
#   ('q', '393.360'),
#   ('q', 'PR'),
#   ('q', '391.700'),
#   ('q', 'CE'),
#   ('q', '334.900'),
#   ('q', 'GO'),
#   ('q', '278.380'),
#   ('q', 'PA'),
#   ('q', '251.440'),
#   ('q', 'MA'),
#   ('q', '235.140'),
#   ('q', 'Munic\xEDpio'),
#   ('q', 'Destino'),
#   ('q', 'Doses enviadas aos Munic\xEDpios'),
#   ('q', '4.855.061'),
#   ('q', 'MS CAPITAL'),
#   ('q', '546.206'),
#   ('q', 'BELO HORIZONTE/MG'),
#   ('q', '193.820'),
#   ('q', 'PORTO ALEGRE/RS'),
#   ('q', '144.420'),
#   ('q', 'RECIFE/PE'),
#   ('q', '94.626'),
#   ('q', 'SALVADOR/BA'),
#   ('q', '90.690'),
#   ('q', 'FORTALEZA/CE'),
#   ('q', '78.030'),
#   ('q', 'CAMPINAS/SP'),
#   ('q', '56.280'),
#   ('q', 'CURITIBA/PR'),
#   ('q', '55.378'),
#   ('q', 'GOIANIA/GO'),
#   ('q', '52.160'),
#   ('q', 'JOAO PESSOA/PB'),
#   ('q', '44.373'),
#   ('q', 'SAO GONCALO/RJ'),
#   ('q', '40.730'),
#   ('q', 'JUIZ DE FORA/MG'),
#   ('q', '40.548'),
#   ('q', 'Tipo de Destino'),
#   ('q', 'Semana'),
#   ('q', 'Search'),
#   ('q', 'Fabricante'),
#   ('q', 'Doses'),
#   ('q', 'Percentual de Repasse aos Munic\xEDpios'),
#   ('q', 'Doses Repassadas aos Munic\xEDpios'),
# ]
#
# response = requests.post('https://translate.googleapis.com/translate_a/t', headers=headers, params=params, data=data)

# data = response.text
data = ["Date", "UF", "Doses sent to States", "Totals", "7,336,818", "MG", "855,580", "RJ", "758,120", "BA", "550,700",
        "SP", "517,090", "LOL", "511,200", "AM", "459,420", "PE", "393,360", "PR", "391,700", "CE", "334,900", "GO",
        "278,380", "PAN", "251,440", "BAD", "235,140", "County", "Destiny", "Doses sent to Municipalities", "4,855,061",
        "MS CAPITAL", "546,206", "BELO HORIZONTE / MG", "193,820", "PORTO ALEGRE / RS", "144,420", "RECIFE PE",
        "94,626", "SALVADOR BA", "90,690", "FORTALEZA / CE", "78,030", "CAMPINAS, SP", "56,280", "CURITIBA / PR",
        "55,378", "GOIANIA / GO", "52,160", "JOAO PESSOA / PB", "44,373", "SAO GONCALO / RJ", "40,730",
        "JUDGE OF FORA / MG", "40,548", "Destination Type", "Week", "Search", "Manufacturer", "Doses",
        "Percentage of Transfer to Municipalities", "Doses Relayed to Municipalities"]
desire_data =  data[3:57]
print(desire_data)
print(len(desire_data))
print([{desire_data[i]: desire_data[i + 1]} for i in range(0,len(desire_data)-1,2)])
# for i in range(len(data)):
#     print({data[i]:data[i+1]})
