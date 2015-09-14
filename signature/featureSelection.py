__author__ = 'Nan Li'
# -*- coding: utf-8 -*-

import os
import sys
import xlrd
import numpy as np
import random
from sklearn import preprocessing

def dicttolist(d):
	lst = []
	for i in d:
		lst.append([i, d[i]])
	return lst

def findCommonX(lst, x):
	d = dict()
	for i in lst:
		for j in i:
			try:
				d[j] += 1
			except:
				d[j] = 1
	l = dicttolist(d)
	l.sort(key=lambda k:k[1], reverse=True)
	print l
	if l[x - 1][1] >= len(lst):
		return True
	else:
		return False


def choiceSample(X, trainnum, testnum):
	train = random.sample(X[:50], trainnum)
	test = random.sample(X[:50], testnum) + random.sample(X[50:], testnum)
	return train, test

def distance(x):
	return np.sum(map(lambda x: x*x, x))

def standard(x, mean_, std_):
	for i in range(len(x)):
		if std_[i] == 0:
			print std_[i]
		x[i] = (x[i] - mean_[i]) / std_[i]
	return x

def predictFunc(dis, disTrain):
	if dis < disTrain:
		return 1
	else:
		return 0

os.chdir(sys.argv[0][:sys.argv[0].rfind("/")])

excel = xlrd.open_workbook('50 result samples.xlsx')
excel2 = xlrd.open_workbook('50 result negative samples.xlsx')
table = excel.sheet_by_index(0)
table2 = excel2.sheet_by_index(0)

para = 45
repeat = 20

Tzong = 0
Fzong = 0

for i in range(0, 50):
	sample = []
	sampleNegative = []
	for j in range(i*50, i*50+50):
		sample.append(table.row_values(j)[2:])
		sample[-1].append(1.0)
	for j in range(i*20, i*20+20):
		sampleNegative.append(table2.row_values(j)[2:])
		sampleNegative[-1].append(-1.0)
	#
	# bo = []
	# for j in range(57):
	# 	bo.append(True)

	X = sample + sampleNegative
	Tsc = 0
	Fsc = 0
	for rep in range(repeat):
		train, test = choiceSample(X, 3, 5)
		train = np.array(train)
		test = np.array(test)
		scaler = preprocessing.StandardScaler().fit(train[:, :-1])
		tr = scaler.transform(train[:, :-1])
		# for i in train:
		# 	print distance(i)
		#
		te = scaler.transform(test[:, :-1])


		# print pearsonr(x, y)
		dis = 1000000.0
		for i in tr:
			temp = distance(i)
			if  temp < dis:
				dis = temp
		pre = [1, 1, 1, 1, 1, 0, 0, 0, 0, 0]
		Tscore = 0
		Fscore = 0
		for i in range(5):
			if predictFunc(distance(te[i]), dis*para) == pre[i]:
				Tscore += 1
		Tscore = Tscore / 5.0
		for i in range(5, 10):
			if predictFunc(distance(te[i]), dis*para) == pre[i]:
				Fscore += 1
		Fscore = Fscore / 5.0
		Tsc += Tscore
		Fsc += Fscore
	print Tsc/float(repeat), Fsc/float(repeat)
	Tzong += Tsc/float(repeat)
	Fzong += Fsc/float(repeat)
print Tzong/50.0, Fzong/50.0, para




	# for j in te:
	# 	best = -1.0
	# 	for i in tr:
	# 		temp = pearsonr(i, j)
	# 		if temp > best:
	# 			best = temp
	# 	print best
	# for j in range(57):
	# 	if bo[j] == lst[j]:
	# 		pass
	# 	else:
	# 		bo[j] = False


