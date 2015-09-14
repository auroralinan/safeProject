__author__ = 'Administrator'
# -*- coding: utf-8 -*-

from signature import model_operation as mo


def verify(uid, data):
	clf = mo.get_model(uid)
	res = clf.predict(data)
	# print "verify:", uid, "result is:", res
	return res

