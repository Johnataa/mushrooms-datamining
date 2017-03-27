# -*- coding: utf-8 -*-

from sklearn.neural_network import MLPClassifier

class ANN:
	parameters 	= None
	data 		= None
	ann 		= None
	result 		= None
	time 		= None


	def __init__(self, data):
		self.data 	= data
		self.ann 	= MLPClassifier(alpha=0.005)


	def train(self):
		self.ann.fit(self.data.x_train, self.data.y_train)

	def predict(self):
		self.result = self.ann.predict(self.data.x_test)

	def getPercentage(self):
		count = 0
		for i in range(len(self.result)):
			if self.data.y_test[i] == self.result[i]:
				count += 1 
		
		count *= 100
		count = round(float(count) / len(self.result), 2)
		return str(count) + "%"