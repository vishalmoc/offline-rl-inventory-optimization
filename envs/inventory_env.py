import gymnasium as gym
from gymnasium import spaces
import numpy as np


class InventoryEnv(gym.Env):
    def __init__(self):
        super().__init__()

        self.max_inventory = 500
        self.inventory = 200
        self.day = 0
        self.max_steps = 365

        self.action_space = spaces.Discrete(100)

        self.observation_space = spaces.Box(
            low=0,
            high=500,
            shape=(4,),
            dtype=np.float32
        )

    def reset(self, seed=None, options=None):
        self.inventory = 200
        self.day = 0

        state = np.array([
            self.inventory,
            0,
            1,
            self.day
        ], dtype=np.float32)

        return state, {}

    def step(self, action):
        demand = np.random.randint(20, 80)

        self.inventory += action
        sales = min(self.inventory, demand)

        self.inventory -= sales

        stockout_penalty = max(0, demand - sales) * 10
        holding_cost = self.inventory * 0.5

        reward = sales - holding_cost - stockout_penalty

        self.day += 1

        done = self.day >= self.max_steps

        next_state = np.array([
            self.inventory,
            demand,
            sales,
            self.day
        ], dtype=np.float32)

        return next_state, reward, done, False, {}
