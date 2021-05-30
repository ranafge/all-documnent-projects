import time
from datetime import datetime

print(datetime.fromtimestamp(393243200243 / 1000).date())
ts = int("122323832")

print(datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S'))


def wait_start(runTime):
    startTime = time(*(map(int, runTime.split(':'))))
    while startTime > datetime.today().time():
        time.sleep(1)


runtime = '18:01:59'
print(list(map(int, runtime.split(':'))))


def Sort_Tuple(tup):
    tup.sort(key=lambda x: x[1], reverse=True)
    return tup


tup = [('A', 10), ('B', 5), ('C', 20), ('D', 15)]
print(Sort_Tuple(tup))

import calendar


def leap(start, stop, step=1):
    return [i for i in range(start, stop, step) if calendar.isleap(i)]


print(leap(1920, 2000, 1))
