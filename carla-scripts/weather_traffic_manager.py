import carla
import json
import os

class WeatherTrafficManager:
    def __init__(self, world):
        """
        Manages weather and traffic settings in CARLA.
        Args:
            world (carla.World): The CARLA world.
        """
        self.world = world
        self.data_dir = "../data/carla_settings/"

    def load_settings(self, traffic_file, weather_file):
        """
        Loads traffic and weather settings from JSON files.
        Args:
            traffic_file (str): Path to traffic settings JSON.
            weather_file (str): Path to weather settings JSON.
        """
        # Load traffic settings
        with open(os.path.join(self.data_dir, traffic_file), 'r') as f:
            traffic_settings = json.load(f)
        self.set_traffic(traffic_settings)

        # Load weather settings
        with open(os.path.join(self.data_dir, weather_file), 'r') as f:
            weather_settings = json.load(f)
        self.set_weather(weather_settings)

    def set_traffic(self, settings):
        """Sets traffic density and spawns vehicles/pedestrians."""
        traffic_manager = self.world.get_traffic_manager()
        traffic_manager.set_global_distance_to_leading_vehicle(2.0)
        traffic_manager.set_random_device_seed(42)

        # Spawn vehicles
        num_vehicles = settings.get('num_vehicles', 20)
        blueprint_library = self.world.get_blueprint_library()
        vehicle_bps = blueprint_library.filter('vehicle.*')
        spawn_points = self.world.get_map().get_spawn_points()
        for i in range(num_vehicles):
            if i < len(spawn_points):
                bp = random.choice(vehicle_bps)
                self.world.try_spawn_actor(bp, spawn_points[i])

        # Spawn pedestrians (simplified)
        num_pedestrians = settings.get('num_pedestrians', 5)
        pedestrian_bps = blueprint_library.filter('walker.pedestrian.*')
        for _ in range(num_pedestrians):
            location = carla.Location(x=random.uniform(-50, 50), y=random.uniform(-50, 50), z=0.5)
            bp = random.choice(pedestrian_bps)
            self.world.try_spawn_actor(bp, carla.Transform(location))

    def set_weather(self, settings):
        """Sets weather conditions."""
        weather = carla.WeatherParameters(
            cloudiness=10.0 if settings['weather'].startswith('Clear') else 80.0,
            precipitation=settings['precipitation'],
            fog_density=settings['fog_density'],
            sun_altitude_angle=70.0 if 'Noon' in settings['weather'] else 10.0
        )
        self.world.set_weather(weather)

if __name__ == '__main__':
    from setup_simulation import setup_carla_simulation, cleanup_actors
    world = setup_carla_simulation()
    manager = WeatherTrafficManager(world)
    manager.load_settings('traffic_low.json', 'weather_clear.json')
    world.tick()
    print("Weather and traffic settings applied.")
    cleanup_actors(world)
