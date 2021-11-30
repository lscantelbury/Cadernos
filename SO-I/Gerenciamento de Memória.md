# Gerenciamento de Memória:

As técnicas de gerenciamento de memória, apresentadas na primeira parte da aula _Gerência de Memória, parte 1_, visam executar o máximo de programas possíveis na memória principal simultâneamente, mesmo sendo eles maiores que o espaço disponível.

### Qual o principal problema no gerenciamento de memória?

Ao alocar programas na memória, o particionamento deve ser eficiente o suficiente para fragmentar o mínimo possível o espaço e ainda assim alocar todos os programas que o usuário queira executar. Para isso, diversas estratégias de escolha de particionamento/alocação foram criadas, dentre elas: 

- **Best-fit**: Aloca o programa na partição em que deixará o menor espaço livre possível.

- **Worst-fit**: Aloca o programa na partição em que deixará o maior espaço livre possível.

- **First-fit**: Aloca o programa na primeira partição com espaço suficiente.

### Qual a principal vantagem da Alocação Particionada Dinâmica em relação à Alocação Particionada Estática?

* **Alocação Particionada Estática**: O tamanho da partição é definido em tempo de compilação de acordo com as variáveis do programa, gerando uma partição do tamanho exato necessário para todas as features do programa.

* **Alocação Particionada Dinâmica**: O tamanho da partição é definido em tempo de execução de acordo com as varíaveis que estão sendo requeridas pelo programa, gerando uma partição do tamanho exato necessário para as features que estão sendo utilizadas pelo programa.

> A principal vantagem da alocação dinâmica é que partições com tamanho maior que o necessário para a utilização do programa pelo usuário não são criadas, deixando mais espaço livre na memória e diminuindo os problemas de fragmentação.

### Quais as limitações que a técnica de swap supera em relação às técnicas de gerenciamento anteriores?

* **Área de swap**: Área do disco de memória em que programas podem ser armazenados de forma temporária enquanto a memória principal utiliza o espaço liberado pelo programa guardado na swap.

> A principal vantagem da swap é a poder executar um programa desejado pelo usuário mesmo se não houver uma partição com espaço o suficiente para alocá-lo. Ao retirar um programa que não está em foco e guardá-lo na área de swap (swap out), espaço é liberado na memória principal para alocar o programa desejado. Quando requerido o programa alocado na swap, este é retirado do disco (swap in) e injetado alocado em alguma partição da memória principal, caso não haja partição de com espaço suficiente para sua alocação, outra swap será executada com um dos programas que estão alocados na memória principal.

## 
