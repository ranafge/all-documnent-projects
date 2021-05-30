import requests
from bs4 import BeautifulSoup
import json

headers = {
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36",
    "X-Requested-With": "XMLHttpRequest",
}

url ="https://www.bi.go.id/en/moneter/informasi-kurs/transaksi-bi/Default.aspx"

payload = {
"MSOTlPn_View": "0",
"MSOTlPn_ShowSettings": "False",
"MSOTlPn_Button": "none",
"_REQUESTDIGEST": "0xF5525CC31882DC4656A11BE3C11A619185A0DF336CFD8F86797746DDF70F6E6E0A9C58D77F2CE9962242166639E54989A277847CE7E8CA52B785A4562AD69625,22 Nov 2020 04:31:38 -0000",
"MSOSPWebPartManager_DisplayModeName": "Browse",
"MSOSPWebPartManager_ExitingDesignMode": "false",
"MSOWebPartPage_Shared":"",
"MSOLayout_LayoutChanges":"",
"MSOLayout_InDesignMode":"",
"_wpSelected":"",
"_wzSelected":"",
"MSOSPWebPartManager_OldDisplayModeName": "Browse",
"MSOSPWebPartManager_StartWebPartEditingName": "false",
"MSOSPWebPartManager_EndWebPartEditing": "false",
"_maintainWorkspaceScrollPosition": "212",
"__VIEWSTATEGENERATOR": "6537C4F3",
"ctl00$ctl40":"",
"ctl00$HeaderControl$TextBoxKeyword":"",
"ctl00$PlaceHolderLeftCell$PlaceHolderSearchArea$ctl01$ctl00": "https://www.bi.go.id/en/moneter/informasi-kurs/transaksi-bi",
"InputKeywords": "Search this site...",
"ctl00$PlaceHolderLeftCell$PlaceHolderSearchArea$ctl01$ctl04": "0",
"ctl00$PlaceHolderMain$biWebKursTransaksiBI$ddlmatauang1": "AUD",
"ctl00$PlaceHolderMain$biWebKursTransaksiBI$txtFrom": "2-Nov-20",
"ctl00$PlaceHolderMain$biWebKursTransaksiBI$txtTo": "20-Nov-20",
"ctl00$PlaceHolderMain$biWebKursTransaksiBI$txtTanggal":"",
"ctl00$PlaceHolderMain$biWebKursTransaksiBI$btnSearch1": "Search",
"ctl00$PlaceHolderMain$biWebKursTransaksiBI$hidSourceID": "ctl00_PlaceHolderMain_biWebKursTransaksiBI_btnSearch1",
"__spDummyText1":"",
"__spDummyText2":"",
"_wpcmWpid":"",
"wpcmVal":""
}


with requests.Session() as s:
    s.headers.update(headers)
    req =s.post(url, data=payload)
    print(req.status_code)
    soup = BeautifulSoup(req.text, 'lxml')
    # print(soup.prettify())
    for items in soup.find('div', {'class':"newRow table01"}):
        print([item.get_text(strip=True) for item in items.find('div')])
        # for tr in items.find_all('tr'):
        #     print(tr)
            # tds = tr.find_all('td')
            # print(tds[1].text,tds[2].text, tds[3].text)

        # print(items)
        # data = [item.get_text(strip=True) for item in items.find_all('tr')]
        # print(data)
