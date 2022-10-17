#### Conjuntos e parâmetros

$J \colon \text{conjunto de trabalhos,} \; J = \{1,2,\ldots,n\},$

$M \colon \text{conjunto de máquinas,} \; M = \{1,2,\ldots,m\},$

$p_{ji} \colon \text{tempo de processamento do trabalho} \; j \in J \; \text{na máquina} \; i \in M,$

$
    r_{jil} \colon
    \begin{cases}
    1; & \text{se a operação} \; l \in M \; \text{do trabalho} \; j \in J \; \text{requer a máquina} \; i \in M \\
    0; & \text{caso contrário,}
    \end{cases}
$

$V \colon \text{big-M}, V = \sum\limits_{j \in J} \sum\limits_{i \in M} p_{ji}.$

#### Variáveis de decisão

$C_{\text{max}} \colon \text{makespan},$

$h_{ik} \colon \text{instante de início do trabalho} \; k \in J \; \text{da máquina} \; i \in M,$

$
    x_{jki} \colon
    \begin{cases}
    1; & \text{se o trabalho} \; j \in J \; \text{for sequenciado na ordem} \; k \in J \; \text{na máquina} \; i \in M \\
    0; & \text{caso contrário.}
    \end{cases}
$

#### Modelo de Programação Linear Inteira Mista

$\text{Min } C_{\text{max}}.$

Sujeito a

$\sum\limits_{j \in J} x_{jki} = 1 \;\; \forall i \in M, \; k \in J,$

$\sum\limits_{k \in J} x_{jki} = 1 \;\; \forall i \in M, \; j \in J,$

$h_{ik} + \sum\limits_{j \in J} p_{ji} x_{jki} \leq h_{i{k+1}} \;\; i \in M, \; k \in J \mid k \lt n,$

$ \sum\limits_{i \in M} r_{jil} h_{ik} + \sum\limits_{i \in M} r_{jil} p_{ji} \leq V(1 - \sum\limits_{i \in M} r_{jil} x_{jki}) + V(1 - \sum\limits_{i \in M} r_{ji{l+1}} x_{jk^{'}i}) + \sum\limits_{i \in M} r_{ji{l+1}} h_{ik^{'}} \;\; \forall j,k,k^{'} \in J, \; l \in M \mid l \lt m,$

$h_{in} + \sum\limits_{j \in J} p_{ji} x_{jni} \leq C_{\text{max}},$

$h_{ik} \geq 0, \; x_{jki} \in \{0,1\}.$