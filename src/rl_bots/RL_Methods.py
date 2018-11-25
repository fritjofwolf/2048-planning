import numpy as np


def updateAVFunction(weights, reward, oldFeatures, newFeatures,e):
	"""
	Computes a new representation of the action-value function using
	linear, gradient-descent Sarsa(0)
	"""
	alpha = 0.001
	gamma = 0.95
	lamb = 1
	
	newWeights = np.zeros(17)
	qOld = computeActionValue(weights, oldFeatures)
	qNew = computeActionValue(weights, newFeatures) 
	
	delta = reward + gamma * qNew - qOld
	#print("Delta ist ",delta)
	e = gamma*lamb*e + oldFeatures
	newWeights = weights + alpha*delta*e
	
	return [newWeights,e]
	
	
def makeFeatures(grid, action):
	"""
	Creates a feature vector for the approximate state-value function
	"""
	features = np.zeros(17)
	features[0:16] = np.matrix.flatten(grid)
	features[16] = action
	return features
	
	
def computeActionValue(weights, features):
	"""
	Returns the value of the approximate action-value function for a 
	given set of state, action and weights
	"""
	
	return np.inner(weights, features) # linear
	#return 1 / (1 + np.exp(np.inner(weights, features))) # sigmoid
	
def selectAction(grid, weights):
	"""
	Selects the greedy action given a policy
	"""
	maximum = -1000000
	max_index = -1
	
	for i in range(4):
		features = makeFeatures(grid,i)
		if computeActionValue(weights, features) > maximum:
			maximum = computeActionValue(weights, features)
			max_index = i
			
	return max_index
