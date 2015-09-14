import urllib2
import time

__author__ = 'Administrator'
# -*- coding: utf-8 -*-

import requests
import json
if __name__ == "__main__":
	http_url = 'http://localhost:1234/upload'
	# http_body = {"key": 'this is a post test'}
	# r = requests.post(http_url, data=json.dumps(http_body))
	# print r.text

	files = {'file': ('name.jpg', open('name.jpg', 'rb'))}
	data = {'filename': 'name.jpg'}
	r = requests.post(http_url, files=files, data=data)
	print r.text

	# form_data = {
	# 	'filename':'name.jpg',
	# }
	# files = {'file': ('name.jpg', open('name.jpg', 'rb'))}
	# r = requests.post(http_url, data = form_data, files=files)



# boundary = '----------%s' % hex(int(time.time() * 1000))
# print boundary
# data = []
# # data.append('--%s' % boundary)
#
# fr = open(r'name.jpg', 'rb')
# data.append('Content-Disposition: form-data; name="%s"; filename="b.jpg"' % 'profile')
# data.append('Content-Type: %s\r\n' % 'image/jpg')
# data.append(fr.read())
# fr.close()
# data.append('--%s--\r\n' % boundary)
#
# http_url = 'http://localhost:1234/upload'
# http_body = '\r\n'.join(data)
# try:
#             #buld http request
# 	req=urllib2.Request(http_url, data=http_body)
#             #header
# 	req.add_header('Content-Type', 'multipart/form-data; boundary=%s' % boundary)
# 	req.add_header('User-Agent', 'Mozilla/5.0')
# 	req.add_header('Referer', 'http://remotserver.com/')
#             #post data to server
# 	resp = urllib2.urlopen(req, timeout=5)
#             #get response
# 	qrcont=resp.read()
# 	print qrcont
# except Exception,e:
# 	print 'http error'