import numpy as np
import random

class ReplayBuffer:
    def __init__(self, capacity):
        """
        A replay buffer for storing experiences.
        Args:
            capacity (int): Maximum number of experiences to store.
        """
        self.capacity = capacity
        self.buffer = []
        self.position = 0

    def add(self, state, action, reward, next_state, done):
        """Adds an experience to the buffer."""
        experience = (state, action, reward, next_state, done)
        if len(self.buffer) < self.capacity:
            self.buffer.append(experience)
        else:
            self.buffer[self.position] = experience
        self.position = (self.position + 1) % self.capacity

    def sample(self, batch_size):
        """
        Samples a batch of experiences.
        Args:
            batch_size (int): Number of experiences to sample.
        Returns:
            tuple: (states, actions, rewards, next_states, dones)
        """
        batch = random.sample(self.buffer, batch_size)
        states, actions, rewards, next_states, dones = zip(*batch)
        return np.array(states), np.array(actions), np.array(rewards), np.array(next_states), np.array(dones)

    def __len__(self):
        return len(self.buffer)

if __name__ == '__main__':
    buffer = ReplayBuffer(capacity=1000)
    buffer.add([1, 2, 3], 0, 1.0, [4, 5, 6], False)
    states, actions, rewards, next_states, dones = buffer.sample(1)
    print(f"Sampled experience: {states}, {actions}, {rewards}, {next_states}, {dones}")
