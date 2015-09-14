__author__ = 'Administrator'
# -*- coding: utf-8 -*-

#file work

import os
import sys
import xlrd
import numpy as np
import random
from sklearn import preprocessing

from signature import model_operation as op

paraForSign = 35
paraForPwd = 35

def distance(x):
	return np.sum(map(lambda x: x*x, x))

def feature_selection(X, y, knew):
	clf = SelectKBest(f_classif, k=knew)
	X_new = clf.fit_transform(X, y)
	return X_new, clf

def findData(username, db, type_):
	if type_ == 'signature':
	db.select('card_bank', what='bank, type', where="num='{}'".format(str))
	return 0


def train(username, db, type_):
	#train must be a ndarray
	tr = findData(username, db, type_)
	if type_ == 'signature':
		para = paraForSign
	else:
		para = paraForPwd
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




