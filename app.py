# -*- coding: utf-8 -*-

from sys import path
path.append('./data')
path.append('./methods')

from data import Data
from svm import SVM
from ann import ANN
from nb import NaiveBayes
from time import time

data = Data("mushrooms.csv")


print 'ANN Method'
method = ANN(data)
i = time()
method.train()
method.predict()
f = time()
print 'Milisegundos:', f-i
print 'Acerto:', method.getPercentage()

print '\nSVM Method'
method = SVM(data)
i = time()
method.train()
method.predict()
f = time()
print 'Milisegundos:', f-i
print 'Acerto:', method.getPercentage()

print '\nNaiveBayes Method'
method = NaiveBayes(data)
i = time()
method.train()
method.predict()
f = time()
print 'Milisegundos:', f-i
print 'Acerto:', method.getPercentage()