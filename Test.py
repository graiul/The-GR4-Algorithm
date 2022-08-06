from numpy import pi
from qiskit import QuantumRegister, ClassicalRegister, QuantumCircuit, execute
from qiskit.providers.ibmq import IBMQ
from distributed import Client, LocalCluster, Worker, wait, progress

def send_to_kingdom(quantum_backend_name, circuit_object):
    # IBMQ.save_account('e6bbad0f51ab787aec48bed242c422777f1680f0428e19b34e19bbcd467a2faff2bdcedd0cbb04b19f4bb700f66900728f778d4bc8226785e6c35dc818374ac8',
    #                   overwrite=True)
    provider = IBMQ.load_account()
    # print(IBMQ.providers())
    # print(IBMQ.get_provider(hub='ibm-q', group='open', project='main'))

    # backend = simulator = provider.get_backend('ibmq_qasm_simulator')
    # backend = simulator = provider.get_backend('ibmq_lima')
    backend = provider.get_backend(quantum_backend_name)

    # # CIRCUITS

    # #
    # https://qiskit.org/documentation/getting_started.html
    # # Create a Quantum Circuit acting on the q register
    # circuit = QuantumCircuit(2, 2)
    # # Add a H gate on qubit 0
    # circuit.h(0)
    # # Add a CX (CNOT) gate on control qubit 0 and target qubit 1
    # circuit.cx(0, 1)
    # # Map the quantum measurement to the classical bits
    # circuit.measure([0,1], [0,1])
    # #

    # #
    # https://quantum-computing.ibm.com/composer/docs/guide/grovers-algorithm
    # Grover pentru 00
    # qreg_q = QuantumRegister(2, 'q')
    # creg_c = ClassicalRegister(2, 'c')
    # circuit = QuantumCircuit(qreg_q, creg_c)
    # circuit.reset(qreg_q[0])
    # circuit.reset(qreg_q[1])
    # circuit.h(qreg_q[1])
    # circuit.h(qreg_q[0])
    # circuit.s(qreg_q[1])
    # circuit.s(qreg_q[0])
    # circuit.h(qreg_q[1])
    # circuit.cx(qreg_q[0], qreg_q[1])
    # circuit.s(qreg_q[0])
    # circuit.h(qreg_q[1])
    # circuit.h(qreg_q[0])
    # circuit.s(qreg_q[1])
    # circuit.x(qreg_q[0])
    # circuit.h(qreg_q[1])
    # circuit.x(qreg_q[1])
    # circuit.h(qreg_q[1])
    # circuit.cx(qreg_q[0], qreg_q[1])
    # circuit.x(qreg_q[0])
    # circuit.h(qreg_q[1])
    # circuit.h(qreg_q[0])
    # circuit.x(qreg_q[1])
    # circuit.h(qreg_q[1])
    # circuit.measure(qreg_q[0], creg_c[0])
    # circuit.measure(qreg_q[1], creg_c[1])

    # Test nr 1, rulat neparalel in 23 MAR 2021
    # si paralel in 24 MAR 2021

    # VECHI
    # https://qiskit.org/textbook/ch-algorithms/grover.html
    # circuit = self.initialize_s(self.prepare_quantum_circuit(2), [0, 1])
    # VECHI

    # Execute the circuit on the qasm simulator
    job = execute(circuit_object, backend, shots=8192)
    # print(backend.name())

    # #
    # https://medium.com/analytics-vidhya/grovers-algorithm-in-python-c1dfa132e3af
    #
    from qiskit.tools.monitor import job_monitor
    job_monitor(job, interval=2)
    # #

    # Grab results from the job
    result = job.result()

    # Returns counts
    counts = result.get_counts(circuit_object)
    # print("\nTotal count for 00 and 11 are:",counts)
    # print("\nTotal count for 00, 01, 10 and 11 are:", counts)
    print("\nCounts: ", counts)

# Circuit Test 6.3
qreg_q_6_3 = QuantumRegister(5, 'q')
creg_c_6_3 = ClassicalRegister(5, 'c')
circuit_6_3 = QuantumCircuit(qreg_q_6_3, creg_c_6_3)

