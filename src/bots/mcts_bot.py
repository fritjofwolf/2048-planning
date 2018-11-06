import numpy as numpy

class Node():

    def __init__(self, state, parent, children):
        self._state = state
        self._parent = parent
        self._children = children


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

    def _initialize_tree(self, state):
        self._tree = Node(state, None, None)