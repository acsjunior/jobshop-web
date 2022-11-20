#### Sets and parameters

$J \colon \text{set of jobs,} \; J = \{1,2,\ldots,n\},$

$M \colon \text{set of machines,} \; M = \{1,2,\ldots,m\},$

$p_{ji} \colon \text{processing time of job} \; j \in J \; \text{on machine} \; i \in M,$

$\sigma_{ji} \colon \text{processing route of job} \; j \in J \; \text{on machine} \; i \in M,$

$V \colon \text{big-M}, V = \sum\limits_{j \in J} \sum\limits_{i \in M} p_{ji}.$

#### Decision variables

$C_{\text{max}} \colon \text{makespan},$

$x_{ji} \colon \text{start time of job} \; j \in J \; \text{on machine} \; i \in M,$

$
    z_{ijk} \colon
    \begin{cases}
    1; & \text{if the job} \; j \in J \; \text{precedes the job} \; k \in J \; \text{on machine} \; i \in M \\
    0; & \text{otherwise.}
    \end{cases}
$

$q_{ijk} \colon \text{surplus variable}.$

#### MILP model

$\text{Min } C_{\text{max}}.$

Sujeito a

$x_{j,\sigma_{ji}} \geq x_{j,\sigma_{ji-1}} + p_{j,\sigma_{ji-1}} \; \; \forall j \in J, \; i \in M \mid i \geq 2,$

$V \cdot z_{ijk} + (x_{ji} - x_{ki}) - p_{ki} = q_{ijk} \;\; \forall i \in M, \; j,k \in J \mid j \lt k,$

$q_{ijk} \leq V - p_{ji} - p_{ki} \;\; \forall i \in M, \; j,k \in J \mid j \lt k,$

$C_{\text{max}} \geq x_{j,\sigma_{jm}} + p_{j,\sigma_{jm}},$

$x_{ji}, q_{ijk} \geq 0, \; z_{ijk} \in \{0,1\}.$