__author__ = 'Administrator'
# -*- coding: utf-8 -*-

import xlrd
import numpy as np
from sklearn import preprocessing
from sklearn.multiclass import OneVsRestClassifier
from sklearn.svm import LinearSVC
from sklearn import cross_validation

def normalize(data):
	return preprocessing.scale(data)

if __name__ == "__main__":
	filenames = ["../data/lxd1.xlsx", "../data/lk2.xlsx", "../data/ln3.xlsx", "../data/wf4.xlsx"]
	X = []
	y = []
	for filename in filenames:
		data = []
		excel = xlrd.open_workbook(filename)
		table = excel.sheet_by_index(0)
		for i in range(225):
			temp = map(float, table.row_values(i))
			if temp[0] == 0.0:
				pass
			else:
				data.append(temp)
		# print len(data)
		data = np.array(data)
		for i in range(len(data[0])-1):
			data[:, i] = normalize(data[:, i])
		data = data.reshape((1680, 1))
		data = data.reshape((15, 14*8))
		print data.shape
		X.extend(data)

	for i in range(1, 5):
		for j in range(15):
			y.append(float(i))
	X = np.array(X)
	print X.shape
	y = np.array(y)



clf = OneVsRestClassifier(LinearSVC(random_state=0)).fit(X, y)
print clf.score(X, y)


