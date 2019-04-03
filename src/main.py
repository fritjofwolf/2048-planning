import numpy as np
import time
from multiprocessing import Pool
from io2048.io_offline import IOOffline
from io2048.io_online import IOOnline
from bots.random_bot import RandomBot
from bots.rollout_bot import RolloutBot
from bots.heuristic_search_bot import HeuristicSearchBot
import time

def evaluate_bot(iterations, n_processors):
    start_time = time.time()
    p = Pool(n_processors)
    scores = p.map(evaluate_single_run, [iterations]*iterations)
    p.close()
    stop_time = time.time()
    total_time = (stop_time -start_time)
    average_score = sum(scores) / iterations
    average_time = n_processors * (stop_time - start_time) / iterations
    return total_time, average_score, average_time, scores

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
    bot = RolloutBot(IOOffline(), RandomBot(), 1)
    #bot = HeuristicSearchBot(2)
    #bot = RandomBot()
    env = IOOffline()
    iterations = 10
    n_processors = 1
    cnt = 0
    #time.sleep(20)
    total_time, average_score, average_time, scores = evaluate_bot(iterations, n_processors)
    print('The total time was:', total_time)
    print('The average score per episode was:', average_score)
    print('The average time per episode was:', average_time)
    print('Individual Scores are:', scores)