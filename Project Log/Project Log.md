# Week 1 
## Objectives
* Learn the basics of Simulated Annealing.

## Tasks
### Completed
* Watch [[Simulated Annealing Explained By Solving Sudoku - Machine Learning]]
* Read [[Diser/Materials/Simulated Annealing]]
* Understand at least one of the examples [[Quadratic Unconstrained Binary Optimization ( QUBO ) on D-Wave Chimera Graph]]

## Meeting (02/09/2021)
### Before 
* Need to understand the basics of Simulated Annealing
 
 ### During
 * NSC tour
 * Discussed the possible project
 * Discussed Simulated Annealing
 ![[Meeting 1 Image.png]]
 
 ### After
 * Need to read [[The Metropolis–Hastings algorithm]] and [[Optimization by Simulated Annealing]]
 * Will have to explain Simulated Annealing on the meeting next week



*****



# Week 2
## Objective
Become a master of Simulated Annealing.

## Tasks
### Completed
* Watch [[Optimization - I (Simulated Annealing)]]
* Watch [[(ML 18.1) Markov chain Monte Carlo (MCMC) introduction]]
* Read [[A Short History of Markov Chain Monte Carlo; Subjective Recollections from Incomplete Data]]
* Watch [[Markov Chains Clearly Explained! Part - 1]]
* Watch [[An introduction to the Random Walk Metropolis algorithm]]
* Read [[Optimization by Simulated Annealing]]
* Read [[The Metropolis–Hastings algorithm]]
* Read [[What is the difference between Simulated Annealing and Monte-Carlo Simulations?]]
* Read [[Markov Chain Monte Carlo & Simulated Annealing]]
* Make lecture notes explaining Simulated Annealing in details
* Make plots or the presentation with matplotlib
* Research how to make plots look scientific ([[Science Plots]])
* Make a ppt that align with lecture notes

## Meeting (09/09/2021)
### Before 
* Make a lecture on Simulated Annealing to present during the meeting

**Questions:**
* Should I learn about Quantum Annealer before Digital Annealer as it is inspired by it? 

### During
Presented the lecture.

**Answers:**
* Yes, if I struggle with Digital Annealer, but it is not urgent

### After
* Need to learn more about Digital Annealer



*****



# Week 3
## Objective
Get more familiar with the Digital Annealer.

## Tasks
### Completed
* Watch [[Digital Annealer technology]]
* Watch [[Fujitsu Forum 2019 Keynote - From mathematical to industrial optimization]]
* Read [[IEEE SPECTRUM Digital Annealer]]
* Skim through [[Quantum Deep Learning; Sampling Neural Nets with a Quantum Annealer]]
* Watch [[Webinar; Quantum Computing by a Quantum Annealer]]
* Read series of articles [[Quadratic Unconstrained Binary Optimization ( QUBO ) on D-Wave Chimera Graph]]

## Meeting (16/09/2021)
### Before 
**Questions:**
* Ask about the benefits of using the sigmoid function for Simulated Annealing
* How do superconductors work with QA?
* What is the architecture of DA?
* Is there a difference between DA and QA in respect to this project? We use QUBO and penalty values are universal. As far as I understand, it is just a different technology to do the same thing and optimising penalties benefits both in the same way.
* Is there a difference between DA/QA and SA? Is the penalty optimisation somehow unique to quantum tunnelling approach.
* [[D-Wave Ocean Software Documentation]] - is there something similar to this for DA?

### During
**Answers:**
* Hardware of DA is not very important as it is outside of the project scope
* Penalty optimisation will most likely increase the effectiveness of both DA and QA, but we only have access to DA.

### After
* Read the EDA lecture
* Read the papers sent



*****



# Week 4
## Objectives
* Prepare for a meeting with Dr. Ayodele
* Get as familiar as possible with ideas from [[Pre-Project Meeting Notes]] 

## Tasks
### Completed
* Go through [[Pre-Project Meeting Notes]] notes and write out everything I do not understand
* Find papers that are related to QUBO penalty optimisation
* Read sections related to penalty values in [[A Tutorial on Formulating and Using QUBO Models]]
* Read the _EDA's and Markov Networks_ lecture sent on Teams
* Understand [[PyQUBO]]
* Understand [[qbsolv]]
* Read up on maximum satisfiability problem (MAX-SAT)
* Go through the ethics form and find controversial points
* Read up on knapsack problem and it's QUBO representation from [[A Tutorial on Formulating and Using QUBO Models]]
* Read up on general assignment problem
* Make a list of questions for Dr. Ayodele and Prof. McCall on things I still do not understand from [[Pre-Project Meeting Notes]]


