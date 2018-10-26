import pytest
import numpy as np
from io2048.io_online import IOOnline

# def test_dummy():
#     io = IOOnline()
#     state = io.reset()
#     done = False
#     while not done:
#         action = np.random.randint(4)
#         state, reward, done = io.step(action)
#     io.close_game()


if __name__ == '__main__':
    io = IOOnline()
    state = io.reset()
    done = False
    while not done:
        action = np.random.randint(4)
        state, reward, done = io.step(action)
    io.close_game()