import numpy as np
from baseBot import BaseBot

class RandomBot(BaseBot):
	
	def selectMove(self,infos):
		move = np.random.randint(4)
		return move