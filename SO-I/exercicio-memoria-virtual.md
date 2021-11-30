# Lista sobre memórias:
> Luis Henrique Scantelbury de Almeida<br />
> Sistemas de informação

1. Explique resumidamente, com suas palavras, as vantagens da memória virtual em relação às técnicas anteriores de gerenciamento de memória:

   > 1. A técnica de memória virtual, permite a execução de programas maiores que a memória principal disponível do dispositivo, já que utiliza parte da memória secundária para armazenar segmentos de menor frequência de uso de um programa em execução.
   > 1. Como a a memória virtual trabalha com endereços virtuais que correspondem a segmentos do conjunto memória principal + secundária do dispositivo, sendo essas não necessariamente contíguas, a fragmentação da memória é reduzida. A possibilidade de armazenar partes de um programa em diferentes partições da memória física, há maior utilização dos espaços livres tanto do disco quando da memória principal.
   > 1. Por não ser necessária memória principal de tamanho suficiente para abrigar o programa inteiro, os desenvolvedores de software podem gerar aplicações sem se preocupar tanto com o espaço disponível de memória principal, pois o gerenciamento da mesma será feito pelo SO, que lidará diretamente com a memória física. O programa em si trabalha com endereços virtuais, como se houvesse uma memória maior do que a disponível no disco.
   > 1. Se necessária alocação de uma parte do programa que está na swap, este é armazenado em uma partição disponível independente da ordem equivalente na memória virtual, pois o SO realiza a paginação e a correspondência de endereços. Dessa forma, uma parte p2 do programa pode estar armazenada antes de uma parte p1 do mesmo sem prejudicar sua execução.
   > 1. A alocação de segmentos mais frequentemente usados de um programa na memória principal, permite que o usuário desenvolva a maior parte das suas tarefas sem enfretar gargalos, os quais seriam causados caso todos o programas na memória fossem alocados inteiramente na mesma.

1. Pesquise mais detalhes sobre o funcionamento de memória virtual no Linux.
 
   > No linux, ao executar o comando `free -` no terminal, são exibidas duas linhas contendo o espaço utilizado/livra nas memórias principal e swap. As quais são gerenciadas como processo pela MMU (_Memory Management Unity_), a qual fornece uma tabela de páginas no endereço físico correspondentes às da memória virtual de um processo. Ao terminar de escrever em uma região, esta já pode ser lida por outros processos, pois as arquiteturas MMU suportam tal dinâmica, denomidada _Memory Mapping_. Esses dados podem ser compartilhados entre programas simultâneamente por 2 ou mais programas caso essas informações estejam no mesmo escopo de memória, caso contrário, é gerado um _Segmentation Fault_. O comando supracitado também exibe os dados _shared_, sendo estes os que falei anteriormente.
   > Outra funcionalidade interessante da virtualização no linux são os sistemas de arquivos pessoais. Ao montar um pendrive no linux, sua árvore de arquivos é exibida no diretório `/mnt` do computador e seu conteúdo pode ser acessado livremente, mesmo não havendo nada gravado no disco, isso consiste numa virtualização de um sistema de arquivos.
   > Outro exemplo é o diretório `/proc`, este se desmontado, não possui arquivos registrados nele, porém se montado, exibe um diretório para cada processo em execução _on the fly_ através do comando `cat /proc`.

1. Pesquise mais detalhes sobre o funcionamento de memória virtual no Windows.
   
   > Similar à swap empregada no Linux, o Windows possui a mecânica de paginação. Esta é configurável através dos seguintes passos:
   > `Este Computador -> Propriedades -> Configurações avançadas de sistema -> Avançado -> Configurações de desempenho -> Avançado -> Memória virtual -> Alterar`.
   > Ao desmarcar a opção de gerenciamento automático, é possível personalizar o tamnho total do arquivo de paginação para cada partição do sistema, sendo o mínimo permitido 16MB.
   > Embora a customização da paginação/swap do Windows não seja introduzida na instalação como o Windows, a interface gráfica é de melhor compreensão que a do Linux e de uso mais simples.
   > O arquivo de paginação do Windows se chama _pagefile.sys_, e é um arquivo oculto, pois é protegido, porem pode ser vizualidado se configurar para exibição de arquivos protegidos do sistema operacional nem _C:_.