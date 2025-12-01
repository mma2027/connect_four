import numpy as np


def sigmoid(x):
    return 1 / (1 + np.exp(-x))

def drelu(x):
    return (x > 0).astype(float)


class SimpleNN:
    def __init__(self, hidden = 64):
        self.input_size = 84
        self.W1 = np.random.uniform(-0.1, 0.1, (hidden, self.input_size))
        self.b1 = np.zeros(hidden)
        self.W2 = np.random.uniform(-0.1, 0.1, hidden)
        self.b2 = 0.0

    def forward(self, x):
        self.x = x
        self.z1 = self.W1 @ x + self.b1          # shape (hidden,)
        self.a1 = np.maximum(self.z1, 0)         # ReLU
        self.z2 = self.W2 @ self.a1 + self.b2
        self.a2 = sigmoid(self.z2)
        return self.a2
    
    def backward(self, y, lr=0.01):
        # Output layer
        dz2 = self.a2 - y                        # scalar
        dW2 = dz2 * self.a1                      # (hidden,)
        db2 = dz2

        # Hidden layer
        dz1 = (self.W2 * dz2) * drelu(self.z1)   # (hidden,)
        dW1 = dz1[:, None] @ self.x[None, :]     # (hidden,42)
        db1 = dz1

        # Update
        self.W2 -= lr * dW2
        self.b2 -= lr * db2
        self.W1 -= lr * dW1
        self.b1 -= lr * db1

model = SimpleNN()