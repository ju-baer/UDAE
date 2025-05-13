# UDAE: Adaptive Uncertainty-Driven Reinforcement Learning for Safe and Efficient Autonomous Driving

Welcome to the frontier of autonomous driving research! This repository presents **UDAE**—an interesting approach that redefines safety and efficiency in reinforcement learning (RL) for self-driving vehicles. UDAE (Uncertainty-Driven Adaptive Exploration) introduces a novel paradigm by leveraging ensemble-based uncertainty estimation to guide exploration in RL, ensuring that autonomous agents not only navigate complex urban environments with precision but also prioritize safety in unpredictable scenarios.

What sets UDAE apart? Traditional RL methods often struggle with the trade-off between exploration and safety, especially in high-stakes domains like autonomous driving. UDAE tackles this challenge head-on by dynamically adapting its exploration strategy based on uncertainty. It also enables the agent to cautiously explore unfamiliar scenarios (e.g., sudden pedestrian crossings) while confidently exploiting known patterns (e.g., routine urban navigation).

## About This Repository

This repository contains the code, data, and pre-trained models for the project *"UDAE: Adaptive Uncertainty-Driven Reinforcement Learning for Safe and Efficient Autonomous Driving"*. 


## Setup
1. Install CARLA (version 0.9.13): [https://carla.readthedocs.io/en/latest/start_quickstart/](https://carla.readthedocs.io/en/latest/start_quickstart/)
2. Install Python dependencies: `pip install -r requirements.txt`
3. Configure CARLA settings as described in the `data/` folder.
4. Recommended Python version: 3.9.13

   
## Running Tests
- Urban navigation task: `python test_setups/urban_navigation.py`
- Emergency avoidance scenario: `python test_setups/emergency_avoidance.py`
- Train UDAE: `python train_uda.py`
  - Outputs a trained model at `uda_model.pth`.
- Run epsilon-greedy baseline: `python baselines/epsilon_greedy.py`
- Evaluate success rates: `python evaluation/evaluate_results.py`
  - Outputs success rates and a plot (`success_rates.pdf`).

## Code Structure
- `carla-scripts/`: Scripts to set up CARLA environments.
- `dqn_ensemble/`: UDAE implementation with DQN ensemble.
- `test_setups/`: Scripts to replicate experiments.
- `data_generation/`: Scripts to generate sample datasets.
- `baselines/`: Implementations of baseline methods.
- `evaluation/`: Scripts to evaluate results.


## Data
- `data/carla_settings/`: JSON files for CARLA traffic and weather configurations.
- `data/sample_data/`: Sample logs to run tests without CARLA (if desired).
  - `urban_navigation_log.csv`: 1000 timesteps from the urban navigation task.
  - `urban_navigation_large.csv`: 5000 timesteps for a longer urban navigation run.
  - `emergency_avoidance_log.csv`: 101 timesteps for a single emergency avoidance scenario.
  - `emergency_avoidance_multiple.csv`: 505 timesteps covering 5 emergency avoidance scenarios.

## Generating Data
You can generate or regenerate the sample datasets using the scripts in the `data_generation/` folder:
- `generate_urban_navigation_log.py`: Generates `urban_navigation_log.csv` (1000 timesteps).
  - Run: `python data_generation/generate_urban_navigation_log.py`
- `generate_urban_navigation_large.py`: Generates `urban_navigation_large.csv` (5000 timesteps).
  - Run: `python data_generation/generate_urban_navigation_large.py`
- `generate_emergency_avoidance_log.py`: Generates `emergency_avoidance_log.csv` (101 timesteps).
  - Run: `python data_generation/generate_emergency_avoidance_log.py`
- `generate_emergency_avoidance_multiple.py`: Generates `emergency_avoidance_multiple.csv` (5 scenarios, 505 timesteps).
  - Run: `python data_generation/generate_emergency_avoidance_multiple.py`
