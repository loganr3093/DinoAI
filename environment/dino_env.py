# environment/dino_env.py

"""
This module defines the custom game environment for Chrome's Dinosaur Game.
Key responsibilities include:
  - Capturing the game state (e.g., via screenshots or extracted features).
  - Simulating key presses (jump, duck, or do nothing) using tools like PyAutoGUI.
  - Calculating rewards based on the agent's performance (e.g., time survived or score).
  - Resetting the game when an episode ends.
It is designed similarly to an OpenAI Gym environment, making it easy to integrate with the DQN agent.
"""
