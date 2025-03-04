# agent/dqn_agent.py

"""
This module implements the Deep Q-Network (DQN) agent.
It defines the neural network architecture used to approximate Q-values for each action.
Key functionalities include:
  - Selecting actions using an epsilon-greedy strategy.
  - Updating the network based on experiences sampled from replay memory.
  - Integrating with the training loop to learn from the game environment.
This module is used directly by the main training loop in main.py.
"""
