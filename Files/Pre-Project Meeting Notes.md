QUBO major issue: problems with multiple ineq constraints - set penalties in a reasonable way
Needs to work for classes of problem

Lots of choices for penalty technique - how to set the value, beyond problem bounds.

Tighter bound means can infer what penalty range needs to be be. Smaller values of penalty make search easier because search space will be smoother for the QUBO Digital Annealer process.

__Possible project__
Question - Can a process of evaluating sub-patterns be used to set tighter penalty bounds to improve QUBO solution process?

__Approach__
look at popular benchmarks - knapsack, general assignment, others from the tutorial
Use problem structure / probing techniques to extract variable interaction structure
Use partial evaluation techniques to find major variable interaction components in untransformed problem and estimate effect on overall fitness. Use this to estimate penalty ranges to achieve a tighter bound
Use PyQUBO, qbSolve, for transformation but amend penalty using estimation process
create own solver {GA, DEUM,}
Run experiments to compare solution time for {own solvers} vs {transformation + DA}
Explore how / whether penalty process affects this performance difference. Assess across different classes of problem.
*********
__Literature__
QUBO tutorial and other papers - to be added
 
__Related GECCO content__
Carlos Coello - finding solutions at the boundary of feasibility 
Mayowa to send and two papers on QUBO