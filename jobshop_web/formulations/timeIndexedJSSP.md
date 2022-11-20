#### Sets and parameters

$J \colon \text{set of jobs,} \; I = \{1,2,\ldots,m\},$

$M \colon \text{set of machines,} \; J = \{1,2,\ldots,n\},$

$H \colon \text{discretized time,} \; H = \{0,1,2,\ldots,S\},$

$p_{ij} \colon \text{processing time of job} \; j \in J \; \text{on machine} \; i \in M,$

$\sigma_{ij} \colon \text{processing route of job} \; j \in J \; \text{on machine} \; i \in M,$

$S \colon \text{total sum of the processing times}, S = \sum\limits_{j \in J} \sum\limits_{i \in M} p_{ji}.$

#### Decision variables

$C_{\text{max}} \colon \text{makespan},$

$
    y_{ijt} \colon
    \begin{cases}
    1; & \text{if the job} \; j \in J \; \text{starts processing at time} \; t \in H \; \text{on machine} \; i \in M \\
    0; & \text{otherwise.}
    \end{cases}
$

#### MILP model

$\text{Min } C_{\text{max}}.$

Sujeito a

$\sum\limits_{t \in H} y_{ijt} = 1 \;\; \forall i \in M, \; j \in J,$

$\sum\limits_{t \in H} (t + p_{ji}) y_{ijt} \leq C_{\text{max}} \;\; \forall i \in M, \; j \in J,$

$\sum\limits_{j \in J} \sum\limits_{t^{'} \in T_{ijt}} y_{jit^{'}} \leq 1 \;\; \forall i \in M, j \in J, t \in H \mid T_{ijt} = \{ t - p_{ji} + 1, \ldots, t\},$

$\sum\limits_{t \in H} (t + p_{j,\sigma_{ji-1}}) y_{\sigma_{ji-1}, jt} \leq \sum\limits_{t \in H} t \cdot y_{\sigma_{ji}, jt} \;\; \forall i \in M, j \in J \mid i \geq 2,$

$y_{jit} \in \{0,1\}.$