__author__ = 'Nan Li'
# -*- coding: utf-8 -*-

a = '[{"character":"h","endSize":0.027450982,"endTime":"2357111","endX":648,"endY":448,"pressure":1,"startSize":0.021568628,"startTime":"2357016","startX":648,"startY":448},{"character":"w","endSize":0.023529414,"endTime":"2357633","endX":179,"endY":345,"pressure":1,"startSize":0.023529414,"startTime":"2357527","startX":190,"startY":328}]'

import json
j = json.loads(a)
print j[0]
for i in range(len(j)):
	print j[i][u'startX'], type(j[i][u'startX'])
	print j[i][u'startY'], type(j[i][u'startY'])
	print j[i][u'startSize'], type(j[i][u'startSize'])
	print j[i][u'startTime'], type(j[i][u'startTime'])
	print j[i][u'endX'], type(j[i][u'endX'])
	print j[i][u'endY'], type(j[i][u'endY'])
	print j[i][u'endSize'], type(j[i][u'endSize'])
	print j[i][u'endTime'], type(j[i][u'endTime'])
	print j[i][u'character'], type(j[i][u'character'])
	print j[i][u'pressure'], type(j[i][u'pressure'])
