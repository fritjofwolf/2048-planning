import numpy as np

class HeuristicSearchBot:

    def __init__(self, depth):
        self._state = np.zeros((4,4))
        self._depth = depth

    def compute_next_action(self, state, depth=3):
        if depth == self._depth and (state == self._state).all():
            return np.random.randint(4), 0
        if depth == self._depth:
            self._state = state.copy()
        afterstates, action_values = self._compute_afterstates(state)
        if self._is_not_a_leaf(depth):
            action_values += [self._compute_expected_reward(x, depth) for x in afterstates]
        action, value = self._select_action(action_values)
        return action, value


    def _compute_expected_reward(self, afterstate, depth):
        next_states_with_2 = self._compute_next_states_with_fixed_tile(afterstate, 2)
        next_states_with_4 = self._compute_next_states_with_fixed_tile(afterstate, 4)
        action_values_with_2 = [self.compute_next_action(x, depth-1)[1] for x in next_states_with_2]
        action_values_with_4 = [self.compute_next_action(x, depth-1)[1] for x in next_states_with_4]
        afterstate_value = self._compute_afterstate_value(action_values_with_2, action_values_with_4)
        return afterstate_value


    def _compute_afterstate_value(self, action_values_with_2, action_values_with_4):
        mean_2 = 0
        mean_4 = 0
        if action_values_with_2 != []:
            mean_2 = np.mean(action_values_with_2)
        if action_values_with_4 != []:
            mean_4 =  np.mean(action_values_with_4)
        return 0.9 *  mean_2 + 0.1 * mean_4


    def _compute_next_states_with_fixed_tile(self, afterstate, tile_value):
        free_tiles = np.where(afterstate == 0)
        next_states = []
        for i,j in zip(free_tiles[0], free_tiles[1]):
            tmp = afterstate.copy()
            tmp[i,j] = tile_value
            next_states.append(tmp)
        return next_states

    def _select_action(self, action_values):
        return np.argmax(action_values), np.max(action_values) 


    def _is_not_a_leaf(self, depth):
        return depth > 1


    def _compute_afterstates(self, state):
        afterstates = []
        action_values = np.zeros(4)
        for action in range(4):
            new_state, reward = self._make_move(state, action)
            afterstates.append(new_state)
            action_values[action] = reward
        return afterstates, action_values


    def _make_move(self, state, action):
        if action == 0:
            tmp_board, reward = self._compute_row_merges(state.T)
            new_state = tmp_board.T
        elif action == 1:
            tmp_board, reward = self._compute_row_merges(state.T[::-1].T)
            new_state = tmp_board.T[::-1].T
        elif action == 2:
            tmp_board, reward = self._compute_row_merges(state[::-1].T)
            new_state = tmp_board.T[::-1]
        else:
            tmp_board, reward = self._compute_row_merges(state)
            new_state = tmp_board
        return new_state, reward


    def _compute_row_merges(self, board):
        tmp_board = np.zeros((4,4))
        reward = 0
        for i in range(4):
            tmp_board[i,:], row_reward = self._merge_row_cells_to_the_left(board[i,:])
            reward += row_reward
        return tmp_board, reward


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