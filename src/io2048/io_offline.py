import numpy as np

class IOOffline:

    def __init__(self):
        self.reset()

    def reset(self):
        self._board = np.zeros((4,4))
        self._score = 0
        self._done = False
        self._add_new_tile()
        self._add_new_tile()
        return self._board

    def step(self, action):
        pass

    def makeMove(self, move):	
		"""
		Main method to handle the game logic

		Tries to make the given move, if not possible checks if there
		are legal moves left. In case the given move is legal, adds a new
		random tile to the grid.
		"""
		[grid,reward] = self.computeReward(move)
		if (self._gameState['grid'] == grid).all(): # illegal move
			for i in range(4):
				[grid,reward] = self.computeReward(i)
				if not (self._gameState['grid'] == grid).all():
					break
			else: # no legal move left
				self._gameState['over'] = True
				self._gameState['keepPlaying'] = False
		else: # legal move
			self._gameState['grid'] = grid
			self._gameState['score'] += reward
			self.addRandomTile()


    def _add_new_tile(self):
        empty_tiles = np.where(self._board == 0)
        if (len(empty_tiles[0]) > 0):
            new_tile_position = np.random.randint(len(empty_tiles[0]))
            new_tile_value = 2 if np.random.rand() < 0.9 else 4
            self._board[empty_tiles[0][new_tile_position], empty_tiles[1][new_tile_position]] = new_tile_value