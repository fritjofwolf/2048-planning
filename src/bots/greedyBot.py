import numpy as np
from baseBot import BaseBot

class GreedyBot(BaseBot):
	
	def __init__(self, depth):
		"""
		Creates an instance of the GreadyBot where depth is the number of
		moves the bot "thinks" ahead
		"""
		self._depth = depth
	
	# def computeReward(self, grid, move):
	# 	"""
	# 	Simulates the given move on the given grid and returns the
	# 	expected reward.
	# 	"""
	# 	reward = 0
	# 	tmp = -1
	# 	if move == 0:
	# 		for i in range(0,4):
	# 			for j in range(0,4):
	# 				pass
	# 	elif move == 1:
	# 		elem.send_keys(Keys.ARROW_RIGHT)
	# 	elif move == 2:
	# 		elem.send_keys(Keys.ARROW_DOWN)
	# 	else:
	# 		elem.send_keys(Keys.ARROW_LEFT)
	# 	return reward
		
	
			
	

	def computeRowReward(self, row):
		"""
		Computes the reward that is returned for the given row, when the
		numbers collapes to the left of the given row
		"""
		# Delete all empty cells
		row2 = []
		for i in row:
			if (i != -1):
				row2.append(i)
		
		# Explicitely compute the reward for the different cases
		# According to the rules a number can only be merged once per move!
		reward = 0
		if (len(row2) > 1 and row2[0] == row2[1]):
			reward += 2*row2[0]
			if (len(row) == 4 and row2[2] == row2[3]):
				reward += 2*row2[2]
		elif (len(row2) > 2 and row2[1] == row2[2]):
			reward += 2*row2[1]
		elif (len(row2) == 4 and row2[2] == row2[3]):
			reward += 2*row2[2]
		while len(row2) < 4:
			row2.append(0)
		return reward

	def computeReward(self, grid, move):
		"""
		Simulates the given move on the given grid and returns the
		expected reward.
		"""
		reward = 0
		tmp = -1
		if move == 0:
			for i in range(4):
				reward += self.computeRowReward(grid[:,i])
		elif move == 1:
			for i in range(4):
				reward += self.computeRowReward(grid[i,::-1])
		elif move == 2:
			for i in range(4):
				reward += self.computeRowReward(grid[::-1,i])
		else:
			for i in range(4):
				reward += self.computeRowReward(grid[i,:])
		return reward

	def selectMove(self, grid):
		move = np.random.randint(4)
		reward = 0
		for i in range(4):
			a = self.computeReward(grid, i)
			if a > reward:
				reward = a
				move = i
		return move