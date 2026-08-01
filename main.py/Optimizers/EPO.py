import math
from mealpy import FloatVar
from mealpy.swarm_based import EPC

def EPO(cost_function):
    problem_dict = {"bounds": FloatVar(lb=-math.pi, ub=math.pi, name="delta"), "obj_func": cost_function, "minmax": "min", "verbose": False, "log_to": "None"}
    optimizer = EPC.DevEPC(epoch=1000, pop_size=50)
    best = optimizer.solve(problem_dict)
    return best
