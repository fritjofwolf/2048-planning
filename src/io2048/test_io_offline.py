import pytest
import numpy as np
from io2048.io_offline import IOOffline

def test_reset():
    io = IOOffline()
    state = io.reset()
    assert(len(np.where(state != 0)[0]) == 2)
    assert(np.sum(state) >=4 and np.sum(state) <= 8)

def test_step():
    io = IOOffline()
    state = io.reset()
    next_state, reward, done = io.step(0)
    next_state, reward, done = io.step(1)
    next_state, reward, done = io.step(2)
    next_state, reward, done = io.step(3)


def test_merge_row_cells_to_the_left():
    io = IOOffline()
    input_row = [1,2,3,4]
    expected_output = [1,2,3,4]
    assert(io._merge_row_cells_to_the_left(input_row) == expected_output)