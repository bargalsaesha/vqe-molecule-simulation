import sys
from pathlib import Path

path = Path(__file__).resolve().parent
sys.path.append(str(path / "main.py"))
sys.path.append(str(path / "main.py" / "Optimizers"))

import Ansatz
from EPO import EPO

result = EPO(Ansatz.expectation_value)
print("Best angle:", result.solution[0])
print("Lowest energy:", result.target.fitness)
