import mlflow


def start_experiment(name="inventory_rl"):
    mlflow.set_experiment(name)
