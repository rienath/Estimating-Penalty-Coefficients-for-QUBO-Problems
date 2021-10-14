# Week 1 
## Objective
Learn the basics of Simulated Annealing.

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
* Is there a difference between DA and QA in respect to this project? We use QUBO and penalty values are universal. As far as I understand, it is just a different technology to do the same thing and optimizing penalties benefits both in the same way.
* Is there a difference between DA/QA and SA? Is the penalty optimization somehow unique to quantum tunneling approach.
* [[D-Wave Ocean Software Documentation]] - is there something similar to this for DA?

### During
**Answers:**
* Hardware of DA is not very important as it is outside of the project scope
* Penalty optimization will most likely increase the effectiveness of both DA and QA, but we only have access to QA

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
* Find papers that are related to QUBO penalty optimization
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
* _"Create own solver {GA, DEUM,}"_
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
* For P value optimization implementation have a look at harmonic analysis and Walsh function
* We can try to optimize for P not in form o QUBO
* There is no API for Digital Annealer, but Dr. Ayodele can manually run it on Digital Annealer
* It is very easy to code Digital Annealer algorithm or a normal computer as it has minor differences from Simulated Annealing in terms of implementation
* We may test our solution against some default P value or try to optimize P with methods done by other people to compare the performance. It is not meaningful to compare Digital Annealer with Genetic Algorithm as one is in form of QUBO and the second is not
* Ethics form: 1c - yes, 2 - no, 3d - yes, 5c - yes, 10 - maybe (no)

### After
* Make a draft of project proposal before the next meeting 
* Have a look at harmonic analysis and Walsh function to get ideas for penalty optimization



*****



# Week 5
## Objectives
* Make a project log
* Make a project proposal draft
* Have a look at harmonic analysis and Walsh function to get ideas for penalty optimization

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
* Understand the difference between Ising and QUBO models. [[Difference between BQM, Ising, and QUBO problems?]].
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

## Meeting (7/10/2021)
### Before 
* Make a git repository with all the files
* Read [[Partial structure learning by subset Walsh transform]]

### During
* One of the lit review grading aspects: analysis of context and consideration of alternatives. What does it mean?

### After
