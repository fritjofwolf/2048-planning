import numpy as np


class IOBase:
	""" IOManager to interact with the website http://gabrielecirulli.github.io/2048/
	where the 2048 game can be played online. This is naturally quite slow, so
	for training an offline version of the game is used.
	"""

	def __init__(self):
		self._gameState = {}


	def extractInfos(self):
		""" Extracts all necessary information from the enviroment, such as
		the current game state, reward etc.
		"""
		pass

	def makeMove(self, move):
		""" Makes a given move and so that a new state of the
		gameboard is computed
		"""
		pass
