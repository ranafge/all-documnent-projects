import datetime
from datetime import timedelta

start_date = "01/02/21"

date_1 = datetime.datetime.strptime(start_date, "%d/%m/%y")
r = [3,6,9,12]
for d in range(1, 9):
    if d <=3:
        print(date_1)
    if d  <6:
        print(date_1 + datetime.timedelta(days=1))
        # break
    # if d >6 <=9:
    #     print(date_1 + datetime.timedelta(days=2))
    # if d>9 <=12:
    #     print(date_1 + datetime.timedelta(days=3))
    #     break;



# end_date = date_1 + datetime.timedelta(days=1)
# df_4["date"] = end_date
