import numpy as np
import math
import gym
from gym import spaces, logger
from gym.utils import seeding

class StoreHouse(gym.Env):
    """
        Storehouse environment.
        Description:
            The robot controls the work of the warehouse, loading and unloading boxes.
            The goal is to fill the warehouse as much as possible without losing the ability to unload boxes.

        Observation:
            Type: Box(4)
            Num	Observation                 Min         Max
            0	Cart Position             -4.8            4.8
            1	Cart Velocity             -Inf            Inf
            2	Pole Angle                 -24 deg        24 deg
            3	Pole Velocity At Tip      -Inf            Inf

        Actions:
            Type: Discrete(2)
            Num	Action
            0	Lift the box.
            1	Put the box.
        """
    def __init__(self):
        self.length = 10
        self.width = 10
        size = 10

        # Define what the agent can do
        self.action_space = spaces.Discrete(2)
        self.observation_space = spaces.box(-size, size, dtype=np.float32)

        # Store what the agent tried
        self.curr_episode = -1
        self.action_episode_memory = []

        # Init storehouse
        self.state = np.zeros((size, size, size), dtype=int)