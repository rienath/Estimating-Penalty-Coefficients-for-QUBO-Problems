from IPython.display import display_html
from itertools import chain, cycle
import pandas as pd


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

    # Show  energies/broken constraints/objective function values of all tries in all problems in a single df
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
        # Calculate total row
        stats.loc['Total'] = stats.sum()
        # Calculate mean row
        stats.loc['Mean'] = stats.mean()
        # Calculate SD row
        stats.loc['SD'] = stats.std()

        return stats
