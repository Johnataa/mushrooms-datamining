# -*- coding: utf-8 -*-

import libraryMushroom as lm

class Data:
	header = None
	X = []
	y = []

	def readCSV(self, path):
		arq = open(path, "r")

		self.header = arq.readline().replace("\n","").split(",")
		self.header.pop(0) # remove coluna classificadora

		for x in arq.readlines():
			self.X.append(x.replace("\n", "").split(","))
			self.y.append(self.X[-1].pop(0))

		arq.close()



data = Data()
data.readCSV("mushrooms.csv")

aux = lm.translate(data.X, 'int')
for i in range(0,5):
	print aux[i]

aux = lm.translate(data.X, 'str')
for i in range(0,5):
	print aux[i]