## Meeting (23/09/2021)
### Before 
* Get as familiar as possible with [[Pre-Project Meeting Notes]]

**Questions:**
* _"Can a process of evaluating sub-patterns be used to set tighter penalty bounds to improve QUBO solution process?"_
	* So we are going to have penalty bounds, not a single penalty value? So the minimum value will be increasing to the maximum value with certain... reduction rate? during the annealing to find the best answer.
	* In Glovers paper it says that you can have multiple penalties. I assume the scope of this project is just a single global penalty.
* _"Use problem structure / probing techniques to extract variable interaction structure._"
	* Problem structure?
	* Probing techniques?
	* Variable interaction structure?
	* Has this been done before? Is there a similar example? 
* _"Use partial evaluation techniques to find major variable interaction components in untransformed problem and estimate effect on overall fitness. Use this to estimate penalty ranges to achieve a tighter bound."_
	* Partial evaluation techniques? 
	* Variable interaction components?
	* Untransformed problem: not in form of QUBO? 
	* Do we do that in a simulation using random walk?
* Use PyQUBO, qbSolve, for transformation but amend penalty using estimation process
	* Is there something similar to D-Wave Ocean for DA?
* _"'Create own solver {GA, DEUM,}'"_
	* Our solver will have the same QUBO format and will get the same input, but it will not have any penalties?
	* qbsolve allows Tabu search as well. Maybe try that too?
* Run experiments to compare solution time for {own solvers} vs {transformation + DA}
	* Is it also meaningful to also compare generated penalties vs standard penalty which is 10 
* Ask about ethics form: 1c, 2, 3d, 5c, 10
* Ask about relevant papers

### During
* Meeting with Dr Ayodele and Professor McCall

**Answers**:
* Penalties cannot be changed during the annealing. They must be fixed.
* We might have multiple penalties if there are more than one constraint function, but this is unlikely
* For P value optimisation implementation have a look at harmonic analysis and Walsh function
* We can try to optimise for P not in form o QUBO
* There is no API for Digital Annealer, but Dr Ayodele can manually run it on Digital Annealer
* It is very easy to code Digital Annealer algorithm or a normal computer as it has minor differences from Simulated Annealing in terms of implementation
* We may test our solution against some default P value or try to optimise P with methods done by other people to compare the performance. It is not meaningful to compare Digital Annealer with Genetic Algorithm as one is in form of QUBO and the second is not
* Ethics form: 1c - yes, 2 - no, 3d - yes, 5c - yes, 10 - maybe (no)

### After
* Make a draft of project proposal before the next meeting 
* Have a look at harmonic analysis and Walsh function to get ideas for penalty optimization



*****



# Week 5
## Objectives
* Make a project log
* Make a project proposal draft
* Have a look at harmonic analysis and Walsh function to get ideas for penalty optimisation

## Tasks
### To-do
* [[Embedding Inequality Constraints for Quantum Annealing Optimization]]
* Create a repository for dissertation materials

### Completed
* Research what project logs can be like
* Make a template of my project log
* Make a full project log and fill it in
* Skim through [[Towards Prediction of Financial Crashes with a D-Wave Quantum Computer]]
* Look at harmonic analysis and Walsh function.
* Understand the difference between Ising and QUBO models. [[Difference between BQM, Ising, and QUBO problems?]]
* Read [[Penalty and partitioning techniques to improve performance of QUBO solvers]]
* Research variable interaction components
* Read [[QROSS; QUBO RELAXATION PARAMETER OPTIMISATION VIA LEARNING SOLVER SURROGATES]]
* Read about SA/DA algorithm difference from [[Physics-Inspired Optimization for Quadratic Unconstrained Problems Using a Digital Annealer]]
* Found TSP dataset: [[TSPLIB—A Traveling Salesman Problem Library]]
* Make an initial project proposal draft

## Meeting (30/09/2021)
### Before 
* Make a project proposal draft

### During
* Discussed progress
* Discussed the proposal draft
* Discussed possible penalty coefficient estimation algorithms

### After
* In proposal draft
	* Write references
	* Make it look professional
	* Add Mayowa as industry advisor
	* Elaborate on Objective 6 and add dissemination
* Read [[Partial structure learning by subset Walsh transform]]



*****



