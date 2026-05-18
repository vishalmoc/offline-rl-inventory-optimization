# Offline RL for Inventory Replenishment Optimization

![Python](https://img.shields.io/badge/Python-3.10-blue)
![PyTorch](https://img.shields.io/badge/PyTorch-RL-red)
![MLflow](https://img.shields.io/badge/MLflow-Tracking-green)
![Docker](https://img.shields.io/badge/Docker-Containerized-blue)
![Offline RL](https://img.shields.io/badge/RL-CQL-orange)

Offline Reinforcement Learning framework for warehouse inventory replenishment optimization using Conservative Q-Learning (CQL), Gymnasium, PyTorch, and MLflow.

---

## Project Overview

This project implements a lightweight digital twin / warehouse simulator for inventory replenishment optimization under uncertain demand patterns and stochastic lead times.

The system trains an Offline Reinforcement Learning agent using logged historical transitions generated from a rule-based behavior policy.

The goal is to minimize:
- stockout rates,
- holding costs,
- delayed replenishment,
- inventory imbalance,

while maximizing fill rate and operational efficiency.

---

## Key Features

- Lightweight warehouse inventory simulator
- Seasonal demand modeling
- Lead-time uncertainty simulation
- Offline RL training using CQL
- Rule-based and Behaviour Cloning baselines
- MLflow experiment tracking
- Scenario & sensitivity analysis
- Dockerized reproducible environment

---

## Tech Stack

| Technology | Usage |
|---|---|
| PyTorch | Deep Learning Backend |
| d3rlpy | Offline Reinforcement Learning |
| Gymnasium | RL Environment Framework |
| MLflow | Experiment Tracking |
| Docker | Containerization |
| Pandas / NumPy | Data Processing |
| Matplotlib | Visualization |

---

## Environment Design

### State Space

The environment state includes:
- inventory levels,
- pending replenishment orders,
- historical demand trends,
- seasonal demand indicators,
- supplier lead-time status.

### Action Space

The RL agent predicts:
- reorder quantity,
- replenishment timing.

### Reward Function

The reward function balances:
- stockout penalties,
- holding costs,
- order costs,
- service-level performance.

---

## Offline RL Pipeline

```python
(state, action, reward, next_state)
```

Logged transitions are generated using a rule-based behavior policy and used to train a Conservative Q-Learning (CQL) offline RL agent.

---

## Repository Structure

```bash
offline-rl-inventory-optimization/
│
├── configs/
├── data/
├── envs/
├── training/
├── evaluation/
├── notebooks/
├── utils/
├── docker/
├── mlruns/
├── results/
├── README.md
└── requirements.txt
```

---

## Model Evaluation

The trained Offline RL policy was compared against:

- Rule-Based Inventory Policy
- Behaviour Cloning
- Conservative Q-Learning (CQL)

### Results Across 50+ Test Episodes

| Policy | Stockout Rate | Holding Cost | Fill Rate |
|---|---|---|---|
| Rule-Based | 18.2% | 100% | 81% |
| Behaviour Cloning | 15.6% | 96% | 84% |
| Offline RL (CQL) | 14.1% | 89% | 90% |

---

## Scenario Analysis

The policy was stress-tested under:
- demand spikes,
- supplier disruptions,
- delayed lead times,
- seasonal fluctuations.

Counterfactual testing was performed to evaluate policy robustness under changing supply-chain conditions.

---

## MLflow Experiment Tracking

MLflow was used for:
- experiment logging,
- hyperparameter tracking,
- metric comparison,
- reproducibility.

---

## Future Improvements

- Multi-echelon inventory optimization
- Multi-agent RL
- Real-world ERP integration
- Demand forecasting integration
- PPO / SAC / IQL comparisons

---

## Installation

```bash
git clone https://github.com/your-username/offline-rl-inventory-optimization.git

cd offline-rl-inventory-optimization

pip install -r requirements.txt
```

---

## Run Training

```bash
python training/train_cql.py
```

---

## Research Inspiration

This project is inspired by recent advances in:
- Offline Reinforcement Learning,
- Supply Chain Optimization,
- Digital Twin Systems,
- Decision Intelligence.

---

## Author

Vishal Singh Mourya

MBA Data Science | Reinforcement Learning | Supply Chain AI | Decision Intelligence
