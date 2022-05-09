from IPython.display import display_html
from itertools import chain, cycle
import pandas as pd
from scipy import stats

class Table:
    """A collection of methods related to producing tables.

    """
    
    @staticmethod
    def display_side_by_side(*args, titles=cycle([''])):
        """Display multiple tables next to one another.

        Parameters
        ----------
        *args : pandas.core.frame.DataFrame
            DataFrames to be displaye.
        titles : list
            DataFrame titles.
        
        """
        
        html_str = ''
        for df, title in zip(args, chain(titles, cycle(['</br>']))):
            html_str += '<th style="text-align:center"><td style="vertical-align:top">'
            html_str += f'<h2 style="text-align:left">{title}</h2>'
            html_str += df.to_html().replace('table', 'table style="display:inline"')
            html_str += '</td></th>'
        display_html(html_str, raw=True)

    @staticmethod
    def record_results(runs, qubo_sizes, penalties, repeats, minimization=False):
        """Records the results of an experiment straight out the solver in a series of tables.

        Parameters
        ----------
        runs : dict
            The objective and constraint function values of every solution from every repeat 
            in the following format: {repeat: [objective values], [constraint values]}. 
            Experiment.run_sampler(...).
        qubo_sizes : list
            Sizes of the solved QUBOs.
        penalties : list
            Penalty coefficients estimated for QUBOs. 
        repeats : int
            Number of times we have solved the same problems.
        minimization : bool, optional
            Whether the problem is a minimisation.
            
        Returns
        -------
        list
            A list of DataFrames each containing information about produced solutions in an individual repeat.
        
        """
        
        coef = 1 if minimization else -1
        results = []
        # 1: QUBO size, 2: calculated penalty coefficient, 3: objective function energy
        # 4: number of broken constraints,
        # 5: total QUBO energy (if transferring maximisation problem to minimisation,
        # we need to take the negative).
        # Total energy should be negative if no constraints were broken.
        for i in range(1, repeats + 1):
            energies = [coef * obj + con * penalty for obj, con, penalty in zip(runs[i][0], runs[i][1], penalties)]
            results.append(pd.DataFrame({'Size': qubo_sizes,
                                         'Penalty': penalties,
                                         'Objective Function': runs[i][0],
                                         'Broken Constraints': runs[i][1],
                                         'Energy (minimisation)': energies}))
        return results

    @staticmethod
    def columns_to_table(results, column_name):
        """Show energies, broken constraints or objective function values of all tries in all problems 
        on a single table.

        Parameters
        ----------
        results : list
            The output of the record_results(...).
        column_name : str
            The name of the column that we want to isolate.

        Returns
        -------
        pandas.core.frame.DataFrame
            DataFrame with certain characteristic (like energies) of all repeats of all problem solution.
        
        """
        
        energies = pd.DataFrame()
        repeats = len(results)  # Number of repeats is equivalent to the number of results
        for i in range(repeats):
            energies[f'{column_name} {i}'] = results[i][column_name]
        return energies

    @staticmethod
    def feasibility_table(results):
        """Calculates and displays whether the solutions are feasible or not.

        Parameters
        ----------
        results : list
            The output of the record_results(...).

        Returns
        -------
        pandas.core.frame.DataFrame
            A DataFrame with booleans that state whether the solution was feasible or not.
        
        """
        
        feasibility = pd.DataFrame()
        repeats = len(results)  # Number of repeats is equivalent to the number of results
        # Solution is feasibly if no constraints were broken
        for i in range(repeats):
            feasibility[f'Feasible {i}'] = results[i]['Broken Constraints'] == 0
        return feasibility

    @classmethod
    def feasibility_statistic(cls, results):
        """Calculates and displays how many instances of each problem were feasible throughout all runs, the
        feasibility rate (feasible/all), and the mean and Standard Deviation of the energy of
        the solutions. It also shows the total, mean and Standard Deviation of all the listed
        parameters at the bottom of the table.

        Parameters
        ----------
        results : list
            The output of the record_results(...).

        Returns
        -------
        pandas.core.frame.DataFrame
            A DataFrame with feasibility statistics.
        
        """
        
        # Make tables with energies and feasible results
        feasibility = cls.feasibility_table(results)
        energies = cls.columns_to_table(results, 'Energy (minimisation)')
        # The number of results corresponds to the number of repeats
        repeats = len(results)

        # Calculate number of feasible solutions (in all runs)
        stats = pd.DataFrame({'Feasible': feasibility.sum(axis=1)})
        # Calculate feasibility rate
        stats['Feasibility rate'] = stats['Feasible'] / repeats
        # Calculate mean energy
        stats['Energy mean'] = energies.mean(axis=1)
        # Calculate energy standard deviation
        stats['Energy SD'] = energies.std(axis=1)
        # Calculate total, mean and standard deviation rows
        # Calculate them first, then add to the table. Otherwise,
        # the new table entries will be used in subsequent
        # calculations
        total = stats.sum()
        mean = stats.mean()
        sd = stats.std()
        stats.loc['Total'] = total
        stats.loc['Mean'] = mean
        stats.loc['SD'] = sd

        return stats

    @staticmethod
    def significance_test(first_greedy, first_sa, first_tabu, second_greedy, second_sa, second_tabu):
        """Uses a students t-test to check if the difference in the number of broken constraints of 
        solutions obtained with penalty coefficients of two different algorithms is statistically
        significant for all problems.

        Parameters
        ----------
        first_greedy : pandas.core.frame.DataFrame
            The first DataFrame to test with the number of constraints broken in each problem on each repeat
            with greedy solver.
        first_sa : pandas.core.frame.DataFrame
            The first DataFrame to test with the number of constraints broken in each problem on each repeat
            with simulated annealing solver.
        first_tabu : pandas.core.frame.DataFrame
            The first DataFrame to test with the number of constraints broken in each problem on each repeat
            with tabu search solver.
        second_greedy : pandas.core.frame.DataFrame
            The second DataFrame to test with the number of constraints broken in each problem on each repeat
            with greedy solver.
        second_sa : pandas.core.frame.DataFrame
            The second DataFrame to test with the number of constraints broken in each problem on each repeat
            with simulated annealing solver.
        second_tabu : pandas.core.frame.DataFrame
            The second DataFrame to test with the number of constraints broken in each problem on each repeat
            with tabu search solver.

        Returns
        -------
        pandas.core.frame.DataFrame
            Results of the students t-test.
        
        """

        # Flatten the dataframes
        flat = lambda df: df.to_numpy().flatten()
        a1, a2, a3 = flat(first_greedy), flat(first_sa), flat(first_tabu)
        b1, b2, b3 = flat(second_greedy), flat(second_sa), flat(second_tabu)
        # Calculate statistics
        significance = pd.DataFrame(index=['t-statistic','p-value'])
        significance['Greedy Algorithm'] = stats.ttest_ind(a1, b1)
        significance['Simulated Annealing'] = stats.ttest_ind(a2, b2)
        significance['Tabu Search'] = stats.ttest_ind(a3, b3)
        return significance

    @staticmethod
    def detailed_significance_test(first_greedy, first_sa, first_tabu, second_greedy, second_sa, second_tabu):
        """Uses a students t-test to check if the difference in the number of broken constraints of 
        solutions obtained with penalty coefficients of two different algorithms is statistically
        significant for every problem.

        Parameters
        ----------
        first_greedy : pandas.core.frame.DataFrame
            The first DataFrame to test with the number of constraints broken in each problem on each repeat
            with greedy solver.
        first_sa : pandas.core.frame.DataFrame
            The first DataFrame to test with the number of constraints broken in each problem on each repeat
            with simulated annealing solver.
        first_tabu : pandas.core.frame.DataFrame
            The first DataFrame to test with the number of constraints broken in each problem on each repeat
            with tabu search solver.
        second_greedy : pandas.core.frame.DataFrame
            The second DataFrame to test with the number of constraints broken in each problem on each repeat
            with greedy solver.
        second_sa : pandas.core.frame.DataFrame
            The second DataFrame to test with the number of constraints broken in each problem on each repeat
            with simulated annealing solver.
        second_tabu : pandas.core.frame.DataFrame
            The second DataFrame to test with the number of constraints broken in each problem on each repeat
            with tabu search solver.

        Returns
        -------
        pandas.core.frame.DataFrame
            Results of the students t-test.
        
        """
        
        column_names = ['Greedy Algorithm t-statistic', 'Greedy Algorithm p-value', 
                        'Simulated Annealing t-statistic', 'Simulated Annealing p-value',
                        'Tabu Search t-statistic', 'Tabu Search p-value']
        detailed_significance = pd.DataFrame(columns=column_names)
        detailed_significance.index.name = 'Problem'
        for i in range(len(first_greedy)):
            # Flatten the rows
            flat = lambda column: column.iloc[i].values
            a1, a2, a3 = flat(first_greedy), flat(first_sa), flat(first_tabu)
            b1, b2, b3 = flat(second_greedy), flat(second_sa), flat(second_tabu)
            # Calculate statistica
            greedy = stats.ttest_ind(a1, b1)
            sa = stats.ttest_ind(a2, b2)
            tabu = stats.ttest_ind(a3, b3)
            # Populate table
            new = [greedy[0], greedy[1], sa[0], sa[1], tabu[0], tabu[1]]
            detailed_significance.loc[f'{i}'] = new
        return detailed_significance

    @staticmethod
    def find_best_significance(sig_data):
        """Counts the number of problems where Verma and Lewis coefficients resulted in
        significantly less broken constraints, significantly more broken constraints and the
        number of problems where there was no significant difference compared to solutions
        that used coefficients generated by our algorithm.

        Parameters
        ----------
        sig_data : type
            Results of the students t-test produced by detailed_significance_test(...).
            
        Returns
        -------
        pandas.core.frame.DataFrame
            The number of problems Verma and Lewis coefficients resulted in significantly less 
            broken constraints, significantly more broken constraints and the
            number of problems where there was no significant difference compared to solutions
            that used coefficients generated by the other algorithm.
        
        """
        
        vl_better = [0, 0, 0]
        no_sig_diff = [0, 0, 0] 
        vl_worse =  [0, 0, 0]
        
        # Use column name based on the algorithm we are considering
        t = ['Greedy Algorithm t-statistic',
            'Simulated Annealing t-statistic',
            'Tabu Search t-statistic']
        p = ['Greedy Algorithm p-value',
             'Simulated Annealing p-value',
             'Tabu Search p-value']
        
        # Count
        for i in range(3):
            for _, row in sig_data.iterrows():
                if row[t[i]] > 0 and row[p[i]] <= 0.05:
                    vl_worse[i] += 1
                elif row[t[i]] < 0 and row[p[i]] <= 0.05:
                    vl_better[i] += 1
                else:
                    no_sig_diff[i] += 1
        
        output = pd.DataFrame({'VL was better': vl_better,
                               'No significant difference': no_sig_diff,
                               'VL was worse': vl_worse}, index=['Greedy', 'SA', 'TS'])
        
        return output
