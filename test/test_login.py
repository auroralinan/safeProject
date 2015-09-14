__author__ = 'Nan Li'
# -*- coding: utf-8 -*-

import requests

if __name__ == "__main__":
	http_url = 'http://localhost:1234/checkin'
	data = {'username': 'linan'}
	data0 = {'username': 'linan', 'password': '123456'}
	data1 = {'username': '1865834', 'password': "123456"}
	data2 = {'username': 'linan', 'password': "234234"}
	print data0
	r = requests.post(http_url, data=data2)
	print r.text
	# r = requests.post(http_url, data=data1)
	# print r.text
	# r = requests.post(http_url, data=data2)
	# print r.text