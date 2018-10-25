import numpy as np
from multiprocessing import Pool
    
class RolloutBot():

    def __init__(self, env, bot, iterations):
        self._env = env
        self._bot = bot
        self._iterations = iterations

    def compute_next_action(self, state):
        action_values = np.zeros(4)
        p = Pool(5)
        self._state = state
        action_values = p.map(self._compute_action_value, [0,1,2,3])

        # for action in range(4):
        #     action_values[action] = self._compute_action_value(state, action)
        return np.argmax(action_values)

    def _compute_action_value(self, action):
        summe = 0
        state = self._state
        for i in range(self._iterations):
            summe += self._compute_trajectory_value(state, action)
        action_value = summe / self._iterations
        return action_value
    
    def _compute_trajectory_value(self, state, action):
        summe = 0
        env = self._env
        env.reset()
        env._board = state
        state, reward, done = env.step(action)
        summe += reward
        while not done:
            action = self._bot.compute_next_action(state)
            state, reward, done = env.step(action)
            summe += reward
        return summe