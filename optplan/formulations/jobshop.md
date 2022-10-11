#### Conjuntos e parâmetros

$I \colon \text{conjunto de tarefas,} \; I = \{1,2,\ldots,m\},$

$J \colon \text{conjunto de máquinas,} \; J = \{1,2,\ldots,n\},$

$t_{ij} \colon \text{tempo de processamento da tarefa} \; i \in I \; \text{na máquina} \; j \in J,$

$r_{ij} \colon \text{rota de processamento da tarefa} \; i \in I \; \text{na máquina} \; j \in J.$

#### Variáveis de decisão

$x_{ij} \colon \text{instante de término da tarefa} \; i \in I \; \text{na máquina} \; j \in ,$

$
    y_{ikj} \colon
    \begin{cases}
    1; & \text{se a tarefa} \; i \in I \; \text{precede a tarefa} \; k \in I \; \text{na máquina} \; j \in J \\
    0; & \text{caso contrário.}
    \end{cases}
$

#### Modelo matemático exato

$\text{Min } \sum\limits_{i=1}^m x_{i{r_{in}}}.$

Sujeito a

$x_{ir_{i1}} \geq t_{ir_{i1}} \; \; \forall i \in I,$

$x_{ir_{i{j+1}}} \geq x_{ir_{ij}} + t_{ir_{i{j+1}}} \; \; \forall i \in I, \; j \in J \mid j \lt n,$

$x_{kj} \geq x_{ij} + t_{kj} - M(1 - y_{ikj}) \; \; \forall i \in I, \; k \in I, \; j \in J \mid i \neq k,$

$x_{ij} \geq x_{kj} + t_{ij} - My_{ikj} \; \; \forall i \in I, \; k \in I, \; j \in J \mid i \neq k,$

$x_{ij} \geq 0, \; y_{ikj} \in \{0,1\}.$

