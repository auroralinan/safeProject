__author__ = 'Administrator'
# -*- coding: utf-8 -*-

#file work

import numpy as np
from sklearn import preprocessing
from dataClean import calc_data

import model_operation as op

paraForSign = 35

def distance(x):
	return np.sum(map(lambda x: x*x, x))

def findData(username, db):
	db.select('data_signature', where="username='{}' and tag='{}'".format(username, 'train'), _test=True)
	res = db.select('data_signature', where="username='{}' and tag='{}'".format(username, 'train'), order='Time')
	temp = []
	data = []
	number = 1
	try:
		for i in res:
			if i.num == number:
				temp.append([int(i.dataid), str(i.username), int(i.num), int(i.Time), float(i.X), float(i.Y), float(i.Pressure), float(i.S), str(i.move)])
			else:
				print temp
				temp = calc_data(temp)
				print temp
				data.append(temp)
				temp = []
				number = i.num
				temp.append([int(i.dataid), str(i.username), int(i.num), int(i.Time), float(i.X), float(i.Y), float(i.Pressure), float(i.S), str(i.move)])
		data = np.array(data)
		return data
	except:
		return 0

def train(username, db):
	# train must be a ndarray
	tr = findData(username, db)
	para = paraForSign
	if tr != 0 and tr is not None:
		scaler = preprocessing.StandardScaler().fit(tr)
		tr = scaler.transform(tr)
		dis = 0.0
		for i in range(len(tr)):
			dis += distance(tr)
		dis /= len(tr)
		op.save_model(scaler, para, dis, username)
		return 1
	else:
		return 'train error!'


if __name__ == "__main__":
	pass

