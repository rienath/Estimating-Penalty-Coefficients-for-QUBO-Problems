# Estimating Penalty Coefficients for Quadratic Unconstrained Binary Optimisation Problems
Welcome to my bachelor's project! There is a pretty cool way to write down combinatorial optimisation problems: QUBO. In that formulation, we have a penalty function that will punish the algorithm if it considers states that break constraints. But how do we know the scale at which we need to punish the solver, so it explores even infeasible states and comes up with a feasible solution? This is what we need a penalty coefficient for! There are different state-of-the-art algorithms for estimating penalty coefficients. In our project, we try to make one of them more accurate and explore what advantages, if any, such improvement would have.

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
├── Dissertation LaTeX.zip                      # LaTeX files
├── Dissertation.pdf                            # Dissertation
├── Files                                       # Different screenshots
├── Materials                                   # The materials used
├── Notes                                       # My notes
├── Project Log                                 # Project log (cleaner in dissertation)
└── Project and Deliverables                    # The project and university deliverables
    ├── Implementation                          # Implementation of the project
    │   ├── Data                                # Data used
    │   │   ├── Multidimensional Knapsack       # MKP dataset
    │   │   ├── Quadratic Assignment Problem    # QAP dataset
    │   │   ├── Travelling Salesman Problem     # TSP dataset
    │   │   └── Produced                        # Produced pickles!
    │   ├── Notebooks                           # Jupyter Notebooks
    │   ├── code                                # Python package
    │   └── environment.yml                     # Anaconda environment
    ├── Literature Review                       # The literature review (included in dissertation)
    ├── Poster                                  # The poster (included in dissertation)
    ├── Project Proposal                        # The project proposal (included in dissertation)
    ├── Requirements Engineering                # The requirements engineering (included in dissertation)
    └── Simulated Annealing                     # Some of my SA notes
```
