# import all necessary objects and methods for quantum circuits
from qiskit import QuantumRegister, ClassicalRegister, QuantumCircuit
from qiskit_aer import AerSimulator
# import randrange for random choices
from random import randrange

#
# your code is here
#
qreg = QuantumRegister(5, 'Qreg')
creg = ClassicalRegister(5, 'Creg')
QxC = QuantumCircuit(qreg, creg)

for i in range(5): #H+Z+H = X
    QxC.h(qreg[i])
    if randrange(2) == 0:
        QxC.z(qreg[i])
    QxC.h(qreg[i])
QxC.barrier()
QxC.measure(qreg, creg)
#display(QxC.draw(output='mpl'))

# execute the program 1000 times
T = AerSimulator().run(QxC,shots=1000)

# print the results
c = T.result().get_counts(QxC)
print(c)