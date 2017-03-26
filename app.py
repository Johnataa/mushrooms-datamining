# -*- coding: utf-8 -*-

from data import Data
from svm import SVM
from time import time

data = Data("mushrooms.csv")

method = SVM(data)
i = time()
method.train()
method.predict()
f = time()
print f-i
print method.getPercentage()