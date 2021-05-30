import schedule
import time

def job():
    print('I"m workding...')

schedule.every(2).minutes.do(job)

while True:
    schedule.run_pending()
    time.sleep(1)
