#### Conjuntos e parâmetros

$J \colon \text{conjunto de trabalhos,} \; I = \{1,2,\ldots,m\},$

$M \colon \text{conjunto de máquinas,} \; J = \{1,2,\ldots,n\},$

$H \colon \text{tempo discretizado,} \; H = \{0,1,2,\ldots,S\},$

$p_{ij} \colon \text{tempo de processamento da tarefa} \; j \in J \; \text{na máquina} \; i \in M,$

$\sigma_{ij} \colon \text{roteiro de processamento da tarefa} \; j \in J \; \text{na máquina} \; i \in M,$

$S \colon \text{soma total dos tempos de processamento}, S = \sum\limits_{i=1}^m \sum\limits_{j=1}^n p_{ij}.$

#### Variáveis de decisão

$C_{\text{max}} \colon \text{makespan},$

$
    x_{ijk} \colon
    \begin{cases}
    1; & \text{se o trabalho} \; j \in J \; \text{inicia o processamento no tempo} \; t \in H \; \text{na máquina} \; i \in M \\
    0; & \text{caso contrário.}
    \end{cases}
$

#### Modelo matemático exato

$\text{Min } C_{\text{max}}.$

Sujeito a

$\sum\limits_{t \in H} x_{ijt} = 1 \;\; \forall i \in M, \; j \in J,$

$\sum\limits_{t \in H} (t + p_{ji}) x_{ijt} \leq C_{\text{max}} \;\; \forall i \in M, \; j \in J,$

$\sum\limits_{j \in J} \sum\limits_{t^{'} \in T_{ijt}} x_{jit^{'}} \leq 1 \;\; \forall i \in M, j \in J, t \in H \mid T_{ijt} = \{ t - p_{ji} + 1, \ldots, t\},$

$\sum\limits_{t \in H} (t + p_{j,\sigma_{ji-1}}) x_{\sigma_{ji-1}, jt} \leq \sum\limits_{t \in H} t \cdot x_{\sigma_{ji}, jt} \;\; \forall i \in M, j \in J \mid i \geq 2$

$x_{jit} \in \{0,1\}$