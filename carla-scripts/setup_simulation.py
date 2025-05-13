import carla
import random
import time
import logging

# Set up logging for better debugging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

def setup_carla_simulation(world_name='Town03', max_retries=3):
    """
    Sets up the CARLA simulation with retries for connection issues.
    Args:
        world_name (str): Name of the CARLA world to load (default: Town03).
        max_retries (int): Maximum number of retries for connecting to the server.
    Returns:
        carla.World: The loaded CARLA world.
    """
    attempt = 0
    client = None
    while attempt < max_retries:
        try:
            client = carla.Client('localhost', 2000)
            client.set_timeout(10.0)
            world = client.load_world(world_name)
            logger.info(f"Loaded CARLA world: {world.get_map().name}")

            # Set synchronous mode
            settings = world.get_settings()
            settings.synchronous_mode = True
            settings.fixed_delta_seconds = 0.05
            world.apply_settings(settings)

            # Set up spectator camera
            spectator = world.get_spectator()
            spectator_transform = carla.Transform(carla.Location(x=0, y=0, z=50), carla.Rotation(pitch=-90))
            spectator.set_transform(spectator_transform)

            return world
        except Exception as e:
            logger.error(f"Failed to connect to CARLA server (attempt {attempt + 1}/{max_retries}): {e}")
            attempt += 1
            time.sleep(2)
    raise RuntimeError(f"Could not connect to CARLA server after {max_retries} attempts.")

def cleanup_actors(world):
    """
    Cleans up all actors in the CARLA world.
    Args:
        world (carla.World): The CARLA world to clean up.
    """
    try:
        actors = world.get_actors()
        for actor in actors:
            if actor.type_id.startswith('vehicle') or actor.type_id.startswith('walker'):
                actor.destroy()
        logger.info("Cleaned up all actors in the CARLA world.")
    except Exception as e:
        logger.error(f"Error during cleanup: {e}")

if __name__ == '__main__':
    world = setup_carla_simulation()
    try:
        time.sleep(5)  # Run for 5 seconds to observe the world
    finally:
        cleanup_actors(world)
