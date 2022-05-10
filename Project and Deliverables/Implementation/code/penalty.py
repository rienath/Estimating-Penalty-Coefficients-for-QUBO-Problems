import numpy as np

class PenaltyAlgorithm:
    """Models a penalty estimation algorithm.
    
    Attributes
    ----------
    algorithm : str
        Name of the panalty algorithm to be used.

    Raises
    ------
    ValueError
        If the entered algorithm does not exist.
    
    """
    
    ALGORITHMS = ['Verma&Lewis', 'Monotone', 'Expected Constraint', 'Minimum Lazy', 'Verma&Lewis check']

    def __new__(cls, algorithm):
        # Only proceed if the algorithm provided is in the list of
        # allowed algorithms. Otherwise, display an error
        if algorithm in cls.ALGORITHMS:
            return super(PenaltyAlgorithm, cls).__new__(cls)
        raise ValueError(f'Only the following algorithms are permitted: {cls.ALGORITHMS}')

    def __init__(self, algorithm):
        self.algorithm = algorithm

    def generate_penalties(self, obj_qubos, con_qubos=None, monotone_value=None):
        """Generates penalty coefficients for the provided objective 
        and optionally constraint QUBOs.

        Parameters
        ----------
        obj_qubos : list
            The objective function QUBOs that we want to generate M for.
        con_qubos : list, optional
            The constraint function QUBOs that we want to generate M for.
        monotone_value : int, optional
            A constant that Monotone algorithms will always return.

        Returns
        -------
        list
            The numpy.float64 penalty coefficients estimated for the provided QUBOs.

        Raises
        ------
        TypeError
            If monotone_value was not provided when using Monotone algorithms.
        
        """
        # Match input penalty algorithm name to the actual algorithm
        match self.algorithm:
            case 'Verma&Lewis':
                return self.__verma_and_lewis(obj_qubos)
            case 'Monotone':
                if monotone_value is None:  # Demand value argument
                    raise TypeError(
                        "PenaltyAlgorithm.generate_penalties() with Monotone algorithm requires 'monotone_value' "
                        "argument")
                return self.__monotone(monotone_value)
            case 'Expected Constraint':
                return self.__expected_constraint(obj_qubos, con_qubos)
            case 'Minimum Lazy':
                return self.__minimum_lazy(obj_qubos, con_qubos)
            case 'Verma&Lewis check':
                return self.__verma_and_lewis_check(obj_qubos)

    @staticmethod
    def __verma_and_lewis(obj_qubos):
        """Generate M using the Verma and Lewis algorithm.

        Parameters
        ----------
        obj_qubos : numpy.ndarray
            The objective function QUBO.

        Returns
        -------
        numpy.float64
            The penalty coefficient estimate for the provided objective QUBO.

        :Authors:
            Dr Mayowa Ayodele
            Raufs Dunamalijevs
        
        """
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
    def __verma_and_lewis_check(obj_qubos):
        """Generate M using the Reality Check algorithm.

        Parameters
        ----------
        obj_qubos : numpy.ndarray
            The objective function QUBO.

        Returns
        -------
        numpy.float64
            The penalty coefficient estimate for the provided objective QUBO.
        
        """
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
        return  -1*(-1*max(weights)//2) #Ceiling division to make sure we do not get 0

    @staticmethod
    def __monotone(monotone_value):
        """Generate M using the Monotone algorithm.

        Parameters
        ----------
        monotone_value : int or float
            The value that we always want to return as an M.

        Returns
        -------
        numpy.float64
            The penalty coefficient equal to the monotone value provided.
        
        """
        return monotone_value

    @staticmethod
    def __expected_constraint(obj_qubos, con_qubos):
        """Generate M using the Expected Constraint algorithm.

        Parameters
        ----------
        obj_qubos : numpy.ndarray
            The objective function QUBO.
        con_qubos : numpy.ndarray
            The constraint function QUBO.

        Returns
        -------
        numpy.float64
            The penalty coefficient estimate for the provided objective and constraint QUBOs.
        
        """
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
        obj = max(weights)

        # This is the additional part to Verma and Lewis method.
        # We go through every variable and calculate the penalty it would cause if
        # every variable it has interacted with was 1, but dividing quadratic coefficients by 2 as
        # we will calculate them twice. We do it with every single variable and then divide them
        # by the total number of variables and sum everything up. This is how we calculate the
        # 'expected' penalty magnitude that breaking a single constraint will bring.
        # This entire operation is equivalent to summing all variables in constraint QUBO
        # and dividing the resultant number by it's length.
        con = sum(map(sum, con_qubos)) / len(con_qubos)
        con = abs(con)  # Take the magnitude to avoid negative M

        # Since we are finding estimates that are likely to be higher than the actual solution,
        # we will only be further increasing the difference by taking a square.
        # We would rather have a number that is smaller than the actual solution as any smaller number
        # will likely produce a coefficient estimate that is more accurate than Verma and Lewis,
        # but unnecessarily large values of denominator can damage the solution process as they will
        # drive M to be smaller therefore making breaking constraints not important. That is why instead
        # of square, we take abs
        return -1*(-1*obj//con) #Ceiling division to make sure we do not get 0

    @staticmethod
    def __minimum_lazy(obj_qubos, con_qubos):
        """Generate M using the Minimum Lazy algorithm.

        Parameters
        ----------
        obj_qubos : numpy.ndarray
            The objective function QUBO.
        con_qubos : numpy.ndarray
            The constraint function QUBO.

        Returns
        -------
        numpy.float64
            The penalty coefficient estimate for the provided objective and constraint QUBOs.
        
        """
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
        obj = max(weights)

        # Go through every QUBO row (every binary variable) and count the penalty that it causes
        weights = np.zeros(shape=(len(con_qubos) * 2), dtype='int64')
        k = 0
        for i in range(len(con_qubos)):
            weights[k] = con_qubos[i][i]
            for j in range(len(con_qubos)):
                if i != j:
                    # Multiply by 2 as the symmetric QUBO has half coefficients in quadratic positions
                    weights[k] += 2 * con_qubos[i][j]
            k = k + 1
        # Divide the weights by the number of values that we have as we 'expect'
        # that every variable will bring 1/max penalty to the mix
        weights = abs(weights)
        weights = weights[weights > 0]
        con = min(weights)
        return -1 * (-1 * obj // con)  # Ceiling division to make sure we do not get 0
