import numpy as np

def f(x):
    return (np.sin(x))**2 + np.cosh(x)

def dydx_f(x):
    return np.sin(2*x) + np.sinh(x)