# Week 6
## Objectives
* Finish the detailed project proposal

## Tasks
### To-do
* Read [[Partial structure learning by subset Walsh transform]]

### Completed
* Make draft 2 of detailed project proposal
* Complete ethics form
* Add a Gantt chart as per Mayowa's feedback

## Meeting (7/10/2021)
### Before 
* Make a project proposal
* Read [[Partial structure learning by subset Walsh transform]]

### During
* Check project proposal
* Look at ethics form
* Complete supervisor's part

### After
* Make a git repository with all the files
* Read [[Partial structure learning by subset Walsh transform]]



*****



# Week 7
## Objectives
* Read more literature
* Make git repository

## Tasks
### To-do
* Read [[Partial structure learning by subset Walsh transform]]

### Completed
* Make git repository
* Read the entire honours guidelines document
* Read [[Introduction to Walsh Analysis]]
* Read [[Embedding Inequality Constraints for Quantum Annealing Optimization]]

## Meeting (14/10/2021)
### Before 
* Make a git repository with all the files
* Read [[Partial structure learning by subset Walsh transform]]

### During
* One of the lit review grading aspects: analysis of context and consideration of alternatives. What does it mean?



*****



# Week 8
## Objectives
* Understand Walsh Transformations and try to link it to Penalty values

## Tasks
### To-do

* Watch [[Surrogate-assisted Multi-objective Combinatorial Optimization]]

### Completed
* Read the lecture sent by Professor McCall
* Read the relevant part of [[The Role of Walsh Structure and Ordinal Linkage in the Optimisation of Pseudo-Boolean Functions under Monotonicity Invariance]]
* Go through [[Genetic Algorithms and Walsh Functions; Part I, A Gentle Introduction]]

## Meeting (21/10/2021)
### During
Talk about Walsh interactions.
Are we talking about i-i pairs?
Complexity.
Ways to calculate penalty.
Possible benchmarks.
Numerical approach.



*****



# Week 9 
## Objectives
* Start writing the Literature Review

## Tasks
### To-do
* Read paragraph 3 of [[Multivariate Markov networks for fitness modelling in an estimation of distribution algorithm]]

### Completed
* Make a template of lit review
* Make a draft of *Annealing* section
* Make a draft of *Simulated Annealing* section

## Meeting (28/10/2021)
### During
* Talked about writing Lit Review
* We are better at saying things rather than writing things. Maybe it is better to first explain verbally what I am about to write?



*****



# Week 10
## Objectives
* Walsh interactions

## Tasks
### To-do
* Email Dr Christie

### Completed
* Read [[Walsh Functions A Gentle Introduction sources Complex Systems]]
* Read paragraph 3 of [[Multivariate Markov networks for fitness modelling in an estimation of distribution algorithm]]
* [[Simulated Stochastic Approximation Annealing for Global Optimization With a Square-Root Cooling Schedule]]

## Meeting (4/11/2021)
### During
* So we convert the penalty function into energy distribution function defined as a sum of Walsh coefficients of a clique, α, times the Walsh functions of a clique. See the image. Where α are the interactions of the clique we are looking at.
* So ultimately, we are trying to find α coefficients?
* We will have perfect model structure as all the interactions are explicitly defined.
* We do not care about the fitness of individuals.

### After
Least squares estimation
Estimation of Markov Random Field



*****



# Week 11
## Objectives
* Lit review

## Tasks
### Completed
* Simulated Annealing draft 2
* Quantum Annealing draft 1
* [[Quantum annealing]]
* [[Quantum Deep Learning; Sampling Neural Nets with a Quantum Annealer]]
* [[QUANTUM ANNEALING AND QUANTUM FLUCTUATION EFFECT IN FRUSTRATED ISING SYSTEMS]]
* [[Quantum annealing; An introduction and new developments]]
* [[OPTIMIZATION BY SIMULATED ANNEALINGl AN EXPERIMENTAL EVALUATION; PART 1, GRAPH PARTITIONIN]]
* [[Digital Annealer for quadratic unconstrained binary optimization; a comparative performance analysis]]
* [[Ising formulations of many NP problems]]
* Digital Annealer draft 1
* QUBO intro draft 1

## Meeting (11/11/2021)
### During
* Quantum Annealing
* Friday Deadline
* Can video lecture be a reference



*****



# Week 12
## Objectives
* Lit review

## Tasks

