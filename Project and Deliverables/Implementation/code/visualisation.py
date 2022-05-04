import math
import tabu
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.interpolate import make_interp_spline
from experiment import Experiment
from table import Table


class Figure:

    global PENALTY_ALGORITHMS
    
    PENALTY_ALGORITHMS = ['Verma&Lewis', 'Expected Constraint', 'Minimum Lazy', 'Verma&Lewis check']
    
    # Smooths the line of a figure given the data, minimum and maximum x
    @staticmethod
    def __smooth_the_line(data, min_x, max_x):
        # Create more points for x-axis
        steps_new = np.linspace(min_x, max_x, 500)
        # Smooth
        spl = make_interp_spline(data[data.columns[1]], data['Successful Percentage'], k=2)
        smooth_percentage = spl(steps_new)
        # Limit smoothed values to 0-100 too
        smooth_percentage = [0 if i < 0 else i for i in smooth_percentage]
        smooth_percentage = [100 if i > 100 else i for i in smooth_percentage]
        return steps_new, smooth_percentage

    # OUTDATED
    # Makes a table with successful runs at each recorded "length", the cumulative number of
    # successful runs and their cumulative percentage
    @staticmethod
    def __run_length_distribution_table(solver_response):
        steps = []
        energies = []

        for step, energy in solver_response.data(fields=['num_steps', 'energy'], sorted_by='num_steps'):
            steps.append(step)
            energies.append(energy)

        # Sort both lists by the number of steps
        steps, energies = (list(elements) for elements in zip(*sorted(zip(steps, energies))))
        # Our target is the mean energy
        target = (sum(energies) / len(energies))
        # Find runs that got energy above our target
        successful = [i < target for i in energies]
        # Make a dataframe
        rld = pd.DataFrame({'Steps': steps, 'Successful': successful})
        # Sum successful runs by repeating steps
        rld = rld.groupby(by=['Steps'], axis=0).sum()
        # Calculate cumulative number of successful runs
        rld['Cumulative'] = rld['Successful'].cumsum()
        # Calculate cumulative percentage of successful runs
        rld['Cumulative Percentage'] = rld['Cumulative'] / max(rld['Cumulative']) * 100
        return rld

    # OUTDATED
    @classmethod
    def run_length_distribution(cls, solver_response):
        rld = cls.__run_length_distribution_table(solver_response)

        # Set plot styles
        plt.style.use(['science', 'no-latex', 'ieee'])
        # Set limits
        # x-axis limits are floor and ceiling to nearest 10 of max and min values
        lowest_steps = math.floor(rld.index[0] / 10) * 10
        highest_steps = math.ceil(rld.index[-1] / 10) * 10
        offset = 0.2  # Offset is needed to see the line at graph borders
        plt.axis((lowest_steps, highest_steps, 0 - offset, 100 + offset))
        # Set labels and dpi
        plt.xlabel("Steps")
        plt.ylabel("Cumulative percentage of successful runs")
        plt.gcf().set_dpi(300)
        # Smooth the line, otherwise it will look like a staircase
        steps_new, smooth_percentage = cls.__smooth_the_line(rld, lowest_steps, highest_steps)
        # Make a plot
        plt.plot(steps_new, smooth_percentage)

    # OUTDATED
    # Makes a table with successful runs at each recorded "time", the cumulative number of
    # successful runs and their cumulative percentage
    @staticmethod
    def __run_time_distribution_table(times, energies):
        # Sort both lists by the number of steps
        times, energies = (list(elements) for elements in zip(*sorted(zip(times, energies))))
        # Our target is the mean energy
        target = (sum(energies) / len(energies))
        # Find runs that got energy above our target
        successful = [i < target for i in energies]
        # Make a dataframe
        rtd = pd.DataFrame({'Time': times, 'Successful': successful})
        # Sum successful runs by repeating steps
        rtd = rtd.groupby(by=['Time'], axis=0).sum()
        # Calculate cumulative number of successful runs
        rtd['Cumulative'] = rtd['Successful'].cumsum()
        # Calculate cumulative percentage of successful runs
        rtd['Cumulative Percentage'] = rtd['Cumulative'] / max(rtd['Cumulative']) * 100
        return rtd

    # OUTDATED
    @classmethod
    def run_time_distribution(cls, times, energies):
        rtd = cls.__run_time_distribution_table(times, energies)

        # Set plot styles
        plt.style.use(['science', 'no-latex', 'ieee'])
        # Set limits
        min_time = rtd.index[0]
        max_time = rtd.index[-1]
        offset = 0.2  # Offset is needed to see the line at graph borders
        plt.axis((min_time, max_time, 0 - offset, 100 + offset))
        # Set labels and dpi
        plt.xlabel("Time taken to reach a solution (s)")
        plt.ylabel("Cumulative percentage of successful runs")
        plt.gcf().set_dpi(300)
        # Smooth the line, otherwise it will look like a staircase
        times_new, smooth_percentage = cls.__smooth_the_line(rtd, min_time, max_time)
        # Make a plot
        plt.plot(times_new, smooth_percentage)

    "If you want to repeat a  run multiple times and get the average feasibility for that number of steps/ms, use repeats. Otherwise, the distribution will be unstable"
    def __get_distribution_data(data, minimisation, solver, max_bound, steps, num_reads=1, repeats=1):
        # We need to work with time if the solver is Tabu
        # Otherwise, we need steps
        tabu_bool = (type(solver) == tabu.sampler.TabuSampler)
        label = 'Time (ms)' if tabu_bool else 'Steps'
        
        # Output
        dist = pd.DataFrame({label: [],'Successful Percentage': [], 'Algorithm': []})

        for algorithm in PENALTY_ALGORITHMS:
            # Add 0 point
            dist = pd.concat([dist, pd.DataFrame({label: [0], 'Successful Percentage': [0], 'Algorithm': algorithm})])
            
            # Generate all QUBOs and penalties
            # We can have two types of data inputs: one suitable for normal data preparation,
            # and second suitable for data prep light. They can be distinguished by their size
            if len(data) == 4:
                obj_qubos = data[0]
                obj_constants = data[1]
                con_qubos = data[2]
                con_constants = data[3]
                QUBOs, penalties = Experiment.data_prep_light(obj_qubos, con_qubos, algorithm, minimisation)
                qubo_sizes = [max(qubo, key=tuple)[0] + 1 for qubo in QUBOs]
            else:
                qubo_sizes = data[0]
                objectives = data[1]
                constraints = data[2]
                QUBOs, penalties, obj_qubos, obj_constants, con_qubos, con_constants = Experiment.data_prep(qubo_sizes, objectives, constraints, algorithm, minimisation)
            
            # Collect data
            for steps_time in range(0, max_bound+1, steps):
                # Skip 0
                if steps_time == 0: 
                    continue
                # Run the sampler
                # If we have tabu 
                if tabu_bool:
                    runs = Experiment.run_sampler(QUBOs, obj_qubos, obj_constants, con_qubos, con_constants, 
                                              solver, repeats, timeout=steps_time)
                else:
                    runs = Experiment.run_sampler(QUBOs, obj_qubos, obj_constants, con_qubos, con_constants, 
                                              solver, repeats, num_sweeps=steps_time, num_reads=num_reads)
                # Record ddadta
                results = Table.record_results(runs, qubo_sizes, penalties, repeats)
                feasibility = Table.feasibility_table(results)
                t_values = (sum(feasibility.values.flatten() == True))
                f_values = (sum(feasibility.values.flatten() == False))
                dist = pd.concat([dist, 
                                pd.DataFrame({label: [steps_time],
                                              'Successful Percentage': [(t_values / (t_values + f_values))*100],
                                              'Algorithm': algorithm})])
        # Reset indices
        dist.reset_index(inplace=True)
        
        return dist

    @classmethod
    def run_distribution(cls, data, minimisation, solver, max_bound, steps, num_reads=1, repeats=1):
        # Get the distribution
        dist = cls.__get_distribution_data(data, minimisation, solver, max_bound, steps, num_reads, repeats)
        # Set plot styles
        plt.style.use(['science', 'no-latex', 'ieee'])
        # Set limits
        # x-axis limits are floor and ceiling to nearest 10 of max and min values
        lowest_steps = math.floor(dist[dist.columns[1]][0] / 10) * 10
        highest_steps = math.ceil(dist[dist.columns[1]][len(dist)-1] / 10) * 10
        offset = 0.2  # Offset is needed to see the line at graph borders
        plt.axis((lowest_steps, highest_steps, 0 - offset, 100 + offset))
        # Set labels and dpi
        plt.xlabel(dist.columns[1])
        plt.ylabel("Percentage of successful runs")
        plt.gcf().set_dpi(300)
        # Plot all the lines
        for algorithm in PENALTY_ALGORITHMS:
            # Smooth the line, otherwise it will look like a staircase
            steps_new, smooth_percentage = cls.__smooth_the_line(dist[dist['Algorithm'] == algorithm], lowest_steps, highest_steps)
            # Make a plot
            plt.plot(steps_new, smooth_percentage)
        plt.legend(PENALTY_ALGORITHMS)
        return dist
