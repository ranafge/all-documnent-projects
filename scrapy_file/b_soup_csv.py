from datetime import datetime
import requests
import csv


def main():
    print("python main function")
    datetime_object = datetime.now().date()
    url = f'https://markets.cboe.com/us/equities/market_statistics/volume_reports/day/{datetime_object}/csv/?mkt=bzx'
    print(url)
    response = requests.get(url, stream=True)
    csv_content = response.content.decode('utf-8')

    print(csv_content)
    cr = csv.reader(csv_content.splitlines(), delimiter='~')
    my_list = list(cr)
    for row in my_list:
        print(row)


if __name__ == '__main__':
    main()
