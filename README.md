# UDAE: Adaptive Uncertainty-Driven Reinforcement Learning for Safe and Efficient Autonomous Driving


## Setup
1. Install CARLA (version 0.9.13): [https://carla.readthedocs.io/en/latest/start_quickstart/](https://carla.readthedocs.io/en/latest/start_quickstart/)
2. Install Python dependencies: `pip install -r requirements.txt`
3. Configure CARLA settings as described in the `data/` folder.

## Running Tests
- Urban navigation task: `python test_setups/urban_navigation.py`
- Emergency avoidance scenario: `python test_setups/emergency_avoidance.py`
- Train UDAE: `python train_uda.py`
  - Outputs a trained model at `uda_model.pth`.

## Code Structure
- `carla_scripts/`: Scripts to set up CARLA environments.
- `dqn_ensemble/`: UDAE implementation with DQN ensemble.
- `test_setups/`: Scripts to replicate experiments.
- `data_generation/`: Scripts to generate sample datasets.

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
