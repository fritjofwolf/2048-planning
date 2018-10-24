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
            done = self._is_done()
            self._update_state(next_state, reward, done)
            return next_state, reward, done
        else:
            done = self._is_done()
            return self._board, 0, done

    def _is_done(self):
        for i in range(4):
            tmp_board, reward = self._make_move(i)
            if (tmp_board != self._board).any():
                return False
        return True

    def _merge_row_cells_to_the_left(self, row):
        merged_row = np.zeros(4)
        shifted_row = row[row!=0]
        shifted_row = np.append(shifted_row, [0]*(4-shifted_row.shape[0]))
        if shifted_row[0] == shifted_row[1] and shifted_row[2] != shifted_row[3]:
            merged_row[0] = 2*shifted_row[0]
            merged_row[1] = shifted_row[2]
            merged_row[2] = shifted_row[3]
            reward = 2*shifted_row[0]
        elif shifted_row[0] == shifted_row[1] and shifted_row[2] == shifted_row[3]:
            merged_row[0] = 2*shifted_row[0]
            merged_row[1] = 2*shifted_row[2]
            reward = 2*shifted_row[0] + 2*shifted_row[2]
        elif shifted_row[1] == shifted_row[2]:
            merged_row[0] = shifted_row[0]
            merged_row[1] = 2*shifted_row[1]
            merged_row[2] = shifted_row[3]
            reward = 2*shifted_row[1]
        elif shifted_row[2] == shifted_row[3]:
            merged_row[0] = shifted_row[0]
            merged_row[1] = shifted_row[1]
            merged_row[2] = 2*shifted_row[2]
            reward = 2*shifted_row[2]
        else:
            merged_row = shifted_row
            reward = 0
        return merged_row, reward

    def _update_state(self, next_state, reward, done):
        self._board = next_state
        self._score += reward
        self._done = done

    def _make_move(self, action):
        if action == 0:
            tmp_board, reward = self._compute_row_merges(self._board.T)
            new_board = tmp_board.T
        elif action == 1:
            tmp_board, reward = self._compute_row_merges(self._board.T[::-1].T)
            new_board = tmp_board.T[::-1].T
        elif action == 2:
            tmp_board, reward = self._compute_row_merges(self._board[::-1].T)
            new_board = tmp_board.T[::-1]
        else:
            tmp_board, reward = self._compute_row_merges(self._board)
            new_board = tmp_board
        return new_board, reward

    def _compute_row_merges(self, board):
        tmp_board = np.zeros((4,4))
        reward = 0
        for i in range(4):
            tmp_board[i,:], row_reward = self._merge_row_cells_to_the_left(board[i,:])
            reward += row_reward
        return tmp_board, reward

    def _add_new_tile(self, board):
        empty_tiles = np.where(board == 0)
        if (len(empty_tiles[0]) > 0):
            new_tile_position = np.random.randint(len(empty_tiles[0]))
            new_tile_value = 2 if np.random.rand() < 0.9 else 4
            board[empty_tiles[0][new_tile_position], empty_tiles[1][new_tile_position]] = new_tile_value
        return board