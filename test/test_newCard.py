import requests

__author__ = 'Nan Li'
# -*- coding: utf-8 -*-


if __name__ == "__main__":
	http_url = 'http://localhost:1234/newCard'
	data0 = {"cardid": "6225885800005592", 'name': '李楠'.decode('gbk'), 'phone': '18658341665', 'username': 'linan'}
	data1 = {'username': 'lvkun'}
	data2 = {'username': ''}
	data3 = {'filename': ''}
	r = requests.post(http_url, data=data0)
	print r.text