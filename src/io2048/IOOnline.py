import numpy as np
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class IOOnline:
	""" IOManager to interact with the website http://gabrielecirulli.github.io/2048/
	where the 2048 game can be played online. This is naturally quite slow, so
	for training the reinforcement learning agent an offline version of the game is used.
	"""

	def __init__(self):
		# Initialize Driver to interact with the website
		self._driver = webdriver.Firefox()
		self._driver.get("http://gabrielecirulli.github.io/2048/")
		self._elem = self._driver.find_element_by_class_name("grid-container")
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
		gameStateRaw = self._driver.execute_script("return localStorage.getItem('gameState')")
		if not gameStateRaw:
			return None
		gameState = gameStateRaw[26:-1].split("]]},")

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

	def restartGame(self):
		self._driver.find_element_by_class_name("restart-button").click()

	def closeGame(self):
		self._driver.close()

	def makeMove(self, move):
		"""
		sends the selected move to the website
		"""
		if move == 0:
			self._elem.send_keys(Keys.ARROW_UP)
		elif move == 1:
			self._elem.send_keys(Keys.ARROW_RIGHT)
		elif move == 2:
			self._elem.send_keys(Keys.ARROW_DOWN)
		else:
			self._elem.send_keys(Keys.ARROW_LEFT)
