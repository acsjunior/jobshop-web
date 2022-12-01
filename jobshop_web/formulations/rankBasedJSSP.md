#### Sets and parameters

$J \colon \text{set of jobs,} \; J = \{1,2,\ldots,n\},$

$M \colon \text{set of machines,} \; M = \{1,2,\ldots,m\},$

$p_{ji} \colon \text{processing time of job} \; j \in J \; \text{on machine} \; i \in M,$

$
    r_{jil} \colon
    \begin{cases}
    1; & \text{if the operation} \; l \in M \; \text{of job} \; j \in J \; \text{requires machine} \; i \in M \\
    0; & \text{otherwise,}
    \end{cases}
$

$V \colon \text{big-M}, V = \sum\limits_{j \in J} \sum\limits_{i \in M} p_{ji}.$

#### Decision variables

$C_{\text{max}} \colon \text{makespan},$

$h_{ik} \colon \text{start time of job} \; k \in J \; \text{on machine} \; i \in M,$

$
    w_{jki} \colon
    \begin{cases}
    1; & \text{if the job} \; j \in J \; \text{is sequenced in order} \; k \in J \; \text{on machine} \; i \in M \\
    0; & \text{otherwise.}
    \end{cases}
$

#### MILP model

$\text{Min } C_{\text{max}}.$

Subject to

$\sum\limits_{j \in J} w_{jki} = 1 \;\; \forall i \in M, \; k \in J,$

$\sum\limits_{k \in J} w_{jki} = 1 \;\; \forall i \in M, \; j \in J,$

$h_{ik} + \sum\limits_{j \in J} p_{ji} w_{jki} \leq h_{i{k+1}} \;\; i \in M, \; k \in J \mid k \lt n,$

$ \sum\limits_{i \in M} r_{jil} h_{ik} + \sum\limits_{i \in M} r_{jil} p_{ji} \leq V(1 - \sum\limits_{i \in M} r_{jil} w_{jki}) + V(1 - \sum\limits_{i \in M} r_{ji{l+1}} w_{jk^{'}i}) + \sum\limits_{i \in M} r_{ji{l+1}} h_{ik^{'}} \;\; \forall j,k,k^{'} \in J, \; l \in M \mid l \lt m,$

$h_{in} + \sum\limits_{j \in J} p_{ji} w_{jni} \leq C_{\text{max}},$

$h_{ik} \geq 0, \; w_{jki} \in \{0,1\}.$