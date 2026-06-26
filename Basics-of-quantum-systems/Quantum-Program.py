"""Randomly picking an 8-bit binary number

Design a quantum circuit with 8 quantum bits and 8 classical bits.

For each quantum bit, flip a coin by python, and apply x-gate if the outcome is head.

Measure your quantum bits.

Execute your circuit 10 times.

Repeat this task as much as you want, and enjoy your random choices."""


from qiskit import QuantumRegister, ClassicalRegister, QuantumCircuit
from qiskit_aer import AerSimulator
from random import randrange

qreg = QuantumRegister(8, "qreg")
creg = ClassicalRegister(8,"creg")
qxc = QuantumCircuit(qreg,creg)

# cara 1, cruz 0
for i in range(8): # se ejecuta 0 1 2 3 4 5 6 7 
    rand = randrange(2) # escoge un numero random entre 0 y 1
    if rand == 1:
        qxc.x(qreg[i])

qxc.barrier()
qxc.measure(qreg,creg)
# qxc.draw(output='mpl') to draw the circuit

job = AerSimulator().run(qxc,shots=10)
counts = job.result().get_counts(qxc)
print(counts)