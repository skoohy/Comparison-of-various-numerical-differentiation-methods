import numpy as np

def f(x):
    return np.log(np.exp(x) + 1)

def dydx_f(x):
    return np.exp(x) / (np.exp(x) + 1)