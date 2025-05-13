import torch
import numpy as np
from carla_scripts.setup_simulation import setup_carla_simulation, cleanup_actors
from carla_scripts.environment import CarlaEnvironment
from dqn_ensemble.uda_model import UDAE

def train_uda(episodes=1000, save_path='uda_model.pth'):
    world = setup_carla_simulation()
    env = CarlaEnvironment(world)
    model = UDAE(state_dim=3, action_dim=4)

    for episode in range(episodes):
        state = env.reset()
        done = False
        episode_reward = 0
        while not done:
            action = model.get_action(state)
            next_state, reward, done = env.step(action)
            model.add_experience(state, action, reward, next_state, done)
            model.train()
            state = next_state
            episode_reward += reward
        print(f"Episode {episode + 1}/{episodes}, Reward: {episode_reward}")

    torch.save(model.state_dict(), save_path)
    print(f"Saved trained model to {save_path}")
    cleanup_actors(world)

if __name__ == '__main__':
    train_uda()
