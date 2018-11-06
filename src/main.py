import numpy as np
import progressbar
import time
from io2048.io_offline import IOOffline
from bots.random_bot import RandomBot
from bots.rollout_bot import RolloutBot

def evaluate_bot(env, bot, iterations):
    sum_score = 0
    start_time = time.time()
    for i in progressbar.progressbar(range(iterations)):
        sum_score += evaluate_single_run(env, bot)
    stop_time = time.time()
    average_score = sum_score / iterations
    average_time = (stop_time - start_time) / iterations
    return average_score, average_time

def evaluate_single_run(env, bot):
    score = 0
    state = env.reset()
    done = False
    while not done:
        action = bot.compute_next_action(state)
        state, reward, done = env.step(action)
        score += reward
    return score

if __name__ == '__main__':
    # bot = RolloutBot(IOOffline(), RandomBot(), 10)
    bot = RandomBot()
    env = IOOffline()
    iterations = 1000
    average_score, average_time = evaluate_bot(env, bot, iterations)
    print('The average score was:', average_score)
    print('The average time was:', average_time)