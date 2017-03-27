# -*- coding: utf-8 -*-

from sklearn.model_selection import train_test_split

import libraryMushroom as lm

class Data:
	header 	= None
	X 		= []
	y 		= []
	x_train = []
	x_test	= []
	y_train = []
	y_test 	= []

	def __init__(self, path):
		arq = open(path, "r")

		self.header = arq.readline().replace("\n","").split(",")
		self.header.pop(0) # remove coluna classificadora

		for x in arq.readlines():
			self.X.append(x.replace("\n", "").split(","))
			self.y.append(self.X[-1].pop(0)) # remove coluna classificadora

		arq.close()
		
		auxX = lm.translateValues(self.X, 'int')
		auxY = lm.translateClassifier(self.y, 'int')

		self.x_train, self.x_test, self.y_train, self.y_test = train_test_split(auxX, auxY, train_size=0.6)	

