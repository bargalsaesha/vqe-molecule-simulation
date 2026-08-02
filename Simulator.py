import sys
from pathlib import Path
from scipy.sparse.linalg import eigsh

path = Path(__file__).resolve().parent
sys.path.append(str(path / "main.py"))
sys.path.append(str(path / "main.py" / "Optimizers"))

import VQE
from EPO import EPO
from COBYLA import COBYLA
from Nelder_Mead import Nelder_Mead
from SLSQP import SLSQP
from SPSA import SPSA

eigenvalues, eigenvectors = eigsh(VQE.molecule(), k=1, which="SA")
print("Exact Solution Best Angle:", 12.8, "degrees")
print("Exact Solution:", eigenvalues[0], "hartrees")
EPO_result = EPO(VQE.expectation_value)
print("EPO Best Angle:", EPO_result.solution[0], "degrees")
print("EPO Lowest Energy:", EPO_result.target.fitness, "hartrees")
COBYLA_result = COBYLA(VQE.expectation_value)
print("COBYLA Best Angle:", COBYLA_result.x[0], "degrees")
print("COBYLA Lowest Energy:", COBYLA_result.fun, "hartrees")
Nelder_Mead_result = Nelder_Mead(VQE.expectation_value)
print("Nelder-Mead Best Angle:", Nelder_Mead_result.x[0], "degrees")
print("Nelder-Mead Lowest Energy:", Nelder_Mead_result.fun, "hartrees")
SLSQP_result = SLSQP(VQE.expectation_value)
print("SLSQP Best Angle:", SLSQP_result.x[0], "degrees")
print("SLSQP Lowest Energy:", SLSQP_result.fun, "hartrees")
SPSA_result = SPSA(VQE.expectation_value)
print("SPSA Best Angle:", SPSA_result[0], "degrees")
print("SPSA Lowest Energy:", VQE.expectation_value(SPSA_result), "hartrees")
