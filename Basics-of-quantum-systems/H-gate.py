# import all necessary objects and methods for quantum circuits
from qiskit import QuantumRegister, ClassicalRegister, QuantumCircuit
from qiskit_aer import AerSimulator

# define a quantum register with a single qubit
q = QuantumRegister(1, "q")
# define a classical register with a single bit
c = ClassicalRegister(1, "c")
# define a quantum circuit
qc = QuantumCircuit(q, c)

# apply the first Hadamard
qc.h(q[0])

# the first measurement
qc.measure(q, c)

# --- CORRECCIÓN RECOMENDADA (Qiskit 1.x+) ---
# Aplicar el segundo Hadamard si el resultado de la medición es 0
with qc.if_test((c, 0)):
    qc.h(q[0])
# ---------------------------------------------

# the second measurement
qc.measure(q[0], c)

# draw the circuit
#display(qc.draw(output="mpl"))

job = AerSimulator().run(qc,shots=1000)
counts = job.result().get_counts(qc)   
print(counts)