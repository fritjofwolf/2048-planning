import numpy as np
from bots.heuristic_search_bot import HeuristicSearchBot

def test_compute_next_action_depth_1():
    bot = HeuristicSearchBot()
    state = np.array([[2,2,4,4],[0,2,0,4],[4,4,4,128],[2,4,0,128]])
    assert(bot.compute_next_action(state, 1) == 2, 284)

    state = np.array([[8, 4, 0, 0],[4, 2, 0, 0],[4, 2, 0, 0],[8, 4, 0, 0]])
    assert(bot.compute_next_action(state, 1) == 0, 12)

def test_compute_next_action_depth_2():
    bot = HeuristicSearchBot()
    state = np.array([[1,7,0,64],[0,5,3,64],[3,32,32,1],[6,64,0,0]])
    expected_action, expected_reward = bot.compute_next_action(state,2)
    assert(expected_action == 3)