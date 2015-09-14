__author__ = 'Administrator'
# -*- coding: utf-8 -*-

import numpy as np
x = [[1,2], [3,4], [5,6], [2,3]]
print x[0:2][:]

X = np.matrix(x)
print X[0:2][:,0]



