import numpy as np
import time
from multiprocessing import Pool
from io2048.io_offline import IOOffline
from bots.random_bot import RandomBot
from bots.rollout_bot import RolloutBot
from rl_bots.deepneuroevolution_bot import DeepNeuroevolution

if __name__ == '__main__':
    # bot = RolloutBot(IOOffline(), RandomBot(), 1)
    n_features = 16
    n_actions = 4
    env = IOOffline()
    dne = DeepNeuroevolution(env, 20, 5, n_features, n_actions, (10,), 2000)
    dne.find_optimal_network()
    # iterations = 100
    # n_processors = 4
    # cnt = 0
    # total_time, average_score, average_time = evaluate_bot(iterations, n_processors)
    # print('The total time was:', total_time)
    # print('The average score per episode was:', average_score)
    # print('The average time per episode was:', average_time)




dne.find_optimal_network()