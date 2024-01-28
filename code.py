import numpy as np
import matplotlib.pyplot as plt

np.random.seed(42)
X = 2  np.random.rand(100, 1)
y = 4 + 3  X + np.random.randn(100, 1)
X_b = np.c_[np.ones((100, 1)), X]

theta = np.random.randn(2, 1)
learning_rate = 0.01
n_iterations = 1000

for _ in range(n_iterations)
    gradients = 2100  X_b.T.dot(X_b.dot(theta) - y)
    theta = theta - learning_rate  gradients

plt.scatter(X, y, label='Data points')
plt.plot(X, X_b.dot(theta), color='red', label='Regression line')
plt.xlabel('X')
plt.ylabel('y')
plt.legend()
plt.show()
