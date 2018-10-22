import numpy as np
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class IOOnline:
    """ IOManager to interact with the website http://gabrielecirulli.github.io/2048/
    where the 2048 game can be played online. This is naturally quite slow, so
    for training the reinforcement learning agent an offline version of the game is used.
    """

    def __init__(self):
        self._driver = webdriver.Firefox()
        self._driver.get("http://gabrielecirulli.github.io/2048/")
        self._elem = self._driver.find_element_by_class_name("grid-container")
        self._score = 0


    def reset(self):
        self._driver.find_element_by_class_name("restart-button").click()
        self._score = 0
        self._extract_gamestate_infos()
        return self._board


    def step(self, action):
        self._make_move(action)
        self._extract_gamestate_infos()
        return self._board, self._reward, self._done
        

    def close_game(self):
        self._driver.close()


    def _extract_gamestate_infos(self):
        game_state_raw = self._driver.execute_script("return localStorage.getItem('gameState')")
        if not game_state_raw:
            return
        game_state = game_state_raw[26:-1].split("]]},")

        board_string = game_state[0].replace("]","")
        board_string = board_string.replace("[","")
        board_string = board_string.split(",")

        board = np.zeros((4,4))
        counter = 0


        for i in range(len(board_string)):
            if "null" in board_string[i]:
                counter += 1
                continue
            elif "position" in board_string[i]:
                puffer = board_string[i+2]
                board[counter%4, counter//4] = int(np.log2(int(puffer[8:-1])))
                counter += 1

        self._board = board

        board_string = game_state[1].split(",")
        old_score = self._score
        self._score = int(board_string[0][8:])
        self._reward = old_score - self._score
        self._done = False if board_string[1][7:] == "false" else True


    def _make_move(self, action):
        if action == 0:
            self._elem.send_keys(Keys.ARROW_UP)
        elif action == 1:
            self._elem.send_keys(Keys.ARROW_RIGHT)
        elif action == 2:
            self._elem.send_keys(Keys.ARROW_DOWN)
        else:
            self._elem.send_keys(Keys.ARROW_LEFT)