### Completed
* QUBO model
* Constraints and Penalties
* Natural QUBO Formulation
* Non-Natural QUBO Formulation
* Analytical penalty optimization 
* Numerical 1 penalty optimization 
* Numerical 2 penalty optimization 
* ML penalty optimization
* Fix Simulated Annealing section (negative when maximizing)
* Write and collapse Libraries and Algorithms sections into a single one
* Add Walsh interactions to Numerical 2
* Fix Q matrix with arbitrary value of 8
* Figures and tables
* Number the formulas
* Pseudocode with labels, lines and table of algorithms
* Introduction
* Summary

## Meeting (17/11/2021)
### During
* Feedback
* Word limit (including references or not)
* Pseudocode table of contents
* Figure contents
* Line numbers in pseudocode
* Label the pseudocode
* Motivation, focus structure (introduction section)
* What CO are
* Solving them quickly is important 
* One promising approach is Walsh interactions which attached explicit energy to energies of the variables, which is naturally. In Lewis part
* In summary, summarize everything and form a research question (or repeat the one from the project proposal)
* Why am I describing all of this
* Explain objective function
* Number equations

### After
* Word limit is 5000 + 10% with references
* Pseudocode should be labeled, numbered, have line counts and be in table of contents.
* There should be a table of figures and table of tables
* Need to add an introduction with the motivation (including what CO problems are and why it is important to be able to solve them quickly), what the following sections will describe and why it is important for our motivation
* Numerical 2 approach. Say in the summary that one promising approach is to use Walsh interactions. They explicitly attach energy to the variables in a way that is natural to boolean functions like QUBO
* Make figures better
* Explain what an objective function is when I introduce it
* Number the equations
* Do not add arbitrary value of M=8 to the Q matrix, but rather see how M affects the matrix.
* In summary, summarize all we have talked about. Identify gaps in research and propose a direction to move into (reduce M from numerical 2 by taking into account the quadratic penalties)
* We do not flip the negative in SA when maximizing
* Do the algorithms section
* Write about the the machine learning approach



*****



# Week 13
## Meeting (24/11/2021)
* Discuss changes made to the literature review 



*****



# Week 14
## Objectives 
* Understand what requirements engineering requires

## Tasks
### Completed
* Read requirements lecture 1
* Read requirements lecture 2
* Make a rough sketch of requirements
* Give the sketch a structure
* [[D-Wave Guide]]
* Add the little details


## Meeting (07/12/2021)
### During
* Talk about requirements engineering
* How many pages (2?)
* Scientific requirements. What are they like? 
* MOSCOW
* Specify that it is for one constrained function 
* Might be used for more, but it is not a necessity
* Must be tested on classical 
* Could be tested on DA
* Should work with QUBO
* Might work with Ising Spinning Glass
* Combinatorial problem
* Should be tested using at least two datasets
* Should be tested with other solutions
	*	Specify solutions
* Any stakeholders 
* How to measure differences
* Rigorous statistical testing / analysis of results
* Requirement related to the company
* Time constraints
* Visualisation requirements? 
* Single solution time requirements
* What sections? Functional, non-functional of the experiment, any more

* Easy to swap problems in and out
* Moscow colored table
* Methods of settings penalties
* Have a way of evaluating the effect the have on performance of Digital Annealer
* 2 parts (experiment, software developed)



*****



# Week 15
## Objectives
* Finish Requirements Engineering

## Tasks
### Completed 
* Finish Requirements Engineering
* Make post-meeting changes

## Meeting
### During
* Discuss Carnegie Scholarship
* Discuss the deliverable

## After
Fix the following:
* Find -> generate penalty coefficients
* Calculate -> generate M
* Always say *M*
* Completed -> basic working version
* Deadline of experiments -> All experimental hypotheses must be tested until middle week of February



*****



# Week 16
## Meeting
### During
* When using D-Wave libraries, do we manually do the multiplication of penalty coefficient with the constraint function and then addition with the original objective function? 
* Permutation problem
* Find an expression

*RUN 1*
* Try to estimate the denominator with bit flips
* Solve 
* Check if answers are feasible

*RUN 2*?
* Try to estimate the denominator with bit flips
* Solve 
* Check if answers are feasible
* Take infeasible solutions and increase P by 2
* Solve
* Repeat 2 last 3 steps



*****



# Holiday
## Objective
- Proof of concept

## Meeting
### During
- Show progress
- Set goals



*****



# Week 17
## Objective
- Run Length Distribution implementation