circuit_6_3.reset(qreg_q_6_3[0])
circuit_6_3.reset(qreg_q_6_3[1])
circuit_6_3.reset(qreg_q_6_3[2])
circuit_6_3.reset(qreg_q_6_3[3])
circuit_6_3.reset(qreg_q_6_3[4])
circuit_6_3.h(qreg_q_6_3[0])
circuit_6_3.h(qreg_q_6_3[1])
circuit_6_3.h(qreg_q_6_3[2])
circuit_6_3.h(qreg_q_6_3[3])
circuit_6_3.h(qreg_q_6_3[4])
circuit_6_3.t(qreg_q_6_3[0])
circuit_6_3.sx(qreg_q_6_3[2])
circuit_6_3.s(qreg_q_6_3[3])
circuit_6_3.p(pi / 2, qreg_q_6_3[4])
circuit_6_3.h(qreg_q_6_3[0])
circuit_6_3.cx(qreg_q_6_3[1], qreg_q_6_3[2])
circuit_6_3.h(qreg_q_6_3[3])
circuit_6_3.h(qreg_q_6_3[4])
circuit_6_3.t(qreg_q_6_3[1])
circuit_6_3.h(qreg_q_6_3[2])
circuit_6_3.x(qreg_q_6_3[1])
circuit_6_3.h(qreg_q_6_3[1])
circuit_6_3.measure(qreg_q_6_3[0], creg_c_6_3[0])
circuit_6_3.measure(qreg_q_6_3[1], creg_c_6_3[1])
circuit_6_3.measure(qreg_q_6_3[2], creg_c_6_3[2])
circuit_6_3.measure(qreg_q_6_3[3], creg_c_6_3[3])
circuit_6_3.measure(qreg_q_6_3[4], creg_c_6_3[4])

