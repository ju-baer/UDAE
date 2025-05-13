# UDAE: Adaptive Uncertainty-Driven Reinforcement Learning for Safe and Efficient Autonomous Driving

## Setup
1. Install CARLA (version 0.9.13): [https://carla.readthedocs.io/en/latest/start_quickstart/](https://carla.readthedocs.io/en/latest/start_quickstart/)
2. Install Python dependencies: `pip install -r requirements.txt`
3. Configure CARLA settings as described in the `data/` folder.

## Running Tests
- Urban navigation task: `python test_setups/urban_navigation.py`
- Emergency avoidance scenario: `python test_setups/emergency_avoidance.py`

## Code Structure
- `carla-scripts/`: Scripts to set up CARLA environments.
- `dqn_ensemble/`: UDAE implementation with DQN ensemble.
- `test_setups/`: Scripts to replicate experiments.


## Data
- `data/carla_settings/`: JSON files for CARLA traffic and weather configurations.
- `data/sample_data/`: Sample logs to run tests without CARLA (if desired).
- `urban_navigation_log.csv`: 1000 timesteps from the urban navigation task.
- `urban_navigation_large.csv`: 5000 timesteps for a longer urban navigation run.
- `emergency_avoidance_log.csv`: 101 timesteps for a single emergency avoidance scenario.
- `emergency_avoidance_multiple.csv`: 505 timesteps covering 5 emergency avoidance scenarios.
