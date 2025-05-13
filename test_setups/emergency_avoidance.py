import carla
from carla_scripts.setup_simulation import setup_carla_simulation
from carla_scripts.environment import CarlaEnvironment
from dqn_ensemble.uda_model import UDAE

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

def run_emergency_avoidance():
    world = setup_carla_simulation()
    env = CarlaEnvironment(world)
    model = UDAE(state_dim=3, action_dim=4)
    state = env.reset()
    for t in range(450, 551):
        if t == 500:  # Simulate pedestrian crossing
            print("Pedestrian crossing detected!")
        action = model.get_action(state, epsilon=0.1)
        state = env.get_state()
         logger.info(f"Timestep {t}, State: {state}, Action: {action}, Reward: {reward}")
            if done:
                logger.info("Episode ended early due to collision.")
                break
    except Exception as e:
        logger.error(f"Error during emergency avoidance: {e}")
        raise
    finally:
        cleanup_actors(world)

if __name__ == '__main__':
    run_emergency_avoidance()
