It was decided to use Jupyter Notebooks as environment and conda to manage the packages. Conda allows exporting list of packages used in the project in form of yaml. Thus, it is easy to see what was used in the project, and if someone else wants to run it, a simple command '' can be used to install identical packages, making the software installation easy. Benefits of conda over pip.
https://pythonspeed.com/articles/conda-vs-pip/

However, quickly run into a problem. Dwave python packages are not very popular and are not supported by conda. 

But we can still use benefits of conda by [Installing non-conda packages](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-pkgs.html#installing-non-conda-packages) That is what has been done.

QBSolv is deprecated. Do not include this.
Chose 3 samplers.

- Why JN
- Progress bar struggles
	- Fastai
	- tqdm
	- Classical approach through IPython
- RLD and RTD
	- Why RLD is better
	- Natural implementation of RLD for greedy
	- Struggles of RLD for tabu and SA
	- Implementation of RTD for tabu

# How experiment works
## Loading data
- Load dataset 1 with small problems
- Load dataset 2 with large problems
- Merge them

## Data preparation
- Make QUBOS:
	- QUBO that represents the objective function
	- QUBO that represents the constraint function
- Calculate penalties
- Make the final QUBO, which includes both functions and penalty coefficient
	- Change it to the format D-Wave understands

## Experiments
- Set number x, which is the number of results we want to get from every algorithm. This is also the range of seeds that we will use (1-x) to obtain different results
- Run greedy algorithm x times
	- Every xth run will have n subruns
	- Where we choose run with minimum energy
	- To make it fair as other algorithms take longer to run
- Run simulated annealing
- Run tabu search

## Analysis
- Record the results
	- The problems (sizes and penalty coefficients), objective function value, number of broken constraints and total energy. There are different tables with different representations as we have many problems and many runs.
	- Calculate feasible runs (max x) for every problem. Find total, mean and SD
- Make a run length distribution for greedy algorithms
- Make a run time distribution for tabu search

9-11, 15 February