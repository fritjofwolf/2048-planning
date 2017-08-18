
import time
import sys
import numpy as np
import RL_Methods as rlm
import greadyMethod as gm

#a = '{"grid":{"size":4,"cells":[[null,null,null,null],[null,null,null,null],
#[{"position":{"x":2,"y":0},"value":2},null,null,null],
#[null,null,{"position":{"x":3,"y":2},"value":4},
#{"position":{"x":3,"y":3},"value":4}]]},"score":8,"over":false,
#"won":false,"keepPlaying":false}'

#b = '{"grid":{"size":4,"cells":[[null,null,null,null],[null,null,null,null],[{"position":{"x":2,"y":0},"value":2},null,null,null],[null,null,{"position":{"x":3,"y":2},"value":4},{"position":{"x":3,"y":3},"value":4}]]},"score":8,"over":false,"won":false,"keepPlaying":false}'


def extractInfos(gameState):
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
	
def makeMove(elem, move):
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
	
	
# Initialize Driver to interact with the website
driver = webdriver.Firefox()
driver.get("http://gabrielecirulli.github.io/2048/")
elem = driver.find_element_by_class_name("grid-container")

# initialize weights for action-value function
weights = np.random.rand(17)
oldFeatures = np.zeros(17)
newFeatures = np.zeros(17)
oldScore = 0
newScore = 0
epsilon = 1
e = np.zeros(17)

summe = 0
n = 10
random = False
# Greedy approach
for i in range(n):
	gameStateRaw = driver.execute_script("return localStorage.getItem('gameState')")
	gameState = extractInfos(gameStateRaw)
	move = np.random.randint(4)
	makeMove(elem,move)
	print(gameState['grid'])
	gameStateRaw = driver.execute_script("return localStorage.getItem('gameState')")
	while gameStateRaw:
		gameState = extractInfos(gameStateRaw)
		if (random):
			move = np.random.randint(4)
		else:
			move = gm.selectMove(gameState["grid"])
		makeMove(elem, move)
		#time.sleep(1)
		gameStateRaw = driver.execute_script("return localStorage.getItem('gameState')")
		score = gameState["score"]
	print(score)
	summe += score
	driver.find_element_by_class_name("restart-button").click()

print("Average score is:", summe/n)
		
# Reinforcement Learning approach
"""
# Loop over episodes
for i in range(30):
	if i == 20:
		print("Finished training")
		epsilon = 0.05
	
	gameStateRaw = driver.execute_script("return localStorage.getItem('gameState')")
	gameState = extractInfos(gameStateRaw)
	# Select next move
	if np.random.rand() < epsilon: # exploration
		move = np.random.randint(4)
		makeMove(elem,move)
	else: # exploitation
		move = rlm.selectAction(gameState["grid"],weights)
	oldScore = gameState["score"]
	oldFeatures = rlm.makeFeatures(gameState["grid"], move)
	makeMove(elem, move)
	gameStateRaw = driver.execute_script("return localStorage.getItem('gameState')")
	
	while gameStateRaw: # while game is not over
		gameState = extractInfos(gameStateRaw)
		newScore = gameState["score"]
		
		# Select next move
		if np.random.rand() < epsilon: # exploration
			move = np.random.randint(4)
		else: # exploitation
			move = rlm.selectAction(gameState["grid"],weights)
		newFeatures = rlm.makeFeatures(gameState["grid"], move)
		
		# Update action-value function
		[weights,e] = rlm.updateAVFunction(weights, newScore-oldScore,oldFeatures, newFeatures,e)
		#weights = weights / np.linalg.norm(weights)
		#print(oldFeatures)
		#print(weights)
		oldFeatures = newFeatures
		oldScore = newScore
		makeMove(elem, move)
		gameStateRaw = driver.execute_script("return localStorage.getItem('gameState')")
		
	print(oldScore)
	print(np.linalg.norm(weights))
	# start a new game
	driver.find_element_by_class_name("restart-button").click()
	epsilon = epsilon * 0.95
		
print(weights)
"""

time.sleep(10)
driver.close()

