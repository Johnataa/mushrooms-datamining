# -*- coding: utf-8 -*-

from sklearn.naive_bayes import GaussianNB

class NaiveBayes:
	parameters 	= None
	data 		= None
	nb  		= None
	result 		= None
	time 		= None


	def __init__(self, data):
		print 'NaiveBayes Method'
		self.data 	= data
		self.nb 	= GaussianNB(priors=None)

	def train(self):
		self.nb.fit(self.data.x_train, self.data.y_train)

	def predict(self):
		self.result = self.nb.predict(self.data.x_test)

	def getPercentage(self):
		count = 0
		for i in range(len(self.result)):
			if self.data.y_test[i] == self.result[i]:
				count += 1 
		
		count *= 100
		count = round(float(count) / len(self.result), 2)
		return str(count) + "%"