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

    input_row = np.array([1,1,2,2])
    expected_output = np.array([2,4,0,0])
    expected_reward = 6
    merged_row, reward = io._merge_row_cells_to_the_left(input_row)
    assert((merged_row == expected_output).all())
    assert(reward == expected_reward)

    input_row = np.array([1,1,1,1])
    expected_output = np.array([2,2,0,0])
    expected_reward = 4
    merged_row, reward = io._merge_row_cells_to_the_left(input_row)
    assert((merged_row == expected_output).all())
    assert(reward == expected_reward)

    input_row = np.array([0,0,0,2])
    expected_output = np.array([2,0,0,0])
    expected_reward = 0
    merged_row, reward = io._merge_row_cells_to_the_left(input_row)
    assert((merged_row == expected_output).all())
    assert(reward == expected_reward)

    input_row = np.array([3,1,1,2])
    expected_output = np.array([3,2,2,0])
    expected_reward = 2
    merged_row, reward = io._merge_row_cells_to_the_left(input_row)
    assert((merged_row == expected_output).all())
    assert(reward == expected_reward)

    input_row = np.array([1,2,3,4])
    expected_output = np.array([1,2,3,4])
    expected_reward = 0
    merged_row, reward = io._merge_row_cells_to_the_left(input_row)
    assert((merged_row == expected_output).all())
    assert(reward == expected_reward)

    input_row = np.array([2,1,4,4])
    expected_output = np.array([2,1,8,0])
    expected_reward = 8
    merged_row, reward = io._merge_row_cells_to_the_left(input_row)
    assert((merged_row == expected_output).all())
    assert(reward == expected_reward)


def test_make_move():
    io = IOOffline()
    
    io._board = np.array([[0,0,2,2],[4,2,8,2],[2,2,4,8],[16,2,2,8]])
    expected_board = np.array([[4,0,0,0],[4,2,8,2],[4,4,8,0],[16,4,8,0]])
    expected_reward = 12
    new_board, reward = io._make_move(3)
    assert((new_board == expected_board).all())
    assert(reward == expected_reward)

    io._board = np.array([[0,0,2,2],[4,2,8,2],[2,2,4,8],[16,2,2,8]])
    expected_board = np.array([[0,0,2,0],[4,0,8,0],[2,2,4,4],[16,4,2,16]])
    expected_reward = 24
    new_board, reward = io._make_move(2)
    assert((new_board == expected_board).all())
    assert(reward == expected_reward)

    io._board = np.array([[0,0,2,2],[4,2,8,2],[2,2,4,8],[16,2,2,8]])
    expected_board = np.array([[0,0,0,4],[4,2,8,2],[0,4,4,8],[0,16,4,8]])
    expected_reward = 12
    new_board, reward = io._make_move(1)
    assert((new_board == expected_board).all())
    assert(reward == expected_reward)

    io._board = np.array([[0,0,2,2],[4,2,8,2],[2,2,4,8],[16,2,2,8]])
    expected_board = np.array([[4,4,2,4],[2,2,8,16],[16,0,4,0],[0,0,2,0]])
    expected_reward = 24
    new_board, reward = io._make_move(0)
    assert((new_board == expected_board).all())
    assert(reward == expected_reward)

    io._board = np.array([[8, 2, 0, 0,],[8, 2, 0, 0,],[2, 8, 2, 0,],[2, 4, 2, 0,]])
    expected_board = np.array([[16,4,4,0],[4,8,0,0],[0,4,0,0],[0,0,0,0]])
    expected_reward = 28
    new_board, reward = io._make_move(0)
    assert((new_board == expected_board).all())
    assert(reward == expected_reward)

    

def test_is_done():
    io = IOOffline()
    io._board = np.array([[ 4,  2,  4,  2], [32, 64, 16,  8], [16,  4, 32,  4], [ 4,  2,  8,  2]])
    assert(io._is_done() == True)

    