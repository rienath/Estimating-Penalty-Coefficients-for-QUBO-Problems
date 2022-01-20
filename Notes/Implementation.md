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