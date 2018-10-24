import numpy as np
from io2048.io_offline import IOOffline
from bots.random_bot import RandomBot
from bots.rollout_bot import RolloutBot

if __name__ == '__main__':
    bot = RolloutBot(IOOffline(), RandomBot(), 10)
    io = IOOffline()
    iterations = 10
    summe = 0
    for i in range(iterations):
        print('Iteration ', i)
        state = io.reset()
        done = False
        while not done:
            action = bot.compute_next_action(state)
            state, reward, done = io.step(action)
            summe += reward
        print(summe)
    print('Average reward was:', summe/iterations)