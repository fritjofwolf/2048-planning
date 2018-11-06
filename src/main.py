import numpy as np
import progressbar
from io2048.io_offline import IOOffline
from bots.random_bot import RandomBot
from bots.rollout_bot import RolloutBot

def evaluate_bot(env, bot, iterations):
    sum_score = 0
    for i in progressbar.progressbar(range(iterations)):
        sum_score += evaluate_single_run(env, bot)
    average_score = sum_score / iterations
    return average_score

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
    average_score = evaluate_bot(env, bot, iterations)
    print('Average reward was:', average_score)