import torch
import torch.nn as nn
import torch.optim as optim
import numpy as np
import random
from replay_buffer import ReplayBuffer

class UDAE(nn.Module):
    def __init__(self, state_dim, action_dim, num_ensemble=5, buffer_size=10000):
        """
        UDAE model with DQN ensemble for uncertainty-driven exploration.
        Args:
            state_dim (int): Dimension of the state space.
            action_dim (int): Dimension of the action space.
            num_ensemble (int): Number of DQN models in the ensemble.
            buffer_size (int): Size of the replay buffer.
        """
        super(UDAE, self).__init__()
        self.state_dim = state_dim
        self.action_dim = action_dim
        self.num_ensemble = num_ensemble
        self.models = nn.ModuleList([self.build_model() for _ in range(num_ensemble)])
        self.optimizers = [optim.Adam(model.parameters(), lr=1e-3) for model in self.models]
        self.replay_buffer = ReplayBuffer(buffer_size)
        self.gamma = 0.5  # Discount factor (from paper: 0.3 to 0.7)
        self.epsilon_start = 0.5
        self.epsilon_end = 0.05
        self.epsilon_decay = 1000
        self.step_count = 0

    def build_model(self):
        return nn.Sequential(
            nn.Linear(self.state_dim, 128),
            nn.ReLU(),
            nn.Linear(128, 128),
            nn.ReLU(),
            nn.Linear(128, self.action_dim)
        )

    def forward(self, state):
        q_values = [model(state) for model in self.models]
        return torch.stack(q_values)  # Shape: (num_ensemble, batch_size, action_dim)

    def get_action(self, state, use_uncertainty=True):
        """
        Selects an action using epsilon-greedy with uncertainty-driven exploration.
        Args:
            state (np.array): Current state.
            use_uncertainty (bool): Whether to use uncertainty for exploration.
        Returns:
            int: Selected action.
        """
        self.step_count += 1
        epsilon = self.epsilon_end + (self.epsilon_start - self.epsilon_end) * np.exp(-self.step_count / self.epsilon_decay)

        if random.random() < epsilon:
            return random.randint(0, self.action_dim - 1)

        state = torch.FloatTensor(state).unsqueeze(0)
        q_values = self.forward(state)
        q_mean = q_values.mean(dim=0)  # Average Q-values across ensemble

        if use_uncertainty:
            q_variance = q_values.var(dim=0)  # Variance across ensemble
            beta = 0.15  # Exploration scaling factor (from paper: 0.05 to 0.2)
            exploration_bonus = beta * q_variance
            q_mean += exploration_bonus

        return q_mean.argmax().item()

    def train(self, batch_size=64):
        """
        Trains the DQN ensemble using a batch from the replay buffer.
        Args:
            batch_size (int): Size of the training batch.
        """
        if len(self.replay_buffer) < batch_size:
            return

        states, actions, rewards, next_states, dones = self.replay_buffer.sample(batch_size)
        states = torch.FloatTensor(states)
        actions = torch.LongTensor(actions)
        rewards = torch.FloatTensor(rewards)
        next_states = torch.FloatTensor(next_states)
        dones = torch.FloatTensor(dones)

        for model, optimizer in zip(self.models, self.optimizers):
            optimizer.zero_grad()
            q_values = model(states).gather(1, actions.unsqueeze(1)).squeeze(1)
            next_q_values = model(next_states).max(1)[0].detach()
            targets = rewards + (1 - dones) * self.gamma * next_q_values
            loss = nn.MSELoss()(q_values, targets)
            loss.backward()
            optimizer.step()

    def add_experience(self, state, action, reward, next_state, done):
        """Adds an experience to the replay buffer."""
        self.replay_buffer.add(state, action, reward, next_state, done)

if __name__ == '__main__':
    model = UDAE(state_dim=3, action_dim=4)
    state = np.random.rand(3)
    action = model.get_action(state)
    print(f"Selected action: {action}")
    model.add_experience(state, action, 1.0, np.random.rand(3), False)
    model.train()
