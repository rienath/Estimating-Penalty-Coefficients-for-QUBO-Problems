## Description
Great explanation why penalty optimization is meaningful:

_"We explain the intuition behind the observation as follows. As one increases the relaxation parameter value, the constraints, in the form of penalty, gradually dominates the QUBO objective. Thus, A QUBO solver will be more likely to find feasible solutions. Meanwhile, the part of the QUBO objective corresponding to the original objective becomes less prominent and sometimes even disappears. The QUBO solver will not be able to respond to the tiny difference presented by the objective part and fails to find (near-)optimal solutions. 1 On the other hand, if one decreases the relaxation parameter over a certain threshold, i.e., to the left part of the dip, there will be fewer feasible solutions, and therefore fewer chances for the QUBO solver to find a solution with a smaller fitness value."_

Also proposes a machine learning algorithm that predicts good penalties based on past penalties:

_"QROSS, a machine learning method to extract knowledge from QUBO problem instances solved in the past to facilitate the relaxation parameter optimisation process for a new instance of the same problem."_

## Link
https://arxiv.org/pdf/2103.10695v1.pdf

#paper #penalties #digital-annealer