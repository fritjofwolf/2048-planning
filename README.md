# 2048-planning
Decision-time planning algorithms for the game 2048 (https://github.com/gabrielecirulli/2048)


Also includes an offline game engine and a driver for the online game based on Selenium

## Installation
### PIP Packages and Virtualenv
To run the code you first need to install the necessary packages using pip. Ideally, you first set up a virtual enviroment
```
python3 -m venv venv
```
then you source it
```
. venv/bin/activate
```
Now you can easily install all necessary packages using the requirements.txt file
```
pip install -r requirements.txt
```
### Gecko Driver and Selenium
The online bot is currently not working, due to a bug in either Firefox or Selenium... 

### Running Tests
To check if the installation was successful you can simply run all the unittests using pytest from the project root
```
pytest
```

## Usage
All the bot were written in an object-orientated fashion. Testing one bot is as simple as plugging it into the src/main.py file and running the experiment with the desired number of iterations and cores with

```
python src/main.py
```

## Algorithms
Following is a short description for all algorithms used in this project. If not stated otherwise the informations were taken from Chapter 8 of the book ["Reinforcement Learning - An Introduction"](https://drive.google.com/file/d/1opPSz5AZ_kVa1uWOdOiveNiBFiEOHjkG/view) by Sutton and Barto.

### Planning Algorithms

#### Heuristic Search Bot

#### Rollout Bot

### Learning Algorithms
#### Deep Neuro Evolution

## Results
### Planning Algorithms
The table shows some results for the various bots with different settings of the hyperparameter. The meaning of the hyperparameter for the different bots are:
- Rollout Bot: Number of rollout per action
- Heuristic Search Bot: Depth of the search tree
- Monte-Carlo Tree Search: Total number of rollouts

The bots theirselves only use one core, but the evaluation function uses more cores. For the timing an AMD CPU with 4 cores was used. The number of cores was considered in the computation of the average time, so the average time gives the time a single episode needs to terminate with one core.

It is important to note, that the times of the runs with higher hyperparameters take much longer. This has two reasons. First, the computation of the next move is more demanding with a deeper tree or more rollouts. Second, the time the game 2048 needs to terminate is not fixed. It highly depends on the skill of the player (or bot in this scenario). So the better the bot, the longer it can play the game.

Algorithm | Score | Execution Time (sec)
------------ | ------------- | -------------
Random | 1116 | 0.05
Rollout(1, Random) | 5252 | 31
Rollout(2, Random) | 7060 | 73
Rollout(5, Random)* | 11928 | 292
Rollout(10, Random)* | 17227 | 646
Rollout(20, Random)* | 32569 | 1949
Rollout(50, Random)* | 36303 | 6060
Rollout(1, HeuristicSearch(1)) | 5617 | 136
Rollout(2, HeuristicSearch(1)) | 8252 | 410
Rollout(5, HeuristicSearch(1)) |10882 | 1047
HeuristicSearch(1) | 2104 | 0.19
HeuristicSearch(2) | 7771 | 15
HeuristicSearch(3)* | 9209 | 1157


### Learning Algorithms
Here is a section about the learning algorithms.

Algorithm | Average Score | Training Time (sec)
----------- | --------------- | ----------------
DeepNeuroEvolution ||
Asynchronous Q-Learning ||
Deep Q-Network ||

## License
This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details
