import numpy as np

class util:
    def verma_penalty(qubo_obj):
        weights = np.zeros(shape = (len(qubo_obj) * 2), dtype='int64')
        k = 0
        for i in range(len(qubo_obj)):
            weights[k]= qubo_obj[i][i]
            weights[k+1]= -qubo_obj[i][i]
            for j in range(len(qubo_obj)):
                if(i!=j):
                    if(qubo_obj[i][j] > 0):
                        weights[k]+= qubo_obj[i][j]
                    else:
                        weights[k+1]-=qubo_obj[i][j]
            k = k+2
        return max(weights)

    
    def convert_QUBO_to_dwave_format(Q):
        newQ = {}
        for i in range(len(Q)):
            newQ[tuple([i,i])] = Q[i][i]

        for i in range(len(Q)):
            for j in range(i+1, len(Q)):
                newQ[tuple([i,j])] = Q[i][j]
        return(newQ)
        