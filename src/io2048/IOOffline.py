import numpy as np


class IOOffline:
	""" IOManager to manage an own implemenation of the game. This is much faster
	than to interact with an website and therefore used for training. For purposes
	of demonstration use the online version.
	"""

	def __init__(self):
		self._gameState = {}


	def extractInfos(self):
		"""

		Extracts the information from the gameState string provided
		by the local storage of the website

		Output:
		dictonary with different gamestate values
				score - int value, that stores the current points
				board - 4x4 array, which stores the numbers on the board

		"""
		gameStateDict = {}
		gameState = gameState[26:-1].split("]]},")

		# Extract grid
		gridString = gameState[0].replace("]","")
		gridString = gridString.replace("[","")
		gridString = gridString.split(",")

		grid = np.zeros((4,4))
		counter = 0


		for i in range(len(gridString)):
			if "null" in gridString[i]:
				counter += 1
				continue
			elif "position" in gridString[i]:
				puffer = gridString[i+2]
				grid[counter%4, counter//4] = int(np.log2(int(puffer[8:-1])))
				counter += 1

		gameStateDict["grid"] = grid
		#print(grid)
		#time.sleep(3)

		# Extract other informations
		gridString = gameState[1].split(",")
		gameStateDict["score"] = int(gridString[0][8:])
		gameStateDict["over"] = False if gridString[1][7:] == "false" else True
		gameStateDict["won"] = False if gridString[2][6:] == "false" else True
		gameStateDict["keepPlaying"] = False if gridString[3][14:] == "false" else True

		return gameStateDict

	def makeMove(self, elem, move):
		"""
		sends the selected move to the website
		"""
		if move == 0:
			elem.send_keys(Keys.ARROW_UP)
		elif move == 1:
			elem.send_keys(Keys.ARROW_RIGHT)
		elif move == 2:
			elem.send_keys(Keys.ARROW_DOWN)
		else:
			elem.send_keys(Keys.ARROW_LEFT)
