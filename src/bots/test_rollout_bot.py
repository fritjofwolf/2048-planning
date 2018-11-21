import pytest
import numpy as np
from bots.rollout_bot import RolloutBot
from bots.random_bot import RandomBot
from io2048.io_offline import IOOffline

def test_compute_next_action():
    bot = RolloutBot(IOOffline(), RandomBot(), 10)
    io = IOOffline()
    state = np.array([[1,2,1,3], [3,1,4,4], [1,2,1,8], [2,1,2,1]])
    action = bot.compute_next_action(state)
    expected_action = 1
    assert(action == expected_action)