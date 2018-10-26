import numpy as np
from bots.heuristic_search_bot import HeuristicSearchBot

def test_compute_next_action_depth_1():
    bot = HeuristicSearchBot(1)
    state = np.array([[2,2,4,4],[0,2,0,4],[4,4,4,128],[2,4,0,128]])
    expected_result = 2
    assert(bot.compute_next_action(state) == expected_result)
