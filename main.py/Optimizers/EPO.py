from mealpy import FloatVar
from mealpy.swarm_based import EPC

#Emperor Penguin Optimizer
def EPO(cost_function):
    problem_dict = {"bounds": FloatVar(lb=-180, ub=180, name="delta"), "obj_func": cost_function, "minmax": "min", "verbose": False, "log_to": "None"}
    optimizer = EPC.DevEPC(epoch=300, pop_size=10)
    best = optimizer.solve(problem_dict)
    return best
