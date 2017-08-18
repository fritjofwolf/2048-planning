from io2048.IOOnline import IOOnline
from bots.RandomBot import RandomBot
from bots.greedyBot import GreedyBot
import time
import sys


if __name__ == '__main__':
	ioManager = IOOnline()
	bot = RandomBot()
	#bot = GreedyBot() 

	for i in range(1):
		infos = ioManager.extractInfos()
		while infos:
			score = infos['score']
			move = bot.selectMove(infos)
			ioManager.makeMove(move)
			infos = ioManager.extractInfos()
		print(score)

	time.sleep(1)
	ioManager.closeGame()