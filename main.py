import numpy as np
import matplotlib.pyplot as plt
from matplotlib.pyplot import figure
import function1
plt.rcParams.update({'font.size': 6})

x  = np.linspace(-5, 5, 150)
x_end_left  = x[0]
x_end_right = x[-1]

f           = function1.f
dydx        = function1.dydx_f

# Plot of function and its derivative 
figure(figsize=(4, 3), dpi=250)
plt.plot(x, f(x),    color="black", linewidth=2, label="Function")
plt.plot(x, dydx(x), color="red",   linewidth=2, label="Functions' Derivative")
plt.xlim(x_end_left, x_end_right)
plt.xlabel("$x$")
plt.ylabel("$y$")
plt.grid(True)
plt.legend(loc="best")
plt.show()

def derivative(f, dx, a, method):
    if method == "central":
        return (f(a + dx) - f(a - dx))/(2*dx)
    elif method == "forward":
        return (f(a + dx) - f(a))/dx
    elif method == "backward":
        return (f(a) - f(a - dx))/dx
    else:
        raise ValueError("Numerical differentiation method must be 'central', 'forward', or 'backward'")

def absolute_error(numerical, analytical):
    return np.abs(numerical - analytical)

def relative_error(numerical, analytical):
    return absolute_error(numerical, analytical) / np.abs(analytical)

