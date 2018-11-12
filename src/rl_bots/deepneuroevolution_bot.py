import numpy as np
from sklearn.neural_network import MLPRegressor
import sklearn
from itertools import repeat
import warnings
warnings.filterwarnings("ignore")
from multiprocessing import Pool


class DeepNeuroevolution():
    
    def __init__(self, env, n_individuals, n_parents, n_features, n_actions, nn_architecture, reward_goal):
        self._env = env
        self._n_individuals = n_individuals
        self._n_parents = n_parents
        self._n_features = n_features
        self._n_actions = n_actions
        self._nn_architecture = nn_architecture
        self._reward_goal = reward_goal
        self._best_score = -10**10
        self._n_generations = 0
    
    
    def find_optimal_network(self):
        self._create_first_population()
        while not self._is_finished():
            self._evaluate_population()
            parents = self._create_parents()
            self._create_new_population(parents)
            self._print_score(parents)
            
    
    def _is_finished(self):
        return self._best_score >= self._reward_goal
    
    
    def _evaluate_population(self):
        for idx, mlp in enumerate(self._current_population):
            score = self._evaluate_network(mlp[0], 10)
            self._current_population[idx][1] = score
    
    
    def _evaluate_network(self, mlp, iterations):
        score = 0
        env = self._env
        for _ in range(iterations):
            state = env.reset()
            done = False
            while not done:
                action = np.random.choice(self._n_actions, p=mlp.predict([state])[0])
                state, reward, done, info = env.step(action)
                score += reward
        return score / iterations
    
    
    def _create_first_population(self):
        self._current_population = []
        for _ in range(self._n_individuals):
            mlp = MLPRegressor(hidden_layer_sizes = (10,), alpha=10**-10, max_iter=1)
            mlp.fit([np.random.randn(self._n_features)], [np.random.randn(self._n_actions)])
            mlp.out_activation_ = 'softmax'
            self._current_population.append([mlp,0])
    
    
    def _create_parents(self):
        parents = sorted(self._current_population, key=lambda x: -x[1])[:self._n_parents]
        for idx, mlp in enumerate(parents):
            score = self._evaluate_network(mlp[0], 100)
            parents[idx][1] = score
        parents.sort(key=lambda x:-x[1])
        return parents
    
    
    def _create_new_population(self, parents):
        new_population = [parents[0]]
        for _ in range(self._n_individuals-1):
            idx = np.random.randint(len(parents))
            weights, biases = self._compute_new_weights(parents[idx][0])
            mlp = self._create_new_nn(weights, biases)
            new_population.append([mlp, 0])
        self._current_population = new_population
    
    
    def _create_new_nn(self, weights, biases):
        mlp = MLPRegressor(hidden_layer_sizes = (10,), alpha=10**-10, max_iter=1)
        mlp.fit([np.random.randn(self._n_features)], [np.random.randn(self._n_actions)])
        mlp.coefs_ = weights
        mlp.intercepts_ = biases
        mlp.out_activation_ = 'softmax'
        return mlp
    
    
    def _compute_new_weights(self, parent):
        weights = parent.coefs_
        biases = parent.intercepts_
        new_weights = []
        new_biases = []
        for weight in weights:
            shape = weight.shape
            new_weights.append(weight + 100*np.random.randn(shape[0], shape[1]))
        for bias in biases:
            new_biases.append(bias + 100*np.random.randn(bias.shape[0]))
        return new_weights, new_biases
    
        
    def _print_score(self, parents):
        self._best_score = max(self._best_score, parents[0][1])
        self._n_generations += 1
        print('Results for generation', self._n_generations, '\n')
        print('Overall best score is:', self._best_score)
        print('Best scores of the current population:')
        for i in parents:
            print(i[1])
        print('\n')