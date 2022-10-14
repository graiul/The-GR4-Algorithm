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
qreg_q_7_3 = QuantumRegister(15, 'q')
creg_c_7_3 = ClassicalRegister(15, 'c')
circuit_7_3 = QuantumCircuit(qreg_q_7_3, creg_c_7_3)

circuit_7_3.reset(qreg_q_7_3[0])
circuit_7_3.reset(qreg_q_7_3[1])
circuit_7_3.reset(qreg_q_7_3[2])
circuit_7_3.reset(qreg_q_7_3[3])
circuit_7_3.reset(qreg_q_7_3[4])
circuit_7_3.reset(qreg_q_7_3[5])
circuit_7_3.reset(qreg_q_7_3[6])
circuit_7_3.reset(qreg_q_7_3[7])
circuit_7_3.reset(qreg_q_7_3[8])
circuit_7_3.reset(qreg_q_7_3[9])
circuit_7_3.reset(qreg_q_7_3[10])
circuit_7_3.reset(qreg_q_7_3[11])
circuit_7_3.reset(qreg_q_7_3[12])
circuit_7_3.reset(qreg_q_7_3[13])
circuit_7_3.reset(qreg_q_7_3[14])
circuit_7_3.h(qreg_q_7_3[0])
circuit_7_3.h(qreg_q_7_3[1])
circuit_7_3.h(qreg_q_7_3[2])
circuit_7_3.h(qreg_q_7_3[3])
circuit_7_3.h(qreg_q_7_3[4])
circuit_7_3.h(qreg_q_7_3[5])
circuit_7_3.h(qreg_q_7_3[6])
circuit_7_3.h(qreg_q_7_3[7])
circuit_7_3.h(qreg_q_7_3[8])
circuit_7_3.h(qreg_q_7_3[9])
circuit_7_3.h(qreg_q_7_3[10])
circuit_7_3.h(qreg_q_7_3[11])
circuit_7_3.h(qreg_q_7_3[12])
circuit_7_3.h(qreg_q_7_3[13])
circuit_7_3.h(qreg_q_7_3[14])
circuit_7_3.rx(pi / 2, qreg_q_7_3[0])
circuit_7_3.u(pi / 2, pi / 2, pi / 2, qreg_q_7_3[1])
circuit_7_3.p(pi / 2, qreg_q_7_3[2])
circuit_7_3.z(qreg_q_7_3[3])
circuit_7_3.y(qreg_q_7_3[4])
circuit_7_3.t(qreg_q_7_3[5])
circuit_7_3.p(pi / 2, qreg_q_7_3[6])
circuit_7_3.y(qreg_q_7_3[7])
circuit_7_3.u(pi / 2, pi / 2, pi / 2, qreg_q_7_3[8])
circuit_7_3.z(qreg_q_7_3[9])
circuit_7_3.sx(qreg_q_7_3[10])
circuit_7_3.z(qreg_q_7_3[11])
circuit_7_3.p(pi / 2, qreg_q_7_3[12])
circuit_7_3.ry(pi / 2, qreg_q_7_3[13])
circuit_7_3.u(pi / 2, pi / 2, pi / 2, qreg_q_7_3[14])
circuit_7_3.s(qreg_q_7_3[0])
circuit_7_3.h(qreg_q_7_3[1])
circuit_7_3.h(qreg_q_7_3[2])
circuit_7_3.h(qreg_q_7_3[3])
circuit_7_3.h(qreg_q_7_3[4])
circuit_7_3.h(qreg_q_7_3[5])
circuit_7_3.h(qreg_q_7_3[6])
circuit_7_3.h(qreg_q_7_3[7])
circuit_7_3.h(qreg_q_7_3[8])
circuit_7_3.h(qreg_q_7_3[9])
circuit_7_3.h(qreg_q_7_3[10])
circuit_7_3.h(qreg_q_7_3[11])
circuit_7_3.h(qreg_q_7_3[12])
circuit_7_3.h(qreg_q_7_3[13])
circuit_7_3.h(qreg_q_7_3[14])
circuit_7_3.h(qreg_q_7_3[0])
circuit_7_3.tdg(qreg_q_7_3[3])
circuit_7_3.sdg(qreg_q_7_3[4])
circuit_7_3.rz(pi / 2, qreg_q_7_3[5])
circuit_7_3.sx(qreg_q_7_3[6])
circuit_7_3.sx(qreg_q_7_3[13])
circuit_7_3.y(qreg_q_7_3[14])
circuit_7_3.h(qreg_q_7_3[5])
circuit_7_3.h(qreg_q_7_3[13])
circuit_7_3.measure(qreg_q_7_3[0], creg_c_7_3[0])
circuit_7_3.measure(qreg_q_7_3[1], creg_c_7_3[1])
circuit_7_3.measure(qreg_q_7_3[2], creg_c_7_3[2])
circuit_7_3.measure(qreg_q_7_3[3], creg_c_7_3[3])
circuit_7_3.measure(qreg_q_7_3[4], creg_c_7_3[4])
circuit_7_3.measure(qreg_q_7_3[5], creg_c_7_3[5])
circuit_7_3.measure(qreg_q_7_3[6], creg_c_7_3[6])
circuit_7_3.measure(qreg_q_7_3[7], creg_c_7_3[7])
circuit_7_3.measure(qreg_q_7_3[8], creg_c_7_3[8])
circuit_7_3.measure(qreg_q_7_3[9], creg_c_7_3[9])
circuit_7_3.measure(qreg_q_7_3[10], creg_c_7_3[10])
circuit_7_3.measure(qreg_q_7_3[11], creg_c_7_3[11])
circuit_7_3.measure(qreg_q_7_3[12], creg_c_7_3[12])
circuit_7_3.measure(qreg_q_7_3[13], creg_c_7_3[13])
circuit_7_3.measure(qreg_q_7_3[14], creg_c_7_3[14])


