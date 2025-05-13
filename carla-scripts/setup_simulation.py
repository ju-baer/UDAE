import carla
import random

def setup_carla_simulation(world_name='Town03'):
    client = carla.Client('localhost', 2000)
    client.set_timeout(10.0)
    world = client.load_world(world_name)
    settings = world.get_settings()
    settings.synchronous_mode = True
    settings.fixed_delta_seconds = 0.05
    world.apply_settings(settings)
    return world

if __name__ == '__main__':
    world = setup_carla_simulation()
    print(f"Loaded CARLA world: {world.get_map().name}")
