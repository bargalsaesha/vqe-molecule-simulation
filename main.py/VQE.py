import cirq
import math
import numpy as np
import openfermion as of
import openfermionpyscf as ofpyscf

def molecule():
    #setting up the molecule's attributes
    geometry = [['H', [0.0, 0.0, 0.0]], ['H', [0.0, 0.0, 0.74]]]
    basis = 'sto-3g'
    multiplicity = 1
    charge = 0

    #utilizing openfermion and piscyf to create the hamiltonians
    hamiltonian = ofpyscf.generate_molecular_hamiltonian(geometry, basis, multiplicity, charge)
    hamiltonian_qubit = of.jordan_wigner(of.get_fermion_operator(hamiltonian))
    hamiltonian_matrix = of.get_sparse_operator(hamiltonian_qubit)
    return hamiltonian_matrix

#setting up ansatz with 4 qubits
def ansatz(angle):
  qubits = cirq.NamedQubit.range(4, prefix='q')
  circuit = cirq.Circuit()
  circuit.append([cirq.rx(math.radians(angle[0])).on(qubits[0]), cirq.rx(math.radians(angle[0])).on(qubits[1]), cirq.rx(math.radians(angle[0])).on(qubits[2]), cirq.rx(math.radians(angle[0])).on(qubits[3])])
  circuit.append([cirq.CNOT(qubits[0], qubits[1]), cirq.CNOT(qubits[2], qubits[3])])
  return circuit, qubits

#setting up cost function
def expectation_value(angle):
  sim = cirq.Simulator()

  #getting a state vector from ansatz
  circuit, qubits = ansatz(angle)
  result = sim.simulate(circuit)
  vector = result.final_state_vector

  #finding the total energy of the molecule through matrix multiplication
  energy = np.dot(vector.conj(), molecule().dot(vector))

  #returning only the real value of the energy
  return energy.real
