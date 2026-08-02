import scipy

#Nelder-Mead optimizer
def Nelder_Mead(cost_function):
    optimizer = scipy.optimize.minimize(fun=cost_function, x0 = [-180, -135, -90, -45, 0, 45, 90, 135, 180], method = "Nelder-Mead", bounds = [(-180, 180)])
    return optimizer
