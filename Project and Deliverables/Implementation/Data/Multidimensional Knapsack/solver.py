import numpy as np
from util import *
from dwave_qbsolv import QBSolv
import neal
from tabu import TabuSampler

#file_path = 'Weing//WEING8.npz'
file_path = 'weish//weish01.npz'
loaded_file = np.load(file_path)
qubo_size = loaded_file['n']
objective = loaded_file['objective']
constraint = loaded_file['constraint']


def convert_1d_qubo_to_2d(qubo, n):
    if (len(qubo)!= (n) * ((n+1) * 0.5)   + 1):
        print('check that n is the correct size')
        return None, None
    constant = qubo[0]
    linear_terms = np.array(qubo[1:(n + 1)])
    no_of_quadratic_terms = len(qubo) - len(linear_terms) -1
    quadratic_terms = np.array(qubo[-no_of_quadratic_terms:])
    k = 0
    qubo_coeffs = []
    for i in range(n):
        coeffs = []
        for j in range(n):
            if(i == j):
                coeffs.append(linear_terms[i])
            elif(j>i):
                coeffs.append(quadratic_terms[k])
                k+=1
            else:
                coeffs.append(0)
        qubo_coeffs.append(coeffs)
    qubo_coeffs = np.array(qubo_coeffs)

    return qubo_coeffs, constant
    
    
    
obj_qubo, obj_constant = convert_1d_qubo_to_2d(objective, qubo_size)

con_qubo,con_constant = convert_1d_qubo_to_2d(constraint, qubo_size)



######## QUBO you need to solve ########
penalty = util.verma_penalty(obj_qubo)
print('penalty', penalty)
#QUBO matrix 
Q = -1*obj_qubo + penalty * con_qubo
#constant term
c = -1*obj_constant+ penalty * con_constant

#example of solving the problem with QBsolve

#change QUBO matrix to the QBSolve format
newQ = util.convert_QUBO_to_dwave_format(Q)



#run solver, need to pip install dwave_qbsolv

sampler = neal.SimulatedAnnealingSampler()
#to use the tabu sampler, need to pip install dwave_tabu
#sampler = TabuSampler()
response = QBSolv().sample_qubo(newQ, solver=sampler, find_max = False)

#response = TabuSampler().sample_qubo(newQ)

print("samples=" + str(list(response.samples())))
print("energies=" + str(list(response.data_vectors['energy'])) )

solution = list(response.samples())[-1]

y = np.array([int(solution[i]) for i in range(len(solution))])
print(y)

obj = y.transpose().dot(obj_qubo).dot(y) + obj_constant
con = y.transpose().dot(con_qubo).dot(y) + con_constant

print('The objective function value of x is ',obj )
print('The constraint function value of x is ',con )