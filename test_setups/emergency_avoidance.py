import carla
from carla_scripts.setup_simulation import setup_carla_simulation
from carla_scripts.environment import CarlaEnvironment
from dqn_ensemble.uda_model import UDAE

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
        print(f"Timestep {t}, State: {state}, Action: {action}")

if __name__ == '__main__':
    run_emergency_avoidance()
