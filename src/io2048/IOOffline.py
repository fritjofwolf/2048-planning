import numpy as np
import random

class IOOffline:
	""" IOManager to manage an own implemenation of the game. This is much faster
	than to interact with an website and therefore used for training. For purposes
	of demonstration use the online version.
	"""

	def __init__(self):
		self._gameState = {"score": 0, 
							"grid": np.zeros((4,4)), 
							"over": False, 
							"won": False, 
							"keepPlaying": True
							}
		self.addRandomTile()
		self.addRandomTile()


	def extractInfos(self):
		"""
		Output:
		dictonary with different gamestate values
				score - int value, that stores the current points
				board - 4x4 array, which stores the numbers on the board

		"""
		if self._gameState['over']:
			return None
		else:
			return self._gameState

	def startNewGame(self):
		self._gameState = {"score": 0, 
							"grid": np.zeros((4,4)), 
							"over": False, 
							"won": False, 
							"keepPlaying": True
							}
		self.addRandomTile()
		self.addRandomTile()

	def closeGame(self):
		self._gameState = None

	def addRandomTile(self):
		emptyTiles = np.where(self._gameState["grid"] == 0)
		if (len(emptyTiles[0]) > 0):
			tmp = np.random.randint(len(emptyTiles[0]))
			tmp2 = 2 if np.random.rand() < 0.9 else 4
			self._gameState["grid"][emptyTiles[0][tmp], emptyTiles[1][tmp]] = tmp2
			return 1
		else:
			return 0

	def computeRowReward(self, row):
		"""
		Computes the reward that is returned for the given row, when the
		numbers collapes to the left of the given row
		"""
		# Delete all empty cells
		row2 = []
		for i in row:
			if (i != 0):
				row2.append(i)
		
		# Explicitely compute the reward for the different cases
		# According to the rules a number can only be merged once per move!
		reward = 0
		if (len(row2) > 1 and row2[0] == row2[1]):
			reward += 2*row2[0]
			row2[0] = 2*row2[0]
			row2[1] = 0
			if (len(row2) == 4 and row2[2] == row2[3]):
				reward += 2*row2[2]
				row2[1] = 2*row2[2]
				row2[2] = 0
				row2[3] = 0
		elif (len(row2) > 2 and row2[1] == row2[2]):
			reward += 2*row2[1]
			row2[1] = 2*row2[1]
			row2[2] = 0
		elif (len(row2) == 4 and row2[2] == row2[3]):
			reward += 2*row2[2]
			row2[2] = 2*row2[2]
			row2[3] = 0
		
		# clean up
		row3 = []
		for i in row2:
			if (i != 0):
				row3.append(i)
		while len(row3) < 4:
			row3.append(0)
		#print(row,row2)
		return [row3,reward]

	def computeReward(self, move):
		"""
		Computes the new grid after a move

		This method receives a move and can compute the new grid from the rules given
		for 2048 and the old grid.
		Input:
			move - integer value from 0 to 3 (0 = up, 1 = right, 2 = down, 3 = left)
		"""
		reward = 0
		tmp = -1
		grid = self._gameState['grid'].copy()
		if move == 0:
			for i in range(4):
				[row,rowReward] = self.computeRowReward(grid[:,i])
				reward += rowReward
				grid[:,i] = row
		elif move == 1:
			for i in range(4):
				[row,rowReward] = self.computeRowReward(grid[i,::-1])
				reward += rowReward
				grid[i,::-1] = row
		elif move == 2:
			for i in range(4):
				[row,rowReward] = self.computeRowReward(grid[::-1,i])
				reward += rowReward
				grid[::-1,i] = row
		elif move == 3:
			for i in range(4):
				[row,rowReward] = self.computeRowReward(grid[i,:])
				reward += rowReward
				grid[i,:] = row
		return [grid, reward]
		
	def makeMove(self, move):	
		"""
		Main method to handle the game logic

		Tries to make the given move, if not possible checks if there
		are legal moves left. In case the given move is legal, adds a new
		random tile to the grid.
		"""
		[grid,reward] = self.computeReward(move)
		if (self._gameState['grid'] == grid).all(): # illegal move
			for i in range(4):
				[grid,reward] = self.computeReward(i)
				if not (self._gameState['grid'] == grid).all():
					break
			else: # no legal move left
				self._gameState['over'] = True
				self._gameState['keepPlaying'] = False
		else: # legal move
			self._gameState['grid'] = grid
			self._gameState['score'] += reward
			self.addRandomTile()
				