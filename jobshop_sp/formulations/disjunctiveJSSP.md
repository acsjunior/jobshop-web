#### Conjuntos e parâmetros

$J \colon \text{conjunto de trabalhos,} \; J = \{1,2,\ldots,n\},$

$M \colon \text{conjunto de máquinas,} \; M = \{1,2,\ldots,m\},$

$p_{ji} \colon \text{tempo de processamento do trabalho} \; j \in J \; \text{na máquina} \; i \in M,$

$\sigma_{ji} \colon \text{roteiro de processamento do trabalho} \; j \in J \; \text{na máquina} \; i \in M,$

$V \colon \text{big-M}, V = \sum\limits_{j \in J} \sum\limits_{i \in M} p_{ji}.$

#### Variáveis de decisão

$C_{\text{max}} \colon \text{makespan},$

$x_{ji} \colon \text{instante de início do trabalho} \; j \in J \; \text{na máquina} \; i \in M,$

$
    z_{ijk} \colon
    \begin{cases}
    1; & \text{se o trabalho} \; j \in J \; \text{precede o trabalho} \; k \in J \; \text{na máquina} \; i \in M \\
    0; & \text{caso contrário.}
    \end{cases}
$

#### Modelo de Programação Linear Inteira Mista

$\text{Min } C_{\text{max}}.$

Sujeito a

$x_{j,\sigma_{ji}} \geq x_{j,\sigma_{ji-1}} + p_{j,\sigma_{ji-1}} \; \; \forall j \in J, \; i \in M \mid i \geq 2,$

$x_{ji} \geq x_{ki} + p_{ki} - V \cdot z_{ijk}  \;\; \forall i \in M, \; j,k \in J \mid j \lt k,$

$x_{ki} \geq x_{ji} + p_{ji} - V(1 - z_{ijk})  \;\; \forall i \in M, \; j,k \in J \mid j \lt k,$

$C_{\text{max}} \geq x_{j,\sigma_{jm}} + p_{j,\sigma_{jm}},$

$x_{ji} \geq 0, \; z_{ijk} \in \{0,1\}.$