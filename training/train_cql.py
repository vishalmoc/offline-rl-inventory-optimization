from d3rlpy.algos import CQLConfig
from d3rlpy.dataset import MDPDataset
import numpy as np

print("Starting CQL training pipeline...")

observations = np.random.rand(1000, 4)
actions = np.random.randint(0, 100, size=(1000, 1))
rewards = np.random.rand(1000)
terminals = np.random.randint(0, 2, size=(1000,))

dataset = MDPDataset(
    observations=observations,
    actions=actions,
    rewards=rewards,
    terminals=terminals
)

cql = CQLConfig().create()

cql.fit(
    dataset,
    n_steps=10000
)

print("Training completed.")
