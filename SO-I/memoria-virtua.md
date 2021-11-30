# Memória virtual:

Principal resolução foi permitir executar programas maiores que a memória disponível. 
Permite retirar uma parte do programa que está em execução e guardá-la na memória.
Guarda as funcionalidades que são menos utilizadas em um programa na área de swap e deixa apenas as partes principais do programa na memória principal.

> Técnica sofisticada de gerência da memória onde as memórias principal e secundária sã combinadas, dando a ilusão ao usuário de existir uma memória muito maior que a memória principal.
> - Aumenta poder de multiprogramação.
> - Permite a execução de programas maiores que a memória principal.
> - Reduz fragmentação. Já que partes diferentes do mesmo processo podem estar separados em diferentes partições livres, ou seja, não é mais necessária alocação contígua.
> **Por isso a memória virtual é a principal forma de gerenciamento de memória da atualidade.**

## Espaço de endereçamento virtual:

    * Um programa no ambiente de memória virtual não faz referência a endereços físicos de memória, mas apenas endereços virtuais.
    * Endereços virtuais dever ser mapeados para um endereço físico.
    * É como se os processos vivessem na Matrix. Pois o sistema operacional usa uma memória real enquanto o programa opera numa memória virtual não real.
  
## Características:

    * Os programas e suas estruturas de dados não estão mais limitados ao tamanho da memória física disponível, pois o SO usa memória secundária como extensão da memória principal.
    * Comos os programas podem ser maiores que a memória física, apenas parte deles pode estar residente na memória em determinado instante.
    * Quando um programa é executado, só uma parte do código fica esidente na memória principal, permanecendo o restante na memória secundária até o momento de ser referenciado.
    * A existência de endereços virtuais é ignorado pelos programadores de aplicações. Os compiladores e linkers se encarregam de gerar o código executável em função desses endereços e o SO cuida dos detalhes de execução.
  
## Paginação:

 * O espaço de endereçamento virtual e o espaço de enderaçamento real são divididos em blocos do mesmo tamanho, chamados páginas.
 * Todo mapeamento é realizado em nível de página através de tabelas de páginas.
 * Cada página virtual do processo possui uma entrada na tabela de páginas (ETP), com informações de mapeamento que permitem ao sistema localizar a página real correspondente.
 * Toda vez que o programa fizer referência a um endereço virtual, o mecanismo de mapeamento localizará, na ETP da tabela do processo, o endereço físico da página real.
 * Quando uma página não se encontra na memória principal, o sistema deve realizar pelo menos um E/S para buscá-la na memória secundária.
 * Working Set: è interessante manter na memória principal um certo número de páginas que reduza ao máximo a taxa de paginação(troca de páginas da memória principal para a secundária) dos processos.
 * Realocação de Paginas: Um problema é decidir que páginas devem ser removidas da memória principal. Para fins de eficiência, seri interessante escolher páginas que não fossem usadas em um futuro próximo.
 * Algumas estratégias: Aleatória. FIFO. Página usada menos recentemente (LRU). Página menos frequentemente utilizada(LFU), etc.