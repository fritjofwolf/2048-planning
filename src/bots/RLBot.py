import numpy as np
from baseBot import BaseBot

class RLBot(BaseBot):
	
	def __init__(self):
		# initialize weights for action-value function
		weights = np.random.rand(17)
		oldFeatures = np.zeros(17)
		newFeatures = np.zeros(17)
		oldScore = 0
		newScore = 0
		epsilon = 1
		e = np.zeros(17)
