import pytest
import numpy as np
from io2048.io_offline import IOOffline

def test_reset():
    io = IOOffline()
    state = io.reset()
    assert(len(np.where(state != 0)[0]) == 2)
    assert(np.sum(state) >=4 and np.sum(state) <= 8)