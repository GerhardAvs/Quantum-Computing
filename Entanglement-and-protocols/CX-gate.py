from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator

pairs = ['00','01','10','11']

for pair in pairs: # corre una vez, pair = str = '00'
    qc = QuantumCircuit(2,2) # (qreg, creg), 2 reg quant y 2 reg classi
    # initialize the pair
    # we follow the reading order in Qiskit
    # q1-tensor-q0
    if pair[1] == '1': # '00' pair[1] = '0'
        qc.x(0)
    if pair[0] =='1':
        qc.x(1)
    qc.cx(1,0)
    qc.measure(0,0)
    qc.measure(1,1)
    display(qc.draw(output='mpl',reverse_bits=True))
    job = AerSimulator().run(qc,shots=1024)
    counts = job.result().get_counts(qc)
    print(pair,"--CNOT->",counts)