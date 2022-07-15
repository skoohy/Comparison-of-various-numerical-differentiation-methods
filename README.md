# Compariosn-of-various-numerical-differentiation-methods

In this numerical experiment I compare the absolute error and relative error (if possible) between three different numerical differentiation techniques. This includes the forward, backward and central difference approximations. 

### Requirements and Tutorial:
Import your own function from a seperate .py file
Inside that file must include two functions
* A function defined as f 
* The analytical derivative of f defined as dydx_f
These functions can be named to whatever you may want with minor changes in the code. Once the functions you wish to work with are imported make sure that in main.py the variables "f" and "dydx" (line 11 and 12) are correctly defined. From there you can run the file and an output of error plots and error averages will print. The x range to which the derivatives (analytically and numerically) are calculted can be easily modified in line 7 of main.py, you are also able to modify the step-size, dx, values you may want to compare with (line 41 in main.py).

If there exist a $0$ in the analytical derivative solution (like in function6) the relative error will skipped (due to divison by zero) and only the absolute
error will be presented. However, even if you know there is a $0$ in the derivative it is possible that due to the discretization for the x values of the analytical solution, the $0$ may be skipped and the relative error will be then be presented and so will the absolute error. An example of this can be seen in function1, function4, function5.

From what I have experimented with the central difference approximation seems to produe the best results in all cases
