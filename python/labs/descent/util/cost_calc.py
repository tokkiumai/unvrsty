import numpy as np


def cost_calc(theta: int, X: np.dot, y: list[float]) -> float:
    m = len(y)
    predictions = X.dot(theta)
    cost = (1 / 2 * m) * np.sum(np.square(predictions - y))
    return cost
