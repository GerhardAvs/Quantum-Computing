"""Elige un ángulo al azar theta E [0, 2pi)

Supongamos que tenemos 1000 copias del estado cuántico |v> = (cos(theta) sin(Theta))
y medimos cada uno de ellos.

¿Cuáles son las cantidades esperadas de observar los estados 0 y 1?

Implementa el experimento anterior diseñando un circuito cuántico y estableciendo el estado cuántico mediante el uso de una puerta Ry.

Compara tus resultados experimentales y analíticos.

Repite la tarea un par de veces. """

from qiskit import QuantumRegister, ClassicalRegister, QuantumCircuit
from qiskit_aer import AerSimulator
from qiskit.visualization import plot_histogram
from math import pi, sin, cos

Rangle = (41*pi)/36 # 205 deg

qreg = QuantumRegister(1, 'Qreg')
creg = ClassicalRegister(1, 'Creg')

QxC = QuantumCircuit(qreg, creg)

QxC.ry(2*Rangle,qreg[0])
QxC.measure(qreg,creg)

#QxC.draw(output='mpl')

# execute the program 1000 times
T = AerSimulator().run(QxC,shots=1000)

# print the results
c = T.result().get_counts(QxC)
print(c)

# draw the histogram
#plot_histogram(c)

Qstate = [cos(Rangle), sin(Rangle)]
conta = 0
acum = 0

for state in Qstate:
    print(f'Amplitud del estado |{conta}> es {state}')
    print(f'Probabilidad del estado |{conta}> es {state**2}\n')
    acum = acum + state**2
    conta += 1
print(f'Probabilidad total: {acum * 100}%\n')

expCeros = 1000*cos(Rangle)**2
expOnes = 1000*sin(Rangle)**2

print("The expected value of observing '0' is",round(expCeros,4))
print("The expected value of observing '1' is",round(expOnes,4))