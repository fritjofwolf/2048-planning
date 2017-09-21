from io2048.IOOnline import IOOnline
from io2048.IOOffline import IOOffline
from bots.PolicyBasedLocalSearch import PolicyBasedLocalSearch as PolicyBot
from bots.greedyBot import GreedyBot
import time
import sys
import numpy as np


if __name__ == '__main__':
	#ioManager = IOOnline()
	ioManager = IOOffline()
	bot = PolicyBot()
	#bot = GreedyBot() 
	# print(ioManager.extractInfos())

	bestScore = 0
	bestScoreWeights1 = np.random.randn(16,16)
	bestScoreWeights2 = np.random.randn(16,4)
	
	iterations = 2000
	for i in range(1000):
		currentScore = 0
		currentWeights1 = bestScoreWeights1 + np.random.randn(16,16)
		currentWeights2 = bestScoreWeights2 + np.random.randn(16,4)
		bot.setWeights(currentWeights1,currentWeights2)
		for j in range(iterations):
			infos = ioManager.extractInfos()
			while infos:
				score = infos['score']
				
				#print(infos['grid'],infos['score'])
				move = bot.selectMove(infos)
				#print(move)
				ioManager.makeMove(move)
				infos = ioManager.extractInfos()
				#print(infos['grid'])
			#print(infos)
			currentScore += score
			ioManager.startNewGame()
			
		currentScore /= iterations
		print('currentScore is ',currentScore)
		if currentScore > bestScore:
			bestScoreWeights1 = currentWeights1
			bestScoreWeights2 = currentWeights2
			bestScore = currentScore

	print('bestScore and weights', bestScore, bestScoreWeights1, bestScoreWeights2)
	#time.sleep(1)
	ioManager.closeGame()