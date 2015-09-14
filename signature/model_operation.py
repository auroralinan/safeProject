__author__ = 'Administrator'
# -*- coding: utf-8 -*-

from sklearn.externals import joblib

def save_model(clf, uid):
	filename = "trainPara/model_%s.pkl" % uid
	joblib.dump(clf, filename)
	return 0

def get_model(uid):
	filename = 'trainPara/model_%s.pkl' % uid
	clf = joblib.load(filename)
	return clf

def delete_model(uid):
	pass