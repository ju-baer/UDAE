import carla
import numpy as np

class CarlaEnvironment:
    def __init__(self, world):
        self.world = world
        self.vehicle = None
        self.spawn_vehicle()

    def spawn_vehicle(self):
        blueprint_library = self.world.get_blueprint_library()
        vehicle_bp = blueprint_library.filter('vehicle.tesla.model3')[0]
        spawn_point = random.choice(self.world.get_map().get_spawn_points())
        self.vehicle = self.world.spawn_actor(vehicle_bp, spawn_point)

    def reset(self):
        if self.vehicle:
            self.vehicle.destroy()
        self.spawn_vehicle()
        return self.get_state()

    def get_state(self):
        location = self.vehicle.get_location()
        return np.array([location.x, location.y, location.z])

if __name__ == '__main__':
    world = setup_carla_simulation()
    env = CarlaEnvironment(world)
    print(f"Initial state: {env.reset()}")
