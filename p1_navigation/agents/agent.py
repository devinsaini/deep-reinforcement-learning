import random

class Agent():
    def __init__(self, state_size, action_size, gamma, learning_rate, seed, device):
        self.state_size = state_size
        self.action_size = action_size
        self.gamma = gamma
        self.learning_rate = learning_rate
        self.seed = random.seed(seed)
        self.device = device

    def compute_action(self, state, eps=0.):
        return NotImplemented

    def train(self, experiences, gamma):
        return NotImplemented