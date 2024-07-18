import numpy as np
from util import cost_calc


def minibatch_gradient_descent(X, y, theta, step=0.01, iterations=100, batch_size=20):
    m = len(y)
    cost_history = np.zeros(iterations)
    for it in range(iterations):
        cost = 0.0
        indices = np.random.permutation(m)
        X = X[indices]
        y = y[indices]
        for i in range(0, m, batch_size):
            X_i = X[i:i + batch_size]
            y_i = y[i:i + batch_size]
            X_i = np.c_[np.ones(len(X_i)), X_i]
            prediction = np.dot(X_i, theta)
            theta = theta - (1 / m) * step * (X_i.T.dot((prediction - y_i)))
            cost += cost_calc(theta, X_i, y_i)
        cost_history[it] = cost
    return theta, cost_history
