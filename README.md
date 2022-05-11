# Estimating Penalty Coefficients for Quadratic Unconstrained Binary Optimisation Problems
Welcome to my bachelor's project! The QUBO is a way to write down a combinatorial optimisation. In that formulation, we have a penalty function that will punish the algorithm if it considers states that break constraints. But how do we know the scale at which we need to punish the solver, so it explores even infeasible states and comes up with a feasible solution? This is what we need a penalty coefficient for! There are different state-of-the-art algorithms for estimating penalty coefficients. In our project, we try to make one of them more accurate and explore what advantages, if any, such improvement would have.

# 🏃 How to run locally
1. Clone the repository.
``` bash
git clone https://github.com/rienath/Estimating-Penalty-Coefficients-for-QUBO-Problems.git
```
2. Install the conda environment.
``` bash
conda env create -f Estimating-Penalty-Coefficients-for-QUBO-Problems/Project and Deliverables/Implementation/environment.yml 
```
3. Activate it.
``` bash
conda activate env
```

# 🏗️ Folder structure 
``` bash
.
├── Dissertation LaTeX.zip
├── Dissertation.pdf
├── Files
├── Materials
├── Notes
├── Project Log
└── Project and Deliverables
    ├── Final Dissertation
    ├── Implementation
    │   ├── Data
    │   │   ├── Multidimensional Knapsack
    │   │   ├── Quadratic Assignment Problem
    │   │   ├── Travelling Salesman Problem
    │   │   └── Produced
    │   ├── Notebooks
    │   ├── code
    │   └── environment.yml
    ├── Literature Review
    ├── Poster
    ├── Project Proposal
    ├── Requirements Engineering
    └── Simulated Annealing
```