## Tasks
- ~~Read [[On the Use of Run Time Distributions to Evaluate and Compare Stochastic Local Search Algorithms]]
- ~~Find a way to implement Run Length Distribution
- Implement new Penalty algorithm
- ~~Read [[Incorporating a Metropolis method in a distribution estimation using Markov random field algorithm]]
* ~~Read  [[Towards a Characterisation of the Behaviour of Stochastic Local Search Algorithms for SAT]]
* ~~Implement RLD for greedy algorithm
* ~~Implement RTD for tabu search

## Meeting
### During
- RLD Notes
	- We need to test it on a single problem rather than a cluster of different ones. I will just pick a problem just like in the [[Incorporating a Metropolis method in a distribution estimation using Markov random field algorithm]]  paper.
	- _"The RLD shows, for each algorithm, the cumulative percentage of successful runs that terminated within a certain number of function evaluations"._
	- All the papers I have came across had a clear indication of success for the algorithm (the solution). But QUBO has no clear solution. I think it is fair to use mean solution cost of Verma and Lewis as a target.
	- RLD cannot be implemented for Simulated Annealing in the form it appears in the dwave-neal. It works on predefined number of steps.
	- RLD with tabu 


### After
- Describe what I am doing in clear and unambiguous way
- Show distribution of energies (box-plot)
- Try RLD on small, medium and large problem



*****



# Week 18
## Objective
- Coding
- Explaining the approach

## Tasks
- ~~Fix the weird energy levels
- ~~Add another dataset
- ~~Code new penalty estimation method
- ~~Write an explanation to what is going on
- ~~Make a notebook that shows how the penalty value will change and why

## Potential future work
- Make a python module, refactor code
- Run experiments
- Add statistical testing
- Tune hyperparameters
- Implement new penalty estimation method
- Add new problems 
- Tables and graphs


*****



# Week 19
## Objective
- Statistical significance

## Tasks
- ~~Change some formulas in Lit Review
- ~~Research tests
- Code t-test



*****



# Weeks 20-21
## Objective
- Statistical significance
- Code improvement

## Tasks
- ~~Change some formulas in Lit Review
- ~~Methodify the main pipeline
- Email Mayowa about double quadratic penalties and squared penalty function
- ~~Make nice RLD and RTD graphs
- ~~Find statistical significance test
	- T-test
	- Null hypothesis: new penalty estimation technique will not produce penalty coefficients that will significantly affect the ground energies achieved in any of the problems across every algorithm.
		- Run an algorithm on all problems many times with both sets of penalty coefficients.
		- Check if the difference in means was significant in the problems (compare the problems independently).
		- See if difference was positive or negative, where it was spotted.
		- Do it with another algorithm and repeat the process.
		- Do it with another dataset and repeat the process.
	* Null hypothesis: new penalty estimation technique will not produce penalty coefficients that will significantly affect the ground energies achieved in all problems and across every algorithms.
		* Take all runs of all problems as equals.
		* Calculate general difference.
	* __Using energy as statistical significance test is a bad idea as different penalty values will most certainly affect the significance. And lower penalty values, for example 0, will give the best energies. But they will also break the most constraints. In statistical significance testing we have to capture the number of constraints that were broken rather than the energy__
* ~~Make nice RLD and RTD plots
* ~~Code data saving and loading
* ~~Make a table with the number of constraints broken
* ~~Code statistical test 1 
* ~~Code statistical test 2

## Penalty ideas
* Do a very slow binary tree search (all possibilities)
	* Exhaustive search kills the entire purpose of optimisation
* Double search
* Don't we have to square penalty function?



*****



# Week 22
## Objective
- Minor code improvements
- Initial dissertation

## Tasks
- Cover page
- ~~Make draft sections
- ~~Acknowledgments
- ~~Choose best answer, not first during minimisation

## Meeting
- Can I use different university logo for cover page? 
	- Yes
- Make a single sentence and make the whole dissertation a document meant for the reader to understand that sentence
- "To optimise better with QA, we need to choose a penalty coefficient that will punish the algorithm for ..., and to choose a better penalty coefficient, I have made a more informed algorithm, but sacrificed guarantees of feasibility"
- The dissertation can have the following sections
	- Project Overview 
		- Project proposal
	* Literature Review
	* Design & Implementation
		- Talk about choices (jupyter notebooks etc...)
	- Results 
		- Show tables, graphs etc... Talk about the results
	- Conclusion 



*****



# Week 23-24
## Objective
* Penalty functions
* Implementation section

