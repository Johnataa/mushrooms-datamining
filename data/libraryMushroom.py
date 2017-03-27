# -*- coding: utf-8 -*-

capShape 				= {'b': 'bell', 'c': 'conical', 'x': 'convex', 'f': 'flat', 'k': 'knobbed', 's': 'sunken'}
capSurface 				= {'f': 'fibrous', 'g': 'grooves', 'y': 'scaly', 's': 'smooth'}
capColor				= {'n': 'brown', 'b': 'buff', 'c': 'cinnamon', 'g': 'gray', 'r': 'green', 'p': 'pink', 'u': 'purple', 'e': 'red', 'w': 'white', 'y': 'yellow'}
bruises 				= {'t': 'bruises', 'f': 'no'}
odor 					= {'a': 'almond', 'l': 'anise', 'c': 'creosote', 'y': 'fishy', 'f': 'foul', 'm': 'musty', 'n': 'none', 'p': 'pungent', 's': 'spicy'}
gillAttachment 			= {'a': 'attached', 'd': 'descending', 'f': 'free', 'n': 'notched'}
gillSpacing 			= {'c': 'close', 'w': 'crowded', 'd': 'distant'}
gillSize 				= {'b': 'broad', 'n': 'narrow'}
gillColor 				= {'k': 'black', 'n': 'brown', 'b': 'buff', 'h': 'chocolate', 'g': 'gray', 'r': ' green', 'o': 'orange', 'p': 'pink', 'u': 'purple', 'e': 'red', 'w': 'white', 'y': 'yellow'}
stalkShape 				= {'e': 'enlarging', 't': 'tapering'}
stalkRoot 				= {'b': 'bulbous', 'c': 'club', 'u': 'cup', 'e': 'equal', 'z': 'rhizomorphs', 'r': 'rooted', '?': 'missing'}
stalkSurfaceAboveRing 	= {'f': 'fibrous', 'y': 'scaly', 'k': 'silky', 's': 'smooth'}
stalkSurfaceBelowRing 	= {'f': 'fibrous', 'y': 'scaly', 'k': 'silky', 's': 'smooth'}
stalkColorAboveRing 	= {'n': 'brown', 'b': 'buff', 'c': 'cinnamon', 'g': 'gray', 'o': 'orange', 'p': 'pink', 'e': 'red', 'w': 'white', 'y': 'yellow'}
stalkColorBelowRing 	= {'n': 'brown', 'b': 'buff', 'c': 'cinnamon', 'g': 'gray', 'o': 'orange', 'p': 'pink', 'e': 'red', 'w': 'white', 'y': 'yellow'}
veilType 				= {'p': 'partial', 'u': 'universal'}
veilColor 				= {'n': 'brown', 'o': 'orange', 'w': 'white', 'y': 'yellow'}
ringNumber 				= {'n': 'none', 'o': 'one', 't': 'two'}
ringType 				= {'c': 'cobwebby', 'e': 'evanescent', 'f': 'flaring', 'l': 'large', 'n': 'none', 'p': 'pendant', 's': 'sheathing', 'z': 'zone'}
sporePrintColor 		= {'k': 'black', 'n': 'brown', 'b': 'buff', 'h': 'chocolate', 'r': 'green', 'o': 'orange', 'u': 'purple', 'w': 'white', 'y': 'yellow'}
population 				= {'a': 'abundant', 'c': 'clustered', 'n': 'numerous', 's': 'scattered', 'v': 'several', 'y': 'solitary'}
habitat 				= {'g': 'grasses', 'l': 'leaves', 'm': 'meadows', 'p': 'paths', 'u': 'urban', 'w': 'waste', 'd': 'woods'}

variables 				= [capShape,capSurface,capColor,bruises,odor,gillAttachment,gillSpacing,gillSize,gillColor,stalkShape,stalkRoot,stalkSurfaceAboveRing,stalkSurfaceBelowRing,stalkColorAboveRing,stalkColorBelowRing,veilType,veilColor,ringNumber,ringType,sporePrintColor,population,habitat]
translator				= {'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4, 'f': 5, 'g': 6, 'h': 7, 'k': 8, 'l': 9, 'm': 10, 'n': 11, 'o': 12, 'p': 13, 'r': 14, 's': 15, 't': 16, 'u': 17, 'v': 18, 'x': 19, 'w': 20, 'y': 21, 'z': 22, '?': 23}

classifier 				= {'e': 'edible', 'p': 'poisonous', 0: 'edible', 1: 'poisonous'}


def translateValues(values, to):
	values = values[:]
	if to == 'int': #char para int
		for i in range(len(values)):
			values[i] = [translator[x] for x in values[i]]
	elif to == 'str': #char para string
		for i in range(len(values)):
			values[i] = [variables[values[i].index(x)][x] for x in values[i]]
	else:
		print "Converter apenas para 'int' ou 'str'!"
		return null
	return values

def translateLine(values):
	values = values[:]
	for i in range(len(values)):
		values[i] = variables[i][getKey(translator, values[i])]
	return values

def translateClassifier(values, to):
	values = values[:]
	if to == 'int':
		for i in range(len(values)):
			values[i] = 1 if values[i] == 'p' else 0
	elif to == 'str':
		for i in range(len(values)):
			values[i] = classifier[values[i]]
	else:
		print "Converter apenas para 'int' ou 'str'!"
		return null
	return values



def getKey(dictionary, fromValue):
	for key, value in dictionary.iteritems():
		if value == fromValue:
			return key
