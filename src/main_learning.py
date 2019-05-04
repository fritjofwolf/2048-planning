import numpy as np
import time
from multiprocessing import Pool
from io2048.io_offline import IOOffline
from bots.random_bot import RandomBot
from bots.rollout_bot import RolloutBot
from rl_bots.ppo import PPO
import matplotlib.pyplot as plt
from scipy import polyfit

if __name__ == '__main__':
    ppo_agent = PPO()
    results = ppo_agent.train(2*10**4)


