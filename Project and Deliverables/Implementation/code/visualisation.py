import math
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.interpolate import make_interp_spline


class Figure:
    # Smooths the line of a figure given the data, minimum and maximum x
    @staticmethod
    def __smooth_the_line(data, min_x, max_x):
        # Create more points for x-axis
        steps_new = np.linspace(min_x, max_x, 500)
        # Smooth
        spl = make_interp_spline(data.index, data['Cumulative Percentage'], k=1)
        smooth_percentage = spl(steps_new)
        # Limit smoothed values to 0-100 too
        smooth_percentage = [0 if i < 0 else i for i in smooth_percentage]
        smooth_percentage = [100 if i > 100 else i for i in smooth_percentage]
        return steps_new, smooth_percentage

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
