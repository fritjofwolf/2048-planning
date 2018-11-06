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

## Algorithms
Following is a short description for all algorithms used in this project

### Random Bot

### Heuristic Search Bot

### Rollout Bot

### Monte-Carlo Tree Search Bot

## Results
Algorithm | Average Score | Average Time
------------ | ------------- | -------------
Random | 1116 | 1 sec
Rollout(1) | |
Rollout(10) | |
Rollout(25) | |
Rollout(50) | |
HeuristicSearch(1) | |
HeuristicSearch(2) | |
HeuristicSearch(3) | |
MCTS(1) | |
MCTS(10) | |
MCTS(100) | |


## License
This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details
