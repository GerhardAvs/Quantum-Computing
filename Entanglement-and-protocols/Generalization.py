"""<h3>(generalization)</h3>

Suppose that we have  $ k>1 $  qubits (or bits). 

Then, any deterministic (basis) state can be represented by   $ k $ bits:  $ \ket{b_1b_2\cdots b_k} $ , where any  $ b_j \in \{0,1\} $ for $ 1 \leq j \leq k $.
- What is the size of the vector representing the states of $k$ qubits?
- If the decimal value of $ \ket{b_1 b_2 \cdots b_k} $ is $ b $, then which entry has the value of 1?"""

from qiskit import QuantumCircuit

# remark the concise representation of a quantum circuit
qc = QuantumCircuit(2)

qc.h(0)
qc.h(1)

qc.draw(output='mpl',reverse_bits=True)