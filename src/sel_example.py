from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import sys
import numpy as np

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
			grid[counter%4, counter//4] = int(puffer[8:-1])
			counter += 1
			
	gameStateDict["grid"] = grid
	
	# Extract other informations
	gridString = gameState[1].split(",")
	gameStateDict["score"] = int(gridString[0][8:])
	gameStateDict["over"] = False if gridString[1][7:] == "false" else True 
	gameStateDict["won"] = False if gridString[2][6:] == "false" else True 
	gameStateDict["keepPlaying"] = False if gridString[3][14:] == "false" else True 
	
	return gameStateDict
	
	
if "__name__" == "__main__":
	driver = webdriver.Firefox()
	driver.get("http://gabrielecirulli.github.io/2048/")
	elem = driver.find_element_by_class_name("grid-container")

	for i in range(10):
		for j in range(10):
			elem.send_keys(Keys.ARROW_DOWN)
			extractInfos(driver.execute_script("return localStorage.getItem('gameState')"))
			elem.send_keys(Keys.ARROW_LEFT)
			extractInfos(driver.execute_script("return localStorage.getItem('gameState')"))
		elem.send_keys(Keys.ARROW_RIGHT)
		extractInfos(driver.execute_script("return localStorage.getItem('gameState')"))

	time.sleep(10)
	driver.close()