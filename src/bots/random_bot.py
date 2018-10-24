import numpy as np

class RandomBot():

    def compute_next_action(self, state):
        return np.random.randint(4)