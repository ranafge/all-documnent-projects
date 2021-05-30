import datetime
import datetime
from datetime import datetime as dt, timedelta

ts = int("1615070997520")/1000
print(dt.utcfromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S'))
