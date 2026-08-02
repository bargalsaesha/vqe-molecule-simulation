import spsa
import numpy as np

#SPSA optimizer
def SPSA(cost_function):
    optimizer = spsa.minimize(cost_function, np.array([-180.0]), iterations = 10)
    return optimizer
