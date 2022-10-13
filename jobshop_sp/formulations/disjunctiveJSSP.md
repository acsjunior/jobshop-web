#### Conjuntos e parâmetros

$I \colon \text{conjunto de tarefas,} \; I = \{1,2,\ldots,m\},$

$J \colon \text{conjunto de máquinas,} \; J = \{1,2,\ldots,n\},$

$p_{ij} \colon \text{tempo de processamento da tarefa} \; i \in I \; \text{na máquina} \; j \in J,$

$\sigma_{ij} \colon \text{roteiro de processamento da tarefa} \; i \in I \; \text{na máquina} \; j \in J,$

$V \colon \text{valor grande o suficiente para garantir as restrições disjuntivas}, V = \sum\limits_{i=1}^m \sum\limits_{j=1}^n p_{ij}.$

#### Variáveis de decisão

$C_{\text{max}} \colon \text{makespan},$

$x_{ij} \colon \text{instante de início da tarefa} \; i \in I \; \text{na máquina} \; j \in J,$

$
    z_{jik} \colon
    \begin{cases}
    1; & \text{se a tarefa} \; i \in I \; \text{precede a tarefa} \; k \in I \; \text{na máquina} \; j \in J \\
    0; & \text{caso contrário.}
    \end{cases}
$

#### Modelo matemático exato

$\text{Min } C_{\text{max}}.$

Sujeito a

$x_{i,\sigma_{ij}} \geq x_{i,\sigma_{ij-1}} + p_{i,\sigma_{ij-1}} \; \; \forall i \in I, \; j \in J \mid j \geq 2,$

$x_{ij} \geq x_{kj} + p_{kj} - Vz_{jik}  \;\; \forall j \in J, \; i,k \in I \mid i \lt k,$

$x_{kj} \geq x_{ij} + p_{ij} - V(1 - z_{jik})  \;\; \forall j \in J, \; i,k \in I \mid i \lt k,$

$C_{\text{max}} \geq x_{i,\sigma_{in}} + p_{i,\sigma_{in}},$

$x_{ij} \geq 0, \; z_{ikj} \in \{0,1\}.$