# # Circuit Test 7.3, 15 Qubits
#
# qreg_q_7_3 = QuantumRegister(15, 'q')
# creg_c_7_3 = ClassicalRegister(15, 'c')
# circuit_7_3 = QuantumCircuit(qreg_q_7_3, creg_c_7_3)
#
# circuit_7_3.reset(qreg_q_7_3[0])
# circuit_7_3.reset(qreg_q_7_3[1])
# circuit_7_3.reset(qreg_q_7_3[2])
# circuit_7_3.reset(qreg_q_7_3[3])
# circuit_7_3.reset(qreg_q_7_3[4])
# circuit_7_3.reset(qreg_q_7_3[5])
# circuit_7_3.reset(qreg_q_7_3[6])
# circuit_7_3.reset(qreg_q_7_3[7])
# circuit_7_3.reset(qreg_q_7_3[8])
# circuit_7_3.reset(qreg_q_7_3[9])
# circuit_7_3.reset(qreg_q_7_3[10])
# circuit_7_3.reset(qreg_q_7_3[11])
# circuit_7_3.reset(qreg_q_7_3[12])
# circuit_7_3.reset(qreg_q_7_3[13])
# circuit_7_3.reset(qreg_q_7_3[14])
# circuit_7_3.h(qreg_q_7_3[0])
# circuit_7_3.h(qreg_q_7_3[1])
# circuit_7_3.h(qreg_q_7_3[2])
# circuit_7_3.h(qreg_q_7_3[3])
# circuit_7_3.h(qreg_q_7_3[4])
# circuit_7_3.h(qreg_q_7_3[5])
# circuit_7_3.h(qreg_q_7_3[6])
# circuit_7_3.h(qreg_q_7_3[7])
# circuit_7_3.h(qreg_q_7_3[8])
# circuit_7_3.h(qreg_q_7_3[9])
# circuit_7_3.h(qreg_q_7_3[10])
# circuit_7_3.h(qreg_q_7_3[11])
# circuit_7_3.h(qreg_q_7_3[12])
# circuit_7_3.h(qreg_q_7_3[13])
# circuit_7_3.h(qreg_q_7_3[14])
# circuit_7_3.rx(pi / 2, qreg_q_7_3[0])
# circuit_7_3.u(pi / 2, pi / 2, pi / 2, qreg_q_7_3[1])
# circuit_7_3.p(pi / 2, qreg_q_7_3[2])
# circuit_7_3.z(qreg_q_7_3[3])
# circuit_7_3.y(qreg_q_7_3[4])
# circuit_7_3.t(qreg_q_7_3[5])
# circuit_7_3.p(pi / 2, qreg_q_7_3[6])
# circuit_7_3.y(qreg_q_7_3[7])
# circuit_7_3.u(pi / 2, pi / 2, pi / 2, qreg_q_7_3[8])
# circuit_7_3.z(qreg_q_7_3[9])
# circuit_7_3.sx(qreg_q_7_3[10])
# circuit_7_3.z(qreg_q_7_3[11])
# circuit_7_3.p(pi / 2, qreg_q_7_3[12])
# circuit_7_3.ry(pi / 2, qreg_q_7_3[13])
# circuit_7_3.u(pi / 2, pi / 2, pi / 2, qreg_q_7_3[14])
# circuit_7_3.s(qreg_q_7_3[0])
# circuit_7_3.h(qreg_q_7_3[1])
# circuit_7_3.h(qreg_q_7_3[2])
# circuit_7_3.h(qreg_q_7_3[3])
# circuit_7_3.h(qreg_q_7_3[4])
# circuit_7_3.h(qreg_q_7_3[5])
# circuit_7_3.h(qreg_q_7_3[6])
# circuit_7_3.h(qreg_q_7_3[7])
# circuit_7_3.h(qreg_q_7_3[8])
# circuit_7_3.h(qreg_q_7_3[9])
# circuit_7_3.h(qreg_q_7_3[10])
# circuit_7_3.h(qreg_q_7_3[11])
# circuit_7_3.h(qreg_q_7_3[12])
# circuit_7_3.h(qreg_q_7_3[13])
# circuit_7_3.h(qreg_q_7_3[14])
# circuit_7_3.h(qreg_q_7_3[0])
# circuit_7_3.tdg(qreg_q_7_3[3])
# circuit_7_3.sdg(qreg_q_7_3[4])
# circuit_7_3.rz(pi / 2, qreg_q_7_3[5])
# circuit_7_3.sx(qreg_q_7_3[6])
# circuit_7_3.sx(qreg_q_7_3[13])
# circuit_7_3.y(qreg_q_7_3[14])
# circuit_7_3.h(qreg_q_7_3[5])
# circuit_7_3.h(qreg_q_7_3[13])
# circuit_7_3.measure(qreg_q_7_3[0], creg_c_7_3[0])
# circuit_7_3.measure(qreg_q_7_3[1], creg_c_7_3[1])
# circuit_7_3.measure(qreg_q_7_3[2], creg_c_7_3[2])
# circuit_7_3.measure(qreg_q_7_3[3], creg_c_7_3[3])
# circuit_7_3.measure(qreg_q_7_3[4], creg_c_7_3[4])
# circuit_7_3.measure(qreg_q_7_3[5], creg_c_7_3[5])
# circuit_7_3.measure(qreg_q_7_3[6], creg_c_7_3[6])
# circuit_7_3.measure(qreg_q_7_3[7], creg_c_7_3[7])
# circuit_7_3.measure(qreg_q_7_3[8], creg_c_7_3[8])
# circuit_7_3.measure(qreg_q_7_3[9], creg_c_7_3[9])
# circuit_7_3.measure(qreg_q_7_3[10], creg_c_7_3[10])
# circuit_7_3.measure(qreg_q_7_3[11], creg_c_7_3[11])
# circuit_7_3.measure(qreg_q_7_3[12], creg_c_7_3[12])
# circuit_7_3.measure(qreg_q_7_3[13], creg_c_7_3[13])
# circuit_7_3.measure(qreg_q_7_3[14], creg_c_7_3[14])


# https://quantumcomputing.stackexchange.com/questions/13667/qiskit-get-gates-from-circuit-object

# for gate in circuit.data:
    # print('\ngate name:', gate[0].name)
    # print('qubit(s) acted on:', gate[1])
    # print('other paramters (such as angles):', gate[0].params)
    # print(gate)

# nr_of_qubits = circuit_6_3.num_qubits
# print(nr_of_qubits)

# send_to_kingdom('ibmq_lima', circuit_6_3)
# https://github.com/dask/distributed/issues/2422
if __name__ == '__main__':
    lc = LocalCluster()
    lc.scale(10)
    client = Client(lc)
    future1 = client.submit(send_to_kingdom, 'ibmq_lima', circuit_6_3)
    wait(future1)
    future1.result()

# def quantum_circuit_splitter(circuit, nr_of_qubits_per_part):



