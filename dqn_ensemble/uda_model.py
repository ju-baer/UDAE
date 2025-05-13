import torch
import torch.nn as nn
import numpy as np

class UDAE(nn.Module):
    def __init__(self, state_dim, action_dim, num_ensemble=5):
        super(UDAE, self).__init__()
        self.num_ensemble = num_ensemble
        self.models = nn.ModuleList([self.build_model(state_dim, action_dim) for _ in range(num_ensemble)])

    def build_model(self, state_dim, action_dim):
        return nn.Sequential(
            nn.Linear(state_dim, 128),
            nn.ReLU(),
            nn.Linear(128, 128),
            nn.ReLU(),
            nn.Linear(128, action_dim)
        )

    def forward(self, state):
        q_values = [model(state) for model in self.models]
        return torch.stack(q_values)

    def get_action(self, state, epsilon):
        if random.random() < epsilon:
            return random.randint(0, self.models[0][-1].out_features - 1)
        state = torch.FloatTensor(state).unsqueeze(0)
        q_values = self.forward(state)
        q_mean = q_values.mean(dim=0)
        return q_mean.argmax().item()

if __name__ == '__main__':
    model = UDAE(state_dim=3, action_dim=4)
    state = np.random.rand(3)
    action = model.get_action(state, epsilon=0.1)
    print(f"Selected action: {action}")
