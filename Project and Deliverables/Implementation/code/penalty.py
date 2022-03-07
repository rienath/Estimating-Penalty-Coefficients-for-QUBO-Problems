import numpy as np


class PenaltyAlgorithm:
    ALGORITHMS = ['Verma&Lewis', 'Monotone']

    def __new__(cls, algorithm):
        # Only proceed if the algorithm provided is in the list of
        # allowed algorithms. Otherwise, display an error
        if algorithm in cls.ALGORITHMS:
            return super(PenaltyAlgorithm, cls).__new__(cls)
        raise ValueError(f'Only the following algorithms are permitted: {cls.ALGORITHMS}')

    def __init__(self, algorithm):
        self.algorithm = algorithm

    def generate_penalties(self, obj_qubos, con_qubos=None, monotone_value=None):
        match self.algorithm:
            case 'Verma&Lewis':
                return self.__verma_and_lewis(obj_qubos)
            case 'Monotone':
                if monotone_value is None:  # Demand value argument
                    raise TypeError(
                        "PenaltyAlgorithm.generate_penalties() with Monotone algorithm requires 'monotone_value' "
                        "argument")
                return self.__monotone(monotone_value)

    @staticmethod
    def __verma_and_lewis(obj_qubos):
        weights = np.zeros(shape=(len(obj_qubos) * 2), dtype='int64')
        k = 0
        for i in range(len(obj_qubos)):
            weights[k] = obj_qubos[i][i]
            weights[k + 1] = -obj_qubos[i][i]
            for j in range(len(obj_qubos)):
                if i != j:
                    # Multiply by 2 as the symmetric QUBO has half coefficients in quadratic positions
                    if obj_qubos[i][j] > 0:
                        weights[k] += 2 * obj_qubos[i][j]
                    else:
                        weights[k + 1] -= 2 * obj_qubos[i][j]
            k = k + 2
        return max(weights)

    @staticmethod
    def __monotone(monotone_value):
        return monotone_value
