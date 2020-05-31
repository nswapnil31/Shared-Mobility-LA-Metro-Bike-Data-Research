import requests
import os
import datetime
import time

from apscheduler.schedulers.background import BackgroundScheduler


url = "https://bikeshare.metro.net/stations/json/"
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}


def scrap():
	now = datetime.datetime.now()
	file_name = (now.strftime("%m-%d-%Y %H"))+'.json'
	response = requests.get(url,headers = headers)
	response_data = response.content.decode()
	with open(file_name,'a') as f:
		f.write(response_data)


if __name__ == '__main__':
	sched = BackgroundScheduler()
	sched.add_job(scrap, 'interval', seconds=10)
	sched.start()
	print('Press Ctrl+{0} to exit'.format('Break' if os.name == 'nt' else 'C'))

	try:
		while True:
			time.sleep(2)
	except (KeyboardInterrupt, SystemExit):
		sched.shutdown()


# sched.print_jobs()
