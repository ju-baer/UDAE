import carla
import torch
import logging
from carla_scripts.setup_simulation import setup_carla_simulation, cleanup_actors
from carla_scripts.environment import CarlaEnvironment
from dqn_ensemble.uda_model import UDAE

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

def run_urban_navigation():
    try:
        world = setup_carla_simulation()
        env = CarlaEnvironment(world)
        model = UDAE(state_dim=3, action_dim=4)

        # Load pre-trained model if available
        try:
            model.load_state_dict(torch.load('../models/uda_model.pth'))
            logger.info("Loaded pre-trained model.")
        except FileNotFoundError:
            logger.warning("No pre-trained model found. Using untrained model.")

        state = env.reset()
        for t in range(1000):
            action = model.get_action(state, epsilon=0.1)
            state, reward, done = env.step(action)
            logger.info(f"Timestep {t}, State: {state}, Action: {action}, Reward: {reward}")
            if done:
                logger.info("Episode ended early due to collision.")
                break
    except Exception as e:
        logger.error(f"Error during urban navigation: {e}")
        raise
    finally:
        cleanup_actors(world)

if __name__ == '__main__':
    run_urban_navigation()