# https://quantumcomputing.stackexchange.com/questions/13667/qiskit-get-gates-from-circuit-object

# for gate in circuit.data:
    # print('\ngate name:', gate[0].name)
    # print('qubit(s) acted on:', gate[1])
    # print('other paramters (such as angles):', gate[0].params)
    # print(gate)

# nr_of_qubits = circuit_6_3.num_qubits
# print(nr_of_qubits)

# send_to_kingdom('ibmq_lima', circuit_6_3)

# https://www.geeksforgeeks.org/number-of-ways-to-split-n-as-sum-of-k-numbers-from-the-given-range/
# Python3 implementation to count the
# number of ways to divide N in K
# groups such that each group
# has elements in range [L, R]
# mod = 1000000007
#
# # DP Table
# dp = [[-1 for j in range(1000)]
#       for i in range(1000)]
#
# # Function to count the number
# # of ways to divide the number N
# # in K groups such that each group
# # has number of elements in range [L, R]
# def calculate(pos, left, k, L, R):
#
#     # Base Case
#     if (pos == k):
#         if (left == 0):
#             return 1
#         else:
#             return 0
#
#     # if N is divides completely
#     # into less than k groups
#     if (left == 0):
#         return 0
#
#     # If the subproblem has been
#     # solved, use the value
#     if (dp[pos][left] != -1):
#         return dp[pos][left]
#
#     answer = 0
#
#     # put all possible values
#     # greater equal to prev
#     for i in range(L, R + 1):
#         if (i > left):
#             break
#
#         answer = (answer +
#                   calculate(pos + 1,
#                             left - i,
#                             k, L, R)) % mod
#
#     dp[pos][left] = answer
#
#     return answer
#
# # Function to count the number of
# # ways to divide the number N
# def countWaystoDivide(n, k, L, R):
#
#     return calculate(0, n, k, L, R)

# Driver code
# if __name__ == "__main__":
#     N = 12
#     K = 3
#     L = 1
#     R = 5
#
#     print(countWaystoDivide(N, K, L, R))

# This code is contributed by rutvik_56

# Aceasta e prima metoda care trebuie apelata in programul principal ca si operatie asupra unui circuit creat.
# Fiecare linie a matricii reprezinta un qubit, iar elementele unei linii reprezinta portile de pe qubitul respectiv.
def convert_circuit_to_matrix(circuit, L, R, gates_for_each_qubit):
    print("\nL = " + str(L))
    print("R = " + str(R))
    j = 0
    for gate in circuit.data:
        #     https://quantumcomputing.stackexchange.com/questions/13667/qiskit-get-gates-from-circuit-object
        qubit_acted_on = int(str(gate[1]).split("'),")[1].split(")]")[0])
        gate_name = gate[0].name
        # print('\ngate name:', gate_name)
        # print('qubit(s) acted on:')
        # print(qubit_acted_on)
        # Pentru a evita suprascrierea unei valori, astfel evitand disparitia unei porti,
        # se verifica daca exista un element deja pe pozitia selectata.
        if gates_for_each_qubit[qubit_acted_on][j] == "":
            gates_for_each_qubit[qubit_acted_on][j] = gate_name
        else:
            # Daca exista deja un element pe pozitia selectata, noua poarta/operatie este plasata pe pozitia urmatoare.
            gates_for_each_qubit[qubit_acted_on][j+1] = gate_name
        if qubit_acted_on == 14: # Nr de qubiti ai circuitului -1, daca am ajuns la ultimul qubit, pt ca numerotarea incepe de la 0.
            j = j+1

    print("Final gate list: ")
    i = 0
    for item in gates_for_each_qubit:
        print("Qubit", i, item)
        i = i + 1
        # print(item)
        # print()
    exit(0)

