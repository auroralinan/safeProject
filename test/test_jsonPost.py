__author__ = 'Nan Li'
# -*- coding: utf-8 -*-
import requests
if __name__ == "__main__":
	http_url = 'http://localhost:1234/receivedata'
	data = {'username': 'linan', 'transid': 123, 'tag': 'train', 'ty': 'password', 'databody': '[{"character":"h","endSize":0.027450982,"endTime":"2357111","endX":648,"endY":448,"pressure":1,"startSize":0.021568628,"startTime":"2357016","startX":648,"startY":448},{"character":"w","endSize":0.023529414,"endTime":"2357633","endX":179,"endY":345,"pressure":1,"startSize":0.023529414,"startTime":"2357527","startX":190,"startY":328}]'}
	data0 = {'username': 'linan', 'password': '123456'}
	data1 = {'username': '1865834', 'password': "123456"}
	data2 = {'username': 'linan', 'password': "234234"}
	r = requests.post(http_url, data=data)
	print r.text