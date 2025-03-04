# agent/replay_memory.py

"""
This module implements the Replay Memory class for experience replay.
It stores the agent’s experiences as tuples (state, action, reward, next_state, done) and
provides functionality to sample mini-batches for training.
This approach helps stabilize learning by breaking correlations between consecutive samples.
It is used by the DQN agent (in dqn_agent.py) during the training process.
"""
