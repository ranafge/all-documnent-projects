
def tableDataText(h_table):
    rows = []
    trs = h_table.find_all('tr', {'class': "trBg01 tdAlignC boldFont13"})

    headerow = [td.get_text(strip=True, separator=' ,').split(',') for td in trs][0]
    print(headerow)
    if headerow:
        rows.append(headerow)

    for tr in h_table.find_all('tr', {'class': 'f_tac f_fs13'}):
        rows.append([tr.get_text(strip=True, separator=' ,').split(',')][0])
    return rows

    # result_table = tableDataText(h_table)
    # df = pd.DataFrame(result_table[1:], columns=result_table[0])
    # dfs = pd.concat([dfs, df], ignore_index=True)


if __name__ == "__main__":
    from bs4 import BeautifulSoup
    import requests
    from selenium import webdriver
    import pandas as pd
    import time

    dfs = pd.DataFrame()
    for i in range(1, 2):
        driver = webdriver.Chrome()
        driver.get(
            'https://racing.hkjc.com/racing/information/English/racing/RaceCard.aspx?RaceDate=2021/02/06&Racecourse=ST&RaceNo=' + str(
                i) + '')
        time.sleep(30)
        res = driver.execute_script('return document.documentElement.outerHTML')
        driver.quit()
        soup = BeautifulSoup(res, 'lxml')
        h_table = soup.find('table', {'class': 'starter f_tac f_fs13 draggable hiddenable'})
        tableDataText(h_table)
