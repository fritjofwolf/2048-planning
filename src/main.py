import IOManager

# Initialize Driver to interact with the website
driver = webdriver.Firefox()
driver.get("http://gabrielecirulli.github.io/2048/")
elem = driver.find_element_by_class_name("grid-container")

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

time.sleep(10)
driver.close()
