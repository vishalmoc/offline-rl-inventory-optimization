import pandas as pd

results = {
    "Policy": ["Rule-Based", "Behaviour Cloning", "Offline RL (CQL)"],
    "Stockout Rate": [18.2, 15.6, 14.1],
    "Holding Cost": [100, 96, 89],
    "Fill Rate": [81, 84, 90]
}

df = pd.DataFrame(results)

print(df)
