# -*- coding: utf-8 -*-

from sys import path
path.append('./data')
path.append('./methods')

from data import Data
from svm import SVM
from ann import ANN
from nb import NaiveBayes
from time import time
import graph

data = Data("mushrooms.csv")
method = ANN(data)
i = time()
method.train()
method.predict()
tempo = time() - i
result = method.getPercentage()
print 'Tempo (ms):', tempo
print 'Taxa de acerto:', result
print ''

data = Data("mushrooms.csv")
method = SVM(data)
i = time()
method.train()
method.predict()
tempo = time() - i
result = method.getPercentage()
print 'Tempo (ms):', tempo
print 'Taxa de acerto:', result
print ''

data = Data("mushrooms.csv")
method = NaiveBayes(data)
i = time()
method.train()
method.predict()
tempo = time() - i
result = method.getPercentage()
print 'Tempo (ms):', tempo
print 'Taxa de acerto:', result