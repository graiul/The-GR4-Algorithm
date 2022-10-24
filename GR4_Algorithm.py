import copy

from numpy import pi
from qiskit import QuantumRegister, ClassicalRegister, QuantumCircuit, execute
from qiskit.providers.ibmq import IBMQ
from distributed import Client, LocalCluster, Worker, wait, progress

class GR4_Algorithm(object):

    def __init__(self, quantum_circuit):
        self.circuit = quantum_circuit
        self.circuit_matrix = None

    def send_to_kingdom(self, quantum_backend_name, circuit_object):
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
    def convert_circuit_to_matrix(self, circuit_number_of_qubits):
        # https://www.geeksforgeeks.org/python-list-comprehension/
        # https://stackoverflow.com/questions/6376886/what-is-the-best-way-to-create-a-string-array-in-python
        # In loc de 15 se va pune automat nr de qubiti pentru numarul de linii.
        # Numarul de coloane poate fi mai mare, in functie de nr maxim de porti pe care vrea utilizatorul sa plaseze pe cate un qubit.
        gates_for_each_qubit = [["" for j in range(50)] for i in range(circuit_number_of_qubits)]
        j = 0
        for gate in self.circuit.data:
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
        self.circuit_matrix = copy.deepcopy(gates_for_each_qubit)

    def print_circuit_matrix_and_figure(self, ):
        print("\nQuantum circuit figure: ")
        print(self.circuit.draw())
        print("\nCircuit converted to matrix: ")
        i = 0
        for item in self.circuit_matrix:
            print("Qubit", i, item)
            i = i + 1
            # print(item)
            # print()
        # exit(0)

    # Aceasta metoda lucreaza cu matricea care a fost creata din circuitul cuantic.
    # Ea sterge partea extrasa din matricea originala a circuitului.
    # Astfel, qubitii care trebuie extrasi se afla intotdeauna la inceputul listei.
    # Acest lucru simplifica extragerea, efectuandu-se operatiunea de slice a listei folosind nr de qubiti disponibili ai echipamentului cuantic.
    # Matricea va fi segmentata in parti. Fiecare parte va avea un numarul de qubiti.
    # Acest numar este numarul de qubiti de care dispune calculatorul/simulatorul cuantic selectat.
    # Acest numar poate fi obtinut printr-o comanda qiskit:
    # https://quantumcomputing.stackexchange.com/questions/17375/is-there-any-way-to-obtain-the-number-of-qubits-of-a-given-backend-in-qiskit

    def quantum_circuit_matrix_part_getter(self, nr_of_qubits_per_part):
        # https://www.geeksforgeeks.org/python-list-slicing/
        part = self.circuit_matrix[0:nr_of_qubits_per_part]

        # Tutorial Dask Lock
        # https://www.youtube.com/watch?v=Q-Y3BR1u7c0&t=180s
        from dask.distributed import Lock
        lock = Lock()
        lock.acquire()
        # https://stackoverflow.com/questions/497426/deleting-multiple-elements-from-a-list
        del self.circuit_matrix[0:nr_of_qubits_per_part] # Aici trebuie paralelizat
        lock.release()

        print()
        for item in part:
            print(item)
        # self.print_circuit_matrix_and_figure()
        # exit(0)
        return part
        # print("Number of qubits: " + str(nr_of_qubits))
        # print("Number of qubits per part: " + str(nr_of_qubits_per_part))
        # print("Qubits: ")
        # print(circuit.qubits)
        #
        # L = 0
        # R = nr_of_qubits_per_part
        # print("\nQubits for the new circuit: ")
        #
        # while nr_of_qubits >= 0:
        #     if nr_of_qubits > 0:
        #         # quantum_circuit_creator(circuit, nr_of_qubits_per_part)
        #         convert_circuit_to_matrix(circuit, L, R, gates_for_each_qubit)
        #
        #         nr_of_qubits = nr_of_qubits-nr_of_qubits_per_part # Numarul de qubiti ramasi din circuitul initial
        #         print("\nNumber of qubits left: " + str(nr_of_qubits))
        #
        #         L = R + 1
        #         R = R + nr_of_qubits_per_part +1
        #         print("\nQubits for the new circuit: ")
        #         convert_circuit_to_matrix(circuit, L, R, gates_for_each_qubit)
        #
        #     if nr_of_qubits == 0:
        #         # for gate in circuit.data:
        #         #     print('\ngate name:', gate[0].name)
        #         #     qubit_acted_on = int(str(gate[1]).split("'),")[1].split(")]")[0])
        #         #     print('qubit(s) acted on:')
        #         #     print(qubit_acted_on)
        #             # print('qubit(s) acted on:', str(gate[1]).split("'),")[1].split(")]")[0])
        #             # print('other paramters (such as angles):', gate[0].params)
        #         # print("Final gate list: ")
        #         # for item in gates_for_each_qubit:
        #         #     print(item)
        #         #     print()
        #         # print(circuit.draw())
        #         break

    def quantum_circuit_creator(self, circuit_part):
        from numpy import pi # Am pus acest import aici pentru ca altfel Dask da eroare ca nu a fost definit 'pi'.

    #     print("-------------------------------")
    #     print("\nQuantum circuit creator")
        number_of_qubits_for_the_new_circuit = len(circuit_part)
        circuit_part_trimmed = []
        qreg = QuantumRegister(number_of_qubits_for_the_new_circuit, 'q')
        creg = ClassicalRegister(number_of_qubits_for_the_new_circuit, 'c')
        new_circuit = QuantumCircuit(qreg, creg)
        # https://stackoverflow.com/questions/522563/accessing-the-index-in-for-loops
        for i, qubit in enumerate(circuit_part):
            index_for_trimming = qubit.index('measure')
            # print(index_for_trimming)
            # print(type(qubit))
            qubit_trimmed = qubit[:index_for_trimming + 1]
            # circuit_part_trimmed.append(qubit_trimmed)
            # https://stackoverflow.com/questions/701802/how-do-i-execute-a-string-containing-python-code-in-python
            for gate in qubit_trimmed:
                # print(gate)
                # !!! Aici trebuie adaugate mai multe porti.
                if gate != 'measure':
                    if gate == 'reset' or gate == 'h' or \
                            gate == 'z' or gate == 'y' or \
                            gate == 'sdg' or gate == 'tdg' or \
                            gate == 't' or gate == 'sx' or \
                            gate == 's':
                        exec("new_circuit." + str(gate) + "(qreg[" + str(i) + "])")
                    if gate == 'rx' or gate == 'ry' or\
                            gate == 'p' or gate == 'rz':
                        # !!! Aici trebuie obtinuta faza din circuitul original,
                        # la convertirea lui in matrice, pt ca nu va fi tot timpul pi/2
                        # print("new_circuit." + str(gate) + "(pi/2, qreg[" + str(i) + "])")
                        exec("new_circuit." + str(gate) + "(pi/2, qreg[" + str(i) + "])")
                    elif gate == 'u':
                        exec("new_circuit." + str(gate) + "(pi / 2, pi / 2, pi / 2, qreg[" + str(i) + "])")
                # else:
                #     exec("new_circuit." + str(gate) + "(qreg[" + str(i) + "])")
                if gate == 'measure':
                    exec("new_circuit.measure" + "(qreg[" + str(i) + "], creg[" + str(i) + "])")
        return new_circuit
        # for item in circuit_part_trimmed:
        #     print(circuit_part_trimmed)




            # for gate in qubit:
            #     print(gate)
    #     print("-------------------------------")
    #     https://quantumcomputing.stackexchange.com/questions/13667/qiskit-get-gates-from-circuit-object
    #     for gate in original_circuit.data:
    #         print('\ngate name:', gate[0].name)
    #         print('qubit(s) acted on:', gate[1])
    #         print('other paramters (such as angles):', gate[0].params)
    #     for nr in range(len(original_circuit.data)-1):
    #     L = 0
    #     R = number_of_qubits_to_be_taken
    #     print("\nQubits for the new circuit: ")
    #
    #     print_circuit_range(original_circuit, L, R)
    #
    #     print(original_circuit.data)
    #     print("-------------------------------")

    # Va fi apelat pe fiecare proces Dask
    def send_to_kingdom(self, quantum_backend_name, circuit_object):
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
        # print("\nTotal count for 00, 01, 10 and 11 are:",counts)
        print("\nTotal counts:",counts)

    def obtain_quantum_backend_number_of_qubits(self, quantum_backend_name):
        # IBMQ.save_account('e6bbad0f51ab787aec48bed242c422777f1680f0428e19b34e19bbcd467a2faff2bdcedd0cbb04b19f4bb700f66900728f778d4bc8226785e6c35dc818374ac8',
        #                   overwrite=True)
        provider = IBMQ.load_account()
        backend = provider.get_backend(quantum_backend_name)
        backend_number_of_qubits = backend.configuration().n_qubits
        return backend_number_of_qubits


