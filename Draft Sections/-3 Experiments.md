## Datasets


## Hyperparameters
- Seed hack
- Most default values
* num_reads shows how many times an algorithm will be run and best result found. Initial states are chosen randomly

### SA
* num_sweeps used to dictate how many steps will be made during the annealing process. The cooling rate (geometric) is adjusted to work with this number of sweeps.
	* Default value of 1000 was experimentally found to be good. Using smaller numbers leads to lower numbers of feasible solutions. Using higher numbers leads to slower runtimes at no significant feasibility rate increase.
	* Increasing num_reads is better in terms of fast/feasibility

### Tabu
- **timeout** ([_int_](https://docs.python.org/3/library/functions.html#int "(in Python v3.10)")_,_ _optional__,_ _default=20_) – Total running time per read in milliseconds. Default value is 20. Increasing it results in better results, but makes the run time slower. It was found that larger timeout values result in more feasible solutions, but slower run times. Moreover, increasing the timeout led to better solutions in the same amount of time compared to increasing num_reads. That is why num_reads is set to the default value (1) and only timeout is increased. 
- **energy_threshold** ([_float_](https://docs.python.org/3/library/functions.html#float "(in Python v3.10)")_,_ _optional_) – Terminate when an energy lower than `energy_threshold` is found. Was not used because we want to make sure that every run is given n seconds and we want to see, how good the solution it will obtain will be in the given time. (Then talk about timeout)

## Greedy
- num_reads - the number of times the algorithm will run for on every sample. The best solution will be chosen and returned. Used to control fairness.

Optimised all of them so with Verma&Lewis, which is our baseline, the run time of a single repeat (we repeat each run 10 times with different seeds for statistical significance) is approximately 30 seconds to go through each dataset with a single algorithm. Therefore, a 10 repeats run will take 300 seconds. And since we test 3 algorithms per dataset per penalty algorithm, one notebook takes over 15 minutes to run. Has its downsides as computer can be loaded with other things. We only ran the algorithms at the time to make sure that it is predominantly it that takes CPU. This way it is reasonably fair as all algorithms get approximately the same amount of CPU time.

TSP is separated into large and small problems and solved separately because the large problems take significantly longer to solve compared not only to the smaller problems of TSP, but also to the problems from other datasets.