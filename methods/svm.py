# -*- coding: utf-8 -*-

from sklearn.svm import SVC

class SVM:
	parameters 	= None
	data 		= None
	svc 		= None
	result 		= None
	time 		= None


	def __init__(self, data):
		print 'SVM Method'
		self.data 	= data
		self.svc 	= SVC(kernel='poly', degree=14, gamma=0.02, coef0=1.5)

	def train(self):
		self.svc.fit(self.data.x_train, self.data.y_train)

	def predict(self):
		self.result = self.svc.predict(self.data.x_test)

	def getPercentage(self):
		count = 0
		for i in range(len(self.result)):
			if self.data.y_test[i] == self.result[i]:
				count += 1 
		
		count *= 100
		count = round(float(count) / len(self.result), 2)
		return str(count) + "%"