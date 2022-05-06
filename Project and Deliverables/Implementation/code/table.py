from IPython.display import display_html
from itertools import chain, cycle
import pandas as pd


from scipy import stats

class Table:
    @staticmethod
    def display_side_by_side(*args, titles=cycle([''])):
        html_str = ''
        for df, title in zip(args, chain(titles, cycle(['</br>']))):
            html_str += '<th style="text-align:center"><td style="vertical-align:top">'
            html_str += f'<h2 style="text-align:left">{title}</h2>'
            html_str += df.to_html().replace('table', 'table style="display:inline"')
            html_str += '</td></th>'
        display_html(html_str, raw=True)

    @staticmethod
    def record_results(runs, qubo_sizes, penalties, repeats, minimization=False):
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

    # Show  energies, broken constraints or objective function values of all tries in all problems in a single df
    @staticmethod
    def columns_to_table(results, column_name):
        energies = pd.DataFrame()
        repeats = len(results)  # Number of repeats is equivalent to the number of results
        for i in range(repeats):
            energies[f'{column_name} {i}'] = results[i][column_name]
        return energies

    # Make a table that will display which solution were feasible
    @staticmethod
    def feasibility_table(results):
        feasibility = pd.DataFrame()
        repeats = len(results)  # Number of repeats is equivalent to the number of results
        # Solution is feasibly if no constraints were broken
        for i in range(repeats):
            feasibility[f'Feasible {i}'] = results[i]['Broken Constraints'] == 0
        return feasibility

    # Returns a table with different feasibility statistics
    @classmethod
    def feasibility_statistic(cls, results):
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

    '''
    Compares if number of broken constraints is significantly different across all
    instances of the same problem
    '''
    @staticmethod
    def significance_test(first_greedy, first_sa, first_tabu, second_greedy, second_sa, second_tabu):
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

    '''
    A detailed version of the above significance test, where all the problem instances are compared
    independantly.
    '''
    @staticmethod
    def detailed_significance_test(first_greedy, first_sa, first_tabu, second_greedy, second_sa, second_tabu):
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

    '''
    Acccepts detailed_significance_test method output.
    Returns the number of problems, where VL breaks significantly less constraints (0),
    there is no significant difference (1), where VL breaks significantly more constraints (2).
    It is impossible for VL to break more constraints as it has the largest M, but this number
    is included for testing purposes.
    '''
    @staticmethod
    def find_best_significance(sig_data):
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
