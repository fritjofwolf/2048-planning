import numpy as np

class IOOffline:

    def __init__(self):
        self.reset()

    def reset(self):
        self._board = np.zeros((4,4))
        self._score = 0
        self._done = False
        self._board = self._add_new_tile(self._board)
        self._board = self._add_new_tile(self._board)
        return self._board

    def step(self, action):
        tmp_state, reward = self._make_move(action)
        if (tmp_state != self._board).any():
            next_state = self._add_new_tile(tmp_state)
            done = self._check_for_finish()
            self._update_state(next_state, reward, done)
            return next_state, reward, done
        else:
            return self._board, 0, self._done

    def _merge_row_cells_to_the_left(self, row):
        merged_row = np.zeros(4)
        shifted_row = row[row!=0]
        shifted_row = np.append(shifted_row, [0]*(4-shifted_row.shape[0]))
        if shifted_row[0] == shifted_row[1] and shifted_row[2] != shifted_row[3]:
            merged_row[0] = 2*shifted_row[0]
            merged_row[1] = shifted_row[2]
            merged_row[2] = shifted_row[3]
        elif shifted_row[0] == shifted_row[1] and shifted_row[2] == shifted_row[3]:
            merged_row[0] = 2*shifted_row[0]
            merged_row[1] = 2*shifted_row[2]
        elif shifted_row[1] == shifted_row[2]:
            merged_row[0] = shifted_row[0]
            merged_row[1] = 2*shifted_row[1]
            merged_row[2] = shifted_row[3]
        else:
            merged_row = shifted_row
        return merged_row

    def _update_state(self, next_state, reward, done):
        self._board = next_state
        self._score += reward
        self._done = done

    

    
    # def _make_move(self, move):	
    # 	"""
    # 	Main method to handle the game logic

    # 	Tries to make the given move, if not possible checks if there
    # 	are legal moves left. In case the given move is legal, adds a new
    # 	random tile to the grid.
    # 	"""
    # 	[grid,reward] = self.computeReward(move)
    # 	if (self._gameState['grid'] == grid).all(): # illegal move
    # 		for i in range(4):
    # 			[grid,reward] = self.computeReward(i)
    # 			if not (self._gameState['grid'] == grid).all():
    # 				break
    # 		else: # no legal move left
    # 			self._gameState['over'] = True
    # 			self._gameState['keepPlaying'] = False
    # 	else: # legal move
    # 		self._gameState['grid'] = grid
    # 		self._gameState['score'] += reward
    # 		self.addRandomTile()


    def _add_new_tile(self, board):
        empty_tiles = np.where(board == 0)
        if (len(empty_tiles[0]) > 0):
            new_tile_position = np.random.randint(len(empty_tiles[0]))
            new_tile_value = 2 if np.random.rand() < 0.9 else 4
            board[empty_tiles[0][new_tile_position], empty_tiles[1][new_tile_position]] = new_tile_value
        return board