## Tasks
* ~~Make Penalty class with different penalty generation algorithms
* ~~Split all supplementary methods into classes
* ~~Make a python module with all the code used in experiments
* ~~Methodify Run Time/Length Distribution code
* ~~Make visualisation module
* Tune hyperparameters
	* ~~Make a list of possible hyperparameters to tune

## Final Questions to Mayowa
I am not sure I entirely understand the given methods. So in Verma and Lewis method we go through every single row and see how a bit flip would affect it. But we do not multiply the quadratic coefficients by 2.  In examples the quadratic coefficients are always twice smaller in a QUBO row as there will be another instance of the same coefficient, just in a different row. So 6x1x6 will be a 3 in row 1 and a 3 in row 6, but when they are added together, they will make a 6.

## Meeting
* Show the python package
* Show new notebooks
	* How clean it is and how to change the penalty/data
* Hyperparameters
* Word/LaTeX



*****



# Week 25
## Tasks
* Tune hyperparameters
* Load other datasets
* Transfer word submissions to LaTeX

## Tasks
* ~~LaTeX styles
* ~~LaTeX title page
* ~~LaTeX Project Overview
* LaTeX Lit Review
* Jupyter Notebook for another dataset
* ~~Test hyperparameters

## Meeting
* Is RTD for tabu search reasonable? As we are defining how long each run will take before we run the algorithm. Thus we know that run time of all runs, both successful and unsuccessful, will be roughly the same.
* What target energy to use with RLD? Currently, I am using mean energy. But then if I repeat this experiment with another penalty coefficient algorithm, mean will change and RLD will change. In a way that will prohibit us from comparing them. At the same time, it is impossible to deduce energy that corresponds to a feasible solution.
* Hyperparameter tactics: choose tabu search hypereparameters that give solution rate 0.5, 
* Run tabu many times with different times for RTD
* For RLD check all solutions for feasibility and base the graph on it
* Move project plan to Appendix
* 1.6 Content Summary (explain the overall structure)
* Add line numbers to algorithms



*****



# Week 26
## Objectives
* LaTeX
* New notebooks for other datasets

## Tasks
* ~~LaTeX Lit Review
* ~~Add line numbers to algorithms
* ~~Move project proposal to Appendix
* ~~Content Summary section at the end
* ~~Make a notebook for Quadratic Assignment Problem
* ~~Make a data preparation method for other datasets
* ~~Make a notebook for Travelling Salesman Problem
	* ~~We run TSP large and small separately because large run for significantly longer time

## Meeting
- Report presentation
- Ask about testing (in mark scheme)
- Starting to see interesting things: MKP was super fast!
- TSP split into 2 parts: large and small
- Decided to tune hyperparameters more thoroughly
- Give algorithms X time per dataset rather than problem
	* Datasets can have different number problems
	* Problems are of different difficulty
* Testing subsections
	* Write something general about approach to software engineering
	* Unit tests?
	* Major decision issues 
	* Efficiency
	* Issues that I have faced when working



*****



# Week 27
## Objectives
* LaTeX

## Tasks
* ~~Move Requirements Engineering to LaTeX
* ~~Add a section explaining Multiple Knapsack Problem to the dissertation
* ~~Add a section explaining Travelling Salesman Problem to the dissertation
* ~~Add a section explaining Quadratic Assignment Problem to the dissertation
* ~~Code the discussed penalty estimation algorithm
* ~~Research Gaussian Elimination
* ~~Think about turning point penalty estimation algorithm



*****



# Week 28
## Objectives
* Poster

# Tasks
* ~~Draft
* ~~Visualisations
* ~~Final


*****



# Week 29
# Objectives
* Finish code
* Prepare for Degree Show

## Tasks
* ~~Penalty Coefficient Distribution
* ~~Run Time and Run Length Distributions



*****



# Week 30 - Week 32
## Objectives
* Write the dissertation

# Tasks
* Write abstract
* Comment the code and add docstring
* Methodify Predicting Changes
* Methodify Statistical Significance
* ~~Get initial RLD/RTD
* Get secondary RLD/RTD
* ~~Add poster as Appendix
* Do something with dataset (upload them to github using [git LFS](https://git-lfs.github.com/))
* Delete RLD/RTD from experiment notebooks
* Check if our algorithms actually do not improve feasibility
* Comment out the Russian font packages
* Make a table with dataset instances, where VL was better
* ~~Make the repository public
* Write readme
* Visualisation module seciton
