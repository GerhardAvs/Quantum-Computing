"""Unitary_simulator proporciona una única representación
matricial de todas las compuertas del circuito hasta ese punto."""

#job = UnitarySimulator().run(qc)
#current_unitary = job.result().get_unitary(circuit, decimals=3).data
#print(current_unitary)

from qiskit import QuantumCircuit
from qiskit_aer import UnitarySimulator

QxC = QuantumCircuit(2)

QxC.h(0)
QxC.h(1)

#qc.draw(output='mpl',reverse_bits=True)

# H tensor H

job = UnitarySimulator().run(QxC)
current_unitary = job.result().get_unitary(QxC, decimals=3).data
for row in current_unitary:
    column = ""
    for entry in row:
        column = column + str(entry.real) + " "
    print(column)
