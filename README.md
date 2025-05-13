# UDAE: Adaptive Uncertainty-Driven Reinforcement Learning for Safe and Efficient Autonomous Driving

## Setup
1. Install CARLA (version 0.9.13): [https://carla.readthedocs.io/en/latest/start_quickstart/](https://carla.readthedocs.io/en/latest/start_quickstart/)
2. Install Python dependencies: `pip install -r requirements.txt`
3. Configure CARLA settings as described in the `data/` folder.

## Running Tests
- Urban navigation task: `python test_setups/urban_navigation.py`
- Emergency avoidance scenario: `python test_setups/emergency_avoidance.py`

## Code Structure
- `carla_scripts/`: Scripts to set up CARLA environments.
- `dqn_ensemble/`: UDAE implementation with DQN ensemble.
- `test_setups/`: Scripts to replicate experiments.
