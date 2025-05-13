import torch

class UncertaintyEstimator:
    def __init__(self, uda_model):
        self.uda_model = uda_model

    def estimate_uncertainty(self, state):
        state = torch.FloatTensor(state).unsqueeze(0)
        q_values = self.uda_model(state)
        variance = q_values.var(dim=0).mean()
        return variance.item()

if __name__ == '__main__':
    model = UDAE(state_dim=3, action_dim=4)
    estimator = UncertaintyEstimator(model)
    state = np.random.rand(3)
    uncertainty = estimator.estimate_uncertainty(state)
    print(f"Uncertainty: {uncertainty}")
