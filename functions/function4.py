import numpy as np

def f(x):
    return np.tanh(x)

def dydx_f(x):
    return (1 / np.cosh(x))**2