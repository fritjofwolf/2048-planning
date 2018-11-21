import numpy as numpy

class Node():

    def __init__(self, state, parent, children):
        self._state = state
        self._parent = parent
        self._children = children
        self._action_values = [0,0,0,0]


class MCTSBot():

    def __init__(self, env, rollout_policy, n_iterations):
        self._env = env
        self._rollout_policy = rollout_policy
        self._n_iterations = n_iterations
        self._tree = None


    def compute_next_action(self, state):
        self._initialize_tree(state)
        self._sample_trajectories()
        action = self._select_action()
        return action

    def _sample_trajectories(self):
        for _ in range(self._n_iterations):
            leaf_node = self._select_leaf_node()
            new_leaf_node = self._expand_tree(leaf_node)
            self._rollout()
            self._backup_action_values()

    def _expand_tree(self, selected_leaf_node):
        children = []
        selected_leaf_node.children.extend(children)

    def _select_action(self):
        return np.argmax(self._tree._action_values)

    def _initialize_tree(self, state):
        self._tree = Node(state, None, [])

    def _select_leaf_node(self):
        current_node = self._tree
        while current_node._children != []:
            max_action = np.argmax(current_node._action_values)
            # todo
            #create next state with certian _action_values

            current_node = current_node._children[max_action]
        return current_node


    def _compute_next_states_with_fixed_tile(self, afterstate, tile_value):
        free_tiles = np.where(afterstate == 0)
        next_states = []
        for i,j in zip(free_tiles[0], free_tiles[1]):
            tmp = afterstate.copy()
            tmp[i,j] = tile_value
            next_states.append(tmp)
        return next_states

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