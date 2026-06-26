"""Remember that x-gate flips the value of a qubit.

Design a quantum circuit with a single qubit.

The qubit is initially set to state 0
.

Set the value of qubit to state 1
 by using x-gate.

Experiment 1: Apply one Hadamard gate, make measurement, and execute your program 10000 times.

Experiment 2: Apply two Hadamard gates, make measurement, and execute your program 10000 times.

Compare your results.

The following two diagrams represent these experiments."""

from qiskit import QuantumRegister, ClassicalRegister, QuantumCircuit
from qiskit_aer import AerSimulator

qreg = QuantumRegister(1,'Qbit')
creg = ClassicalRegister(1,'Cbit')
qxc = QuantumCircuit(qreg,creg)

qxc.x(qreg[0])
qxc.h(qreg[0])
qxc.h(qreg[0])

qxc.measure(qreg,creg)
# qxc.draw(output='mpl')

t = AerSimulator().run(qxc,shots=10000)
c = t.result().get_counts(qxc)
print(c) # print the outcomes