# def quantum_circuit_creator(original_circuit, number_of_qubits_to_be_taken):
    # print("-------------------------------")
    # print("\nQuantum circuit creator")
    # print("-------------------------------")
#     https://quantumcomputing.stackexchange.com/questions/13667/qiskit-get-gates-from-circuit-object
#     for gate in original_circuit.data:
#         print('\ngate name:', gate[0].name)
#         print('qubit(s) acted on:', gate[1])
#         print('other paramters (such as angles):', gate[0].params)
    # for nr in range(len(original_circuit.data)-1):
    # L = 0
    # R = number_of_qubits_to_be_taken
    # print("\nQubits for the new circuit: ")

    # print_circuit_range(original_circuit, L, R)

#     print(original_circuit.data)
#     print("-------------------------------")

def quantum_circuit_splitter(circuit, nr_of_qubits_per_part):
    # https://quantumcomputing.stackexchange.com/questions/17375/is-there-any-way-to-obtain-the-number-of-qubits-of-a-given-backend-in-qiskit
    nr_of_qubits = circuit.num_qubits # Acesta va fi numarul de qubiti disponibili aflat automat pentru fiecare calculator/simulator cuantic

    print("Number of qubits: " + str(nr_of_qubits))
    print("Number of qubits per part: " + str(nr_of_qubits_per_part))
    # print("Qubits: ")
    # print(circuit.qubits)
    print("Quantum circuit figure: ")
    print(circuit.draw())
    # exit(0)
    # print(countWaystoDivide(nr_of_qubits, 3, 1, 10))

    L = 0
    R = nr_of_qubits_per_part
    print("\nQubits for the new circuit: ")
    # https://www.geeksforgeeks.org/python-list-comprehension/
    # https://stackoverflow.com/questions/6376886/what-is-the-best-way-to-create-a-string-array-in-python
    # In loc de 15 se va pune automat nr de qubiti pentru numarul de linii.
    # Numarul de coloane poate fi mai mare, in functie de nr maxim de porti pe care vrea utilizatorul sa plaseze pe cate un qubit.
    gates_for_each_qubit = [["" for j in range(15)] for i in range(15)]
    convert_circuit_to_matrix(circuit, L, R, gates_for_each_qubit)

    while nr_of_qubits >= 0:
        if nr_of_qubits > 0:
            # quantum_circuit_creator(circuit, nr_of_qubits_per_part)
            convert_circuit_to_matrix(circuit, L, R, gates_for_each_qubit)

            nr_of_qubits = nr_of_qubits-nr_of_qubits_per_part # Numarul de qubiti ramasi din circuitul initial
            print("\nNumber of qubits left: " + str(nr_of_qubits))

            L = R + 1
            R = R + nr_of_qubits_per_part +1
            print("\nQubits for the new circuit: ")
            convert_circuit_to_matrix(circuit, L, R, gates_for_each_qubit)

        if nr_of_qubits == 0:
            # for gate in circuit.data:
            #     print('\ngate name:', gate[0].name)
            #     qubit_acted_on = int(str(gate[1]).split("'),")[1].split(")]")[0])
            #     print('qubit(s) acted on:')
            #     print(qubit_acted_on)
                # print('qubit(s) acted on:', str(gate[1]).split("'),")[1].split(")]")[0])
                # print('other paramters (such as angles):', gate[0].params)
            # print("Final gate list: ")
            # for item in gates_for_each_qubit:
            #     print(item)
            #     print()
            # print(circuit.draw())
            break



# https://github.com/dask/distributed/issues/2422
if __name__ == '__main__':
    # lc = LocalCluster()
    # lc.scale(10)
    # client = Client(lc)
    # future1 = client.submit(send_to_kingdom, 'ibmq_lima', circuit_6_3)
    # wait(future1)
    # future1.result()
    quantum_circuit_splitter(circuit_7_3, 5)





