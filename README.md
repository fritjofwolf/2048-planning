# 2048-planning
Decision-time planning algorithms for the game 2048 (https://play2048.co/)

<div style="text-align:center">
    <img src="https://github.com/fritjofwolf/2048-planning/blob/master/media/sample_game.gif" width="400" height="400"/>
</div>

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
In order to interact with the 2048 online version, you first need to download the geckodriver. You can find the latest releases for different operating systems [here](https://github.com/mozilla/geckodriver/releases). Then you need to add the folder where the geckodriver was downloaded to your path. On Unix systems that can be done via:
```
export PATH=$PATH:/path/to/directory/of/executable/downloaded/in/previous/step
``` 
Last you have to make sure to set the n_processors in the main-script to one. Otherwise all processes will interact with the same version of the 2048 webpage.

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
Following is a short description for all algorithms used in this project. There are two main groups of algorithms used in this project. First, there are decision-time planning algorithms that do not learn a value function, but instead use a model to search the state-space. Second, there are Reinforcement Learning Algorithms that first have to learn a policy or a value function to play the game. 

### Planning Algorithms
The planning algorithms considered here are decision-time algorithms. Since they do not compute any value function or policy in advance they can be used without any pretraining, but are also not able to learn anything from the past experience and there computational cost at runtime is quite high. 
The information about the following algorithms were taken from Chapter 8 of the book ["Reinforcement Learning - An Introduction"](https://drive.google.com/file/d/1opPSz5AZ_kVa1uWOdOiveNiBFiEOHjkG/view) by Sutton and Barto.

#### Heuristic Search Bot
This is basically the classic brute-force tree search. Given a current state the algorithm computes the reward it gets for taking the different actions. The depth of the search is only hyperparameter. For a depth of one this is just the greedy algorithm which chooses the action which maximizes the immediate reward. For larger depth sizes the exact reward cannot be computed due to the stochasticity of the enviroment. Several strategies can be deployed to handle this problem. We simply compute the expected value over all possible new states, i.e. all possible states with a 2 or 4 tile added, using their respective probabilities. Due to this large branch factor the search becomes infeasible with depth more than 3. It is worth noting that this algorithm does not use a evaluation function at the leaf nodes of the search tree as often seen e.g. in classical chess programs, but instead only uses the reward that is generated along the way through the tree, which is not present in games like chess or go.

#### Rollout Bot
First investigated in the end of the nineties for the game of backgammon, rollout algorithms (and there extension in form of Monte Carlo Tree Search) are now one of the state-of-the-art algorithms used for example in the AlphaZero program by DeepMind. The basic idea is quite simple. For each state a number of trajectories is sampled that run to the end of the game. By backing up the achieved scores we get a value for each action in the current state. Then the action with the highest value can be selected. Since the game is run until the end there is no need for an evaluation function. The rollout policy that is used to compute the actions for the rollout trajectories can be any policy. Evidence suggests that even the random policy and a low number of samples can produce quite good results.

### Learning Algorithms
Reinforcement Learning uses value functions to learn the values (or action-values) of states and actions. Using these value functions good policies can be found. The algorithms presented here all use a neural network to represent the value function (or in some cases the policy directly). This network needs to be trained in advanced which can be quite time-consuming, but once the network is trained the actions for a new state can be selected very fast.

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
