import carla
import numpy as np
import random

class CarlaEnvironment:
    def __init__(self, world, target_speed=10.0):
        """
        Initializes the CARLA environment.
        Args:
            world (carla.World): The CARLA world.
            target_speed (float): Target speed for the vehicle (m/s).
        """
        self.world = world
        self.target_speed = target_speed
        self.vehicle = None
        self.collision_sensor = None
        self.spawn_vehicle()
        self.setup_sensors()
        self.collision_history = []

    def spawn_vehicle(self):
        """Spawns a vehicle in the CARLA world."""
        blueprint_library = self.world.get_blueprint_library()
        vehicle_bp = blueprint_library.filter('vehicle.tesla.model3')[0]
        spawn_points = self.world.get_map().get_spawn_points()
        spawn_point = random.choice(spawn_points)
        self.vehicle = self.world.spawn_actor(vehicle_bp, spawn_point)
        self.vehicle.set_autopilot(True)  # Enable CARLA's autopilot for simplicity

    def setup_sensors(self):
        """Sets up a collision sensor on the vehicle."""
        blueprint_library = self.world.get_blueprint_library()
        collision_bp = blueprint_library.find('sensor.other.collision')
        self.collision_sensor = self.world.spawn_actor(
            collision_bp, carla.Transform(), attach_to=self.vehicle
        )
        self.collision_sensor.listen(lambda event: self.collision_history.append(event))

    def reset(self):
        """Resets the environment."""
        if self.vehicle:
            self.vehicle.destroy()
        if self.collision_sensor:
            self.collision_sensor.destroy()
        self.collision_history = []
        self.spawn_vehicle()
        self.setup_sensors()
        self.world.tick()
        return self.get_state()

    def get_state(self):
        """Returns the current state of the vehicle."""
        location = self.vehicle.get_location()
        velocity = self.vehicle.get_velocity()
        speed = np.sqrt(velocity.x**2 + velocity.y**2 + velocity.z**2)
        return np.array([location.x, location.y, speed])

    def compute_reward(self, state):
        """
        Computes the reward based on safety, efficiency, and progress.
        Args:
            state (np.array): Current state [x, y, speed].
        Returns:
            float: Reward value.
        """
        reward = 0.0
        # Safety: Penalize collisions
        if self.collision_history:
            reward -= 5.0
        # Efficiency: Reward maintaining target speed
        speed = state[2]
        if abs(speed - self.target_speed) <= 0.05 * self.target_speed:
            reward += 0.5
        # Progress: Reward movement (simplified)
        reward += 0.1
        return reward

    def step(self, action):
        """
        Takes an action and steps the environment.
        Args:
            action (int): Action to take (simplified: 0=brake, 1=accelerate).
        Returns:
            tuple: (next_state, reward, done)
        """
        if action == 0:  # Brake
            self.vehicle.apply_control(carla.VehicleControl(throttle=0.0, brake=1.0))
        else:  # Accelerate
            self.vehicle.apply_control(carla.VehicleControl(throttle=0.5, brake=0.0))
        
        self.world.tick()
        next_state = self.get_state()
        reward = self.compute_reward(next_state)
        done = len(self.collision_history) > 0  # End episode on collision
        return next_state, reward, done

if __name__ == '__main__':
    from setup_simulation import setup_carla_simulation, cleanup_actors
    world = setup_carla_simulation()
    env = CarlaEnvironment(world)
    state = env.reset()
    print(f"Initial state: {state}")
    action = 1  # Accelerate
    next_state, reward, done = env.step(action)
    print(f"Next state: {next_state}, Reward: {reward}, Done: {done}")
    cleanup_actors(world)
