__author__ = 'Administrator'
# -*- coding: utf-8 -*-

import os
import sys
import xlrd
import numpy
import random
from sklearn import preprocessing, svm
from signature import train_signature as tr

def choiceSample(sample, number):
	for i in range(repeat):
		traindata = choiceSample(sample, 3)

os.chdir(sys.argv[0][:sys.argv[0].rfind("/")])

excel = xlrd.open_workbook('50 result samples.xlsx')
excel2 = xlrd.open_workbook('50 result negative samples.xlsx')
table = excel.sheet_by_index(0)
table2 = excel2.sheet_by_index(0)

repeat = 10

for i in range(20, 21):
	sample = []
	sampleNegative = []
	for j in range(i*50, i*50+50):
		sample.append(table.row_values(j)[2:])
	for j in range(i*20, i*20+20):
		sampleNegative.append(table2.row_values(j)[2:])

	bo = []
	for j in range(57):
		bo.append(True)

	X = sample+sampleNegative
	y = []
	for j in range(50):
		y.append(1)
	for j in range(20):
		y.append(-1)

	X = numpy.asarray(X)
	y = numpy.asarray(y)

	X, cl = tr.feature_selection(X, y, 10)
	lst = cl.get_support()

	for j in range(57):
		if bo[j] == lst[j]:
			pass
		else:
			bo[j] = False

	X = preprocessing.scale(X)
	X = numpy.matrix(X)
	y = numpy.matrix(y)





