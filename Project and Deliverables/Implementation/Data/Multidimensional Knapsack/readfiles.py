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

    

print('constant term and QUBO matrix representing the cost (unconstrained objective) function' )
print(obj_constant, obj_qubo)
print('constant term and QUBO matrix representing the constraint function' )
print(con_constant, con_qubo)



######## QUBO you need to solve ########
penalty = util.verma_penalty(obj_qubo)
print('penalty', penalty)
#QUBO matrix 
Q = -1*obj_qubo + penalty * con_qubo
#constant term
c = -1*obj_constant+ penalty * con_constant


#evaluate a random solution
x = np.array([np.random.randint(2) for i in range(len(Q))])
print(x)

#example of how to estimate the energy (objective function) and the constraint function seperately, useful if you want to test that your solution is feasible
#x^TQx + c
obj = x.transpose().dot(obj_qubo).dot(x) + obj_constant
con = x.transpose().dot(con_qubo).dot(x) + con_constant

print('The objective function of x is ',obj )
print('The constraint function of x is ',con )
