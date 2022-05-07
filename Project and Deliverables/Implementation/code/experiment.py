import numpy as np
from penalty import PenaltyAlgorithm
from IPython.display import clear_output


class Experiment:
    """
    
    """

    @staticmethod
    def __convert_1d_qubo_to_2d(qubo, n):
        """

        Parameters
        ----------
        qubo : type
            Explanation
        n : type
            Explanation

        Returns
        -------
        type
            Explanation

        :Author:
            Dr Mayowa Ayodele
        
        """
        if len(qubo) != n * ((n + 1) * 0.5) + 1:
            print('check that n is the correct size')
            return None, None
        constant = qubo[0]
        linear_terms = np.array(qubo[1:(n + 1)])
        no_of_quadratic_terms = len(qubo) - len(linear_terms) - 1
        quadratic_terms = np.array(qubo[-no_of_quadratic_terms:])
        k = 0
        qubo_coefs = []
        for i in range(n):
            coefs = []
            for j in range(n):
                if i == j:
                    coefs.append(linear_terms[i])
                elif j > i:
                    coefs.append(quadratic_terms[k])
                    k += 1
                else:
                    coefs.append(0)
            qubo_coefs.append(coefs)
        qubo_coefs = np.array(qubo_coefs)

        return qubo_coefs, constant

    @staticmethod
    def __convert_qubo_to_dwave_format(q):
        """

        Parameters
        ----------
        q : type
            Explanation

        Returns
        -------
        type
            Explanation

        :Author:
            Dr Mayowa Ayodele
        
        """
        new_q = {}
        for i in range(len(q)):
            new_q[tuple([i, i])] = q[i][i]

        for i in range(len(q)):
            for j in range(i + 1, len(q)):
                new_q[tuple([i, j])] = q[i][j]
        return new_q

    # Kwargs are for the penalty algorithms
    # Light version of data prep. Can be applied when objective and constraint function QUBOs have already been
    # formulated.
    @classmethod
    def data_prep_light(cls, obj_qubos, con_qubos, penalty_algorithm_name, minimisation, **kwargs):
        """

        Parameters
        ----------
        obj_qubos : type
            Explanation
        con_qubos : type
            Explanation
        penalty_alorithm_name : type
            Explanation
        minimisation : type
            Explanation
        **kwargs, optional
            Explanation

        Returns
        -------
        type
            Explanation
            
        """
        # Calculate penalties
        penalty_algorithm = PenaltyAlgorithm(penalty_algorithm_name)
        if con_qubos:
            penalties = [penalty_algorithm.generate_penalties(i, j, **kwargs) for (i, j) in zip(obj_qubos, con_qubos)]
        else:
            penalties = [penalty_algorithm.generate_penalties(i, **kwargs) for i in obj_qubos]
        # If we are solving maximization problem, we will need to convert it to
        # minimisation by multiplying the objective function by -1
        coef = 1 if minimisation else -1
        # QUBO matrix with constraints (no constants)
        qs = [coef * obj_qubo + penalty * con_qubo for obj_qubo, penalty, con_qubo in
              zip(obj_qubos, penalties, con_qubos)]
        # Change QUBO matrix to the dwave format
        qs = [cls.__convert_qubo_to_dwave_format(q) for q in qs]
        return qs, penalties

    # Kwargs are for the penalty algorithms

    @classmethod
    def data_prep(cls, qubo_sizes, objectives, constraints, penalty_algorithm_name, minimisation, **kwargs):
        """

        Parameters
        ----------
        qubo_sizes : type
            Explanation
        objectives : type
            Explanation
        constraints : type
            Explanation
        penalty_algorithm_name : type
            Explanation
        minimisation : type
            Explanation
        **kwargs, optional
            Explanation

        Returns
        -------
        type
            Explanation
                
        """
        # Get the unconstrained objective function and the constraint function with constants
        obj_qubos, obj_constants, con_qubos, con_constants = [], [], [], []
        for i in range(len(qubo_sizes)):
            # Unconstrained objective function
            obj = cls.__convert_1d_qubo_to_2d(objectives[i], qubo_sizes[i])
            obj_qubos.append(obj[0])
            obj_constants.append(obj[1])
            # Constraint function
            const = cls.__convert_1d_qubo_to_2d(constraints[i], qubo_sizes[i])
            con_qubos.append(const[0])
            con_constants.append(const[1])
        # Make full QUBOs and generate penalty coefficients
        qs, penalties = cls.data_prep_light(obj_qubos, con_qubos, penalty_algorithm_name, minimisation, **kwargs)

        return qs, penalties, obj_qubos, obj_constants, con_qubos, con_constants

    @staticmethod
    def run_sampler(qs, obj_qubos, obj_constants, con_qubos, con_constants, sampler, repeats, **kwargs):
        """

        Parameters
        ----------
        qs : type
            Explanation
        obj_qubos : type
            Explanation
        obj_constants : type
            Explanation
        con_qubos : type
            Explanation
        con_constants : type
            Explanation
        sampler : type
            Explanation
        repeats : type
            Explanation
        **kwargs, optional
            Explanation
        
        Returns
        -------
        type
            Explanation
        
        """
        # Format {seed : [objective_energies, constraint_energies]}
        runs = {}
        # Solve every QUBO n times with a different seed to simulate different runs.
        # Start with 1 as simulated annealing breaks with 0.
        for seed in range(1, repeats + 1):
            clear_output(wait=True)
            # Solve every QUBO
            objs, cons = [], []
            for problem_num in range(len(qs)):
                response = sampler.sample_qubo(qs[problem_num], seed=seed, **kwargs)

                # If we want to see more details
                # print("samples=" + str(list(response.samples())))
                # print("energies=" + str(list(response.data_vectors['energy'])) )

                # Choose solution with the lowest energy
                solution = list(response.lowest())[0]
                y = np.array([int(solution[i]) for i in range(len(solution))])

                # Even though we have multiplied the objective function by -1 to
                # transfer it to minimisation problem when defining a QUBO if it was maximisation,
                # we do not need to multiply it by -1 again as we are using the original
                # unmultipled objective function here.
                # So here we will have the original objective function value
                obj = y.transpose().dot(obj_qubos[problem_num]).dot(y) + obj_constants[problem_num]
                # The constraint function before multiplying it by penalty coefficient
                con = y.transpose().dot(con_qubos[problem_num]).dot(y) + con_constants[problem_num]

                objs.append(obj)
                cons.append(con)

            runs[seed] = (objs, cons)
            print(np.round(seed / repeats * 100, 2), '%')

        return runs
