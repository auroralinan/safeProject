__author__ = 'Nan Li'
# -*- coding: utf-8 -*-

import requests

if __name__ == "__main__":
	http_url = 'http://localhost:1234/getrest'
	data0 = {"cardid": "6225885800005592", 'card': '122345'}
	data1 = {'username': 'lvkun'}
	data2 = {'username': ''}
	data3 = {'filename': ''}
	r = requests.post(http_url, data=data0)
	print r.text