# https://github.com/dask/distributed/issues/2422
if __name__ == '__main__':
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

    # 25 qubit circuit
    qreg_q_25 = QuantumRegister(25, 'q')
    creg_c_25 = ClassicalRegister(25, 'c')
    circuit_25 = QuantumCircuit(qreg_q_25, creg_c_25)
    for i in range(0, 25):
        # print(i)
        circuit_25.reset(qreg_q_25[i])
        circuit_25.h(qreg_q_25[i])
    circuit_25.cx(qreg_q_25[0], qreg_q_25[1])
    circuit_25.rz(pi / 2, qreg_q_25[2])
    circuit_25.h(qreg_q_25[0])
    circuit_25.barrier(qreg_q_25[1])
    circuit_25.y(qreg_q_25[0])
    circuit_25.ch(qreg_q_25[2], qreg_q_25[1])
    circuit_25.y(qreg_q_25[1])
    circuit_25.y(qreg_q_25[2])
    circuit_25.z(qreg_q_25[3])
    circuit_25.p(pi / 2, qreg_q_25[4])
    circuit_25.ry(pi / 2, qreg_q_25[5])
    circuit_25.u(pi / 2, pi / 2, pi / 2, qreg_q_25[6])
    circuit_25.y(qreg_q_25[3])
    circuit_25.y(qreg_q_25[4])
    circuit_25.y(qreg_q_25[5])
    circuit_25.y(qreg_q_25[6])
    circuit_25.h(qreg_q_25[3])
    circuit_25.h(qreg_q_25[4])
    circuit_25.h(qreg_q_25[5])
    circuit_25.h(qreg_q_25[6])
    circuit_25.rz(pi / 2, qreg_q_25[3])
    circuit_25.sdg(qreg_q_25[4])
    circuit_25.t(qreg_q_25[5])
    circuit_25.s(qreg_q_25[6])
    circuit_25.h(qreg_q_25[3])
    circuit_25.h(qreg_q_25[4])
    circuit_25.h(qreg_q_25[5])
    circuit_25.h(qreg_q_25[6])
    circuit_25.z(qreg_q_25[7])
    circuit_25.sx(qreg_q_25[8])
    circuit_25.p(pi / 2, qreg_q_25[9])
    circuit_25.rz(pi / 2, qreg_q_25[10])
    circuit_25.y(qreg_q_25[7])
    circuit_25.y(qreg_q_25[8])
    circuit_25.y(qreg_q_25[9])
    circuit_25.y(qreg_q_25[10])
    circuit_25.h(qreg_q_25[7])
    circuit_25.h(qreg_q_25[8])
    circuit_25.h(qreg_q_25[9])
    circuit_25.h(qreg_q_25[10])
    circuit_25.t(qreg_q_25[7])
    circuit_25.z(qreg_q_25[8])
    circuit_25.sxdg(qreg_q_25[9])
    circuit_25.rx(pi / 2, qreg_q_25[10])
    circuit_25.x(qreg_q_25[11])
    circuit_25.cx(qreg_q_25[12], qreg_q_25[13])
    circuit_25.ccx(qreg_q_25[11], qreg_q_25[12], qreg_q_25[13])
    circuit_25.swap(qreg_q_25[11], qreg_q_25[12])
    circuit_25.id(qreg_q_25[13])
    circuit_25.t(qreg_q_25[11])
    circuit_25.s(qreg_q_25[12])
    circuit_25.z(qreg_q_25[13])
    circuit_25.tdg(qreg_q_25[11])
    circuit_25.sdg(qreg_q_25[12])
    circuit_25.p(pi / 2, qreg_q_25[13])
    circuit_25.h(qreg_q_25[11])
    circuit_25.y(qreg_q_25[11])
    circuit_25.rx(pi / 2, qreg_q_25[14])
    circuit_25.u(pi / 2, pi / 2, pi / 2, qreg_q_25[16])
    circuit_25.swap(qreg_q_25[14], qreg_q_25[15])
    circuit_25.rz(pi / 2, qreg_q_25[16])
    circuit_25.s(qreg_q_25[14])
    circuit_25.y(qreg_q_25[16])
    circuit_25.cx(qreg_q_25[14], qreg_q_25[15])
    circuit_25.ry(pi / 2, qreg_q_25[14])
    circuit_25.sx(qreg_q_25[15])
    circuit_25.z(qreg_q_25[14])
    circuit_25.s(qreg_q_25[15])
    circuit_25.y(qreg_q_25[14])
    circuit_25.y(qreg_q_25[15])
    circuit_25.cx(qreg_q_25[17], qreg_q_25[18])
    circuit_25.y(qreg_q_25[18])
    circuit_25.y(qreg_q_25[18])
    circuit_25.y(qreg_q_25[18])
    circuit_25.ccx(qreg_q_25[17], qreg_q_25[18], qreg_q_25[19])
    circuit_25.h(qreg_q_25[17])
    circuit_25.h(qreg_q_25[19])
    circuit_25.sx(qreg_q_25[20])
    circuit_25.rz(pi / 2, qreg_q_25[21])
    circuit_25.s(qreg_q_25[22])
    circuit_25.h(qreg_q_25[20])
    circuit_25.rz(pi / 2, qreg_q_25[22])
    circuit_25.rx(pi / 2, qreg_q_25[20])
    circuit_25.ccx(qreg_q_25[20], qreg_q_25[21], qreg_q_25[22])
    circuit_25.h(qreg_q_25[20])
    circuit_25.p(pi / 2, qreg_q_25[21])
    circuit_25.sdg(qreg_q_25[22])
    circuit_25.ry(pi / 2, qreg_q_25[21])
    circuit_25.y(qreg_q_25[21])
    circuit_25.id(qreg_q_25[23])
    circuit_25.t(qreg_q_25[23])
    circuit_25.rx(pi / 2, qreg_q_25[23])
    circuit_25.y(qreg_q_25[23])
    circuit_25.t(qreg_q_25[24])
    circuit_25.u(pi / 2, pi / 2, pi / 2, qreg_q_25[24])
    circuit_25.y(qreg_q_25[24])
    for i in range(0, 25):
        circuit_25.measure(qreg_q_25[i], creg_c_25[i])

    # Aici valoarea lui fold poate pagina afisarea circuitului
    # in consola astfel incat sa nu fie prea lat
    print(circuit_25.draw(fold=-1))
    exit(0)

    # Fake backends for easy testing.
    # https://quantumcomputing.stackexchange.com/questions/17375/is-there-any-way-to-obtain-the-number-of-qubits-of-a-given-backend-in-qiskit
    # from qiskit.test.mock import FakeProvider
    # provider = FakeProvider()
    # backends = provider.backends()
    # backend_1 = provider.get_backend('fake_belem')
    # backend_2 = provider.get_backend('fake_lima')
    # backend_3 = provider.get_backend('fake_quito')
    # backend_name_1 = backend_1.name()
    # backend_name_2 = backend_2.name()
    # backend_name_3 = backend_3.name()
    # backend_1_number_of_qubits = backend_1.configuration().n_qubits
    # backend_2_number_of_qubits = backend_2.configuration().n_qubits
    # backend_3_number_of_qubits = backend_3.configuration().n_qubits
    #
    # print(backends)
    # print("Backend name:", backend_name_1, ". It has a capacity of", backend_1_number_of_qubits, "qubits.")
    # print("Backend name:", backend_name_2, ". It has a capacity of", backend_2_number_of_qubits, "qubits.")
    # print("Backend name:", backend_name_3, ". It has a capacity of", backend_3_number_of_qubits, "qubits.")

    # exit(0)

    # Se initializeaza algoritmul GR4
    gr4 = GR4_Algorithm(circuit_7_3)

    nr_of_qubits = circuit_7_3.num_qubits
    circuit_converted_to_matrix = copy.deepcopy(gr4.convert_circuit_to_matrix(nr_of_qubits))
    gr4.print_circuit_matrix_and_figure()
    # exit(0)

    # Primul parametru este matricea aferenta circuitului.
    # Al doilea parametru este numarul de qubiti de care dispune fiecare echipament.
    # Va fi extras din matrice un numar de qubiti egal cu cel de mai sus.
    # circuit_part_1 = gr4.quantum_circuit_matrix_part_getter(backend_1_number_of_qubits)
    # new_circuit_1 = gr4.quantum_circuit_creator(circuit_part_1)
    # print(new_circuit_1.draw())
    # circuit_part_2 = gr4.quantum_circuit_matrix_part_getter(backend_2_number_of_qubits)
    # new_circuit_2 = gr4.quantum_circuit_creator(circuit_part_2)
    # print(new_circuit_2.draw())
    # circuit_part_3 = gr4.quantum_circuit_matrix_part_getter(backend_3_number_of_qubits)
    # new_circuit_3 = gr4.quantum_circuit_creator(circuit_part_3)
    # print(new_circuit_3.draw())

    # IDEE: partitionarea matricei circuitului sa fie facuta de DASK si apoi comparat cu varianta mea de partitionare.
    # De efectuat apoi teste cu cele doua proceduri (Dask si Radu) atat la calculatoare cuantice cat si la simulatoare cuantice.


    lc = LocalCluster()
    lc.scale(10)
    client = Client(lc)
    future1 = client.submit(gr4.quantum_circuit_creator, gr4.quantum_circuit_matrix_part_getter(gr4.obtain_quantum_backend_number_of_qubits('ibmq_belem')))
    # wait(future1)
    # circuit_part_1 = future1.result()
    future2 = client.submit(gr4.quantum_circuit_creator, gr4.quantum_circuit_matrix_part_getter(gr4.obtain_quantum_backend_number_of_qubits('ibmq_lima')))
    # wait(future2)
    # new_circuit_1 = future2.result()
    future3 = client.submit(gr4.quantum_circuit_creator, gr4.quantum_circuit_matrix_part_getter(gr4.obtain_quantum_backend_number_of_qubits('ibmq_quito')))
    rez1 = future1.result()
    rez2 = future2.result()
    rez3 = future3.result()
    print(rez1.draw())
    print(rez2.draw())
    print(rez3.draw())

    print("IBM: ")
    # backend1 = provider.get_backend('ibmq_belem')
    # backend2 = provider.get_backend('ibmq_lima')
    # backend3 = provider.get_backend('ibmq_quito')
    future1 = client.submit(gr4.send_to_kingdom, 'ibmq_belem', rez1)
    # wait(future1)
    future2 = client.submit(gr4.send_to_kingdom, 'ibmq_lima', rez2)
    future3 = client.submit(gr4.send_to_kingdom, 'ibmq_quito', rez3)
    wait([future1, future2, future3])





