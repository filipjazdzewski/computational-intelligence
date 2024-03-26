import numpy as np


# Funkcja aktywacji
def sigmoid(x):
    return 1 / (1 + np.exp(-x))


def forwardPass(age, weight, height):
    hidden1 = age * -0.46122 + weight * 0.97314 + height * -0.39203 + 0.80109
    hidden1_after_activation = sigmoid(hidden1)
    hidden2 = age * 0.78548 + weight * 2.10584 + height * -0.57847 + 0.43529
    hidden2_after_activation = sigmoid(hidden2)
    output = (
        hidden1_after_activation * -0.81546
        + hidden2_after_activation * 1.03775
        - 0.2368
    )
    return output


print(forwardPass(23, 75, 176))
