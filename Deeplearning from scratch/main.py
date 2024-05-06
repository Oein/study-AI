import numpy as np

INPUT = np.array([1.0, 0.5])

# activation function
def sigmoid(x):
    return 1 / (1 + np.exp(-x))

W1 = np.array([[0.1, 0.3, 0.5], [0.2, 0.4, 0.6]])
B1 = np.array([0.1, 0.2, 0.3])

# Layer 1 Calc
A1 = np.dot(INPUT, W1) + B1
Z1 = sigmoid(A1)

W2 = np.array([[0.1, 0.4], [0.2, 0.5], [0.3, 0.6]])
B2 = np.array([0.1, 0.2])

# Layer 2 Calc
A2 = np.dot(Z1, W2) + B2
Z2 = sigmoid(A2)

W3 = np.array([[0.1, 0.3], [0.2, 0.4]])
B3 = np.array([0.1, 0.2])

# Layer 3 Calc

def identify_function(x):
    return x

def softmax(a):
    c = np.max(a)
    exp_a = np.exp(a - c)
    sum_exp_a = np.sum(exp_a)
    return exp_a / sum_exp_a

A3 = np.dot(Z2, W3) + B3
Y = identify_function(A3)

# print(Y)
# print(np.exp(10000))