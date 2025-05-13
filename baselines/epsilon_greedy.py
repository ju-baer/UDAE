import numpy as np
import csv
from carla_scripts.environment import CarlaEnvironment

class EpsilonGreedy:
    def __init__(self, action_dim, epsilon_start=0.5, epsilon_end=0.05, decay_steps=1000):
        self.action_dim = action_dim
        self.epsilon_start = epsilon_start
        self.epsilon_end = epsilon_end
        self.decay_steps = decay_steps
        self.step = 0

    def get_action(self, state):
        self.step += 1
        epsilon = self.epsilon_end + (self.epsilon_start - self.epsilon_end) * (1 - min(self.step / self.decay_steps, 1))
        if np.random.rand() < epsilon:
            return np.random.randint(self.action_dim)
        return 1

def run_epsilon_greedy():
    from carla_scripts.setup_simulation import setup_carla_simulation, cleanup_actors
    world = setup_carla_simulation()
    env = CarlaEnvironment(world)
    agent = EpsilonGreedy(action_dim=4)

    state = env.reset()
    data = []
    for t in range(1000):
        action = agent.get_action(state)
        next_state, reward, done = env.step(action)
        data.append([t, next_state[0], next_state[1], action, reward, 0.0])  # Uncertainty not used
        state = next_state
        print(f"Timestep {t}, Action: {action}, Reward: {reward}")
        if done:
            break

    # Save log
    with open('../data/sample_data/epsilon_greedy_log.csv', 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['timestep', 'x_position', 'y_position', 'action', 'reward', 'uncertainty'])
        writer.writerows(data)

    cleanup_actors(world)

if __name__ == '__main__':
    run_epsilon_greedy()