dx_values               = [1e-2, 1e-4, 1e-8]
for dx in dx_values:

    analytical          = np.array([dydx(xs) for xs in x])
    central_values      = np.array([derivative(f, dx, xs, "central") for xs in x]) 
    forward_values      = np.array([derivative(f, dx, xs, "forward") for xs in x]) 
    backward_values     = np.array([derivative(f, dx, xs, "backward") for xs in x]) 
    
    if 0 in set(analytical):
        print("The existence of 0 is present in the analytical derivative.")
        print("Only the absolute error will be presented and calculated \n")
    
        # Absolute Errors
        central_values_abs  = np.array(absolute_error(central_values, analytical)) 
        forward_values_abs  = np.array(absolute_error(forward_values, analytical)) 
        backward_values_abs = np.array(absolute_error(backward_values, analytical))
    
        abs_errors          = [[np.average(central_values_abs), "Central Method"], 
                               [np.average(forward_values_abs), "Forward Method"], 
                               [np.average(backward_values_abs), "Backward Method"]]
    ##############################################################################################
        abs_avgs               = []
        for abs_avg in abs_errors:
            abs_avgs.append(abs_avg[:1])
        min_abs_error          = np.min(abs_avgs)
        index_of_min_abs_error = abs_avgs.index(min_abs_error)
        abs_error              = abs_errors[index_of_min_abs_error]
        Method_abs             = abs_error[1]
    ##############################################################################################
        print(f'When dx = {dx}: \n')
        print(f'Central Method Average Absolute Error   = {np.average(central_values_abs)}')
        print(f'Forward Method Average Absolute Error   = {np.average(forward_values_abs)}')
        print(f'Backward Method Average Absolute Error  = {np.average(backward_values_abs)}')
        print(f'{Method_abs} has the smallest average absolute error of {min_abs_error}')
        print("______________________________________________________________________________")
    ##############################################################################################
        # Absolute Error Plot
        figure(figsize=(4,3), dpi=250)
        plt.plot(x, central_values_abs,  color="black", linewidth=1.5, label="Central Method")
        plt.plot(x, forward_values_abs,  color="green", linewidth=1.5, label="Forward Method")
        plt.plot(x, backward_values_abs, color="red",   linewidth=1.5, label="Backward Method")
        plt.xlim(x_end_left, x_end_right)
        plt.yscale("symlog")
        y_values = central_values_abs + forward_values_abs + backward_values_abs
        plt.ylim(min(y_values), max(y_values))
        plt.yticks(np.linspace(min(y_values), max(y_values), 5))
        plt.grid(True)
        plt.title(f'Absolute Error for Different Numerical Methods $(dx={dx})$')
        plt.legend()
        plt.xlabel("$x$")
        plt.ylabel("Absolute Error")
        plt.show()

    else:
        # Absolute Errors
        central_values_abs  = np.array(absolute_error(central_values, analytical)) 
        forward_values_abs  = np.array(absolute_error(forward_values, analytical)) 
        backward_values_abs = np.array(absolute_error(backward_values, analytical))
        # Relative Errors
        central_values_rel  = np.array(relative_error(central_values, analytical)) 
        forward_values_rel  = np.array(relative_error(forward_values, analytical)) 
        backward_values_rel = np.array(relative_error(backward_values, analytical)) 
        
        abs_errors          = [[np.average(central_values_abs), "Central Method"], 
                               [np.average(forward_values_abs), "Forward Method"], 
                               [np.average(backward_values_abs), "Backward Method"]]
        
        rel_errors          = [[np.average(central_values_rel), "Central Method"], 
                               [np.average(forward_values_rel), "Forward Method"], 
                               [np.average(backward_values_rel), "Backward Method"]]
    ##############################################################################################
        abs_avgs               = []
        for abs_avg in abs_errors:
            abs_avgs.append(abs_avg[:1])
        min_abs_error          = np.min(abs_avgs)
        index_of_min_abs_error = abs_avgs.index(min_abs_error)
        abs_error              = abs_errors[index_of_min_abs_error]
        Method_abs             = abs_error[1]
    ##############################################################################################
        rel_avgs               = []
        for rel_avg in rel_errors:
            rel_avgs.append(rel_avg[:1])
        min_rel_error          = np.min(rel_avgs)
        index_of_min_rel_error = rel_avgs.index(min_rel_error)
        rel_error = rel_errors[index_of_min_rel_error]
        Method_rel             = rel_error[1]
    ##############################################################################################
        print(f'When dx = {dx}: \n')
        print(f'Central Method Average Absolute Error   = {np.average(central_values_abs)}')
        print(f'Forward Method Average Absolute Error   = {np.average(forward_values_abs)}')
        print(f'Backward Method Average Absolute Error  = {np.average(backward_values_abs)}')
        print(f'{Method_abs} has the smallest average absolute error of {min_abs_error} \n')
        print(f'Central Method Average Relative Error   = {np.average(central_values_rel)}')
        print(f'Forward Method Average Relative Error   = {np.average(forward_values_rel)}')
        print(f'Backward Method Average Relative Error  = {np.average(backward_values_rel)}')
        print(f'{Method_rel} has the smallest average relative error of {min_rel_error}')
        print("______________________________________________________________________________")
    ##############################################################################################
        # Absolute Error Plot
        figure(figsize=(4,3), dpi=250)
        plt.semilogy(x, central_values_abs,  color="black", linewidth=1.5, label="Central Method")
        plt.semilogy(x, forward_values_abs,  color="green", linewidth=1.5, label="Forward Method")
        plt.semilogy(x, backward_values_abs, color="red",   linewidth=1.5, label="Backward Method")
        plt.xlim(x_end_left, x_end_right)
        plt.grid(True)
        plt.title(f'Absolute Error for Different Numerical Methods $(dx={dx})$')
        plt.legend()
        plt.xlabel("$x$")
        plt.ylabel("Absolute Error")
        plt.show()
    
        # Relative Error Plot
        figure(figsize=(4,3), dpi=250)
        plt.semilogy(x, central_values_rel,  color="black", linewidth=1.5, label="Central Method")
        plt.semilogy(x, forward_values_rel,  color="green", linewidth=1.5, label="Forward Method")
        plt.semilogy(x, backward_values_rel, color="red",   linewidth=1.5, label="Backward Method")
        plt.xlim(x_end_left, x_end_right)
        plt.grid(True)
        plt.title(f'Relative Error for Different Numerical Methods $(dx={dx})$')
        plt.legend()
        plt.xlabel("$x$")
        plt.ylabel("Relative Error")
        plt.show()
    