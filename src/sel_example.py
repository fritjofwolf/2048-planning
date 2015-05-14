from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


a = '{"grid":{"size":4,"cells":[[null,null,null,null],[null,null,null,null],[{"position":{"x":2,"y":0},"value":2},null,
null,null],[null,null,{"position":{"x":3,"y":2},"value":4},{"position":{"x":3,"y":3},"value":4}]]},"score":8,"over":false,
"won":false,"keepPlaying":false}'



""" Extracts the information from the gameState string provided
	by the local storage
	Output: score - int value, that stores the current points
			board - 4x4 array, which stores the numbers on the board
			
"""
def extractInfos(gameState):
	gameState = gameState[1:-1].split(",")
	
	
	
print(extractInfos(a))


driver = webdriver.Firefox()
driver.get("http://gabrielecirulli.github.io/2048/")
elem = driver.find_element_by_class_name("grid-container")


for i in range(1):
	#print(driver.find_element_by_class_name("score-container").text)
	for j in range(1):
		elem.send_keys(Keys.ARROW_DOWN)
		elem.send_keys(Keys.ARROW_LEFT)
	elem.send_keys(Keys.ARROW_RIGHT)
	
result = driver.execute_script("return localStorage.getItem('gameState')")
#print(driver.get("return javascript:localStorage.getItem('bestScore');"))
#elem.send_keys(Keys.ARROW_DOWN)
print(result.split(","))
#print(driver.find_element_by_class_name("score-container").text)
time.sleep(3)
driver.close()
