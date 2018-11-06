import numpy as np
import time
from multiprocessing import Pool
from io2048.io_offline import IOOffline
from bots.random_bot import RandomBot
from bots.rollout_bot import RolloutBot

def evaluate_bot(iterations, n_processors):
    start_time = time.time()
    p = Pool(2)
    scores = p.map(evaluate_single_run, [iterations]*iterations)
    p.close()
    stop_time = time.time()
    average_score = sum(scores) / iterations
    average_time = n_processors * (stop_time - start_time) / iterations
    return average_score, average_time

def evaluate_single_run(dummy):
    global env
    global bot
    score = 0
    state = env.reset()
    done = False
    while not done:
        action = bot.compute_next_action(state)
        state, reward, done = env.step(action)
        score += reward
    return score

if __name__ == '__main__':
    # bot = RolloutBot(IOOffline(), RandomBot(), 1)
    bot = RandomBot()
    env = IOOffline()
    iterations = 100
    n_processors = 2
    cnt = 0
    average_score, average_time = evaluate_bot(iterations, n_processors)
    print('The average score per episode was:', average_score)
    print('The average time per episode was:', average_time)