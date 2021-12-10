# Lista de Gerenciamento de Arquivos

## 1. Faça um resumo de 1 página com os pontos principais relacionados ao gerenciamento de arquivos.

Arquivos são instruções ou dados gravados pelo sistema operacional no disco. Estes podem são organizados em diretórios, que podem conter outros diretórios e assim sucessivamente, criando uma árvore de arquivos. Dessa forma a organização lógica e manipulação dos arquivos pelo sistema operacional é facilitada, em consequência seu desempenho aumenta.


O sistema de arquivos é a forma como o sistema operacional estrutura os arquivos no sistema. Estes arquivos podem ser acessados pelas seguintes operações:

* **CREATE**: Criação de um arquivo
* **OPEN**: Abertura de um arquivo
* **CLOSE**: Fechamento de um arquivo
* **READ**: Leitura de um arquivo
* **WRITE**: Gravação em um arquivo
* **DELETE**: Eliminação de um arquivo

Os arquivos possuem atribuições, como: tamanho, proteção, criador e data de criação.

Para a identificação dos tipos de arquivos, existem as extensões. Identificadas por virem após o nome do arquivo precedidas por um ponto final. Cada extensão pode ser lida, gravada e em certos casos executada, essas permissões são dadas ao usuário pelo sistema operacional por motivos de segurança. Arquivos executáveis podem gerar arquivos de leitura, gravação ou execução mesmo que temporariamente, como o editor que utilizo para redigir este texto. O editor consiste em um arquivo executável que pode criar outros arquivos, podendo este ser um texto (*leitura/gravação*) ou um código(*leitura/gravação/execução*).

A manipulação de arquivos, dos arquivos criados, pelo usuário é uma atividade que envolve diretamente o sistema de arquivos do sistema operacional, sendo esta parte a mais visível do mesmo.Ao criar arquivos no disco, informações devem ser armazenadas para o acesso do sistema operacional.

Existem diversas formas de como alocar e organizar as informações no disco, sendo elas de forma contígua ou particionada. Para lidar com esses tipos de alocação, diversas técnicas de gerenciamento de memória/armazenamento foram criadas, o conjunto dessas técnicas mais suas estruturas de implementação compoem o sistema de arquivos.

Além de lidar com o espaço ocupado no disco, o sistema de arquivos também é responsável por gerenciar os espaços livres, já que para a alocação futura de mais informações no disco, o sistema deve saber onde está livre, o quanto está livre e se deve ser alocado algo naquela partição de armazenamento.

Para lidar com o particionamento de arquivos no disco, diversas técnicas foram desenvolvidas, entre elas a **contígua**, a  ***encadeada*** e a ***indexada***. A primeira consiste em armazenar as informações de forma contínua no disco, sem interrupções, porém para isso é sempre necessária uma partição que possa conter o arquivo inteiro. Já a segunda consiste em dividir o arquivo em blocos, cada um deles contendo um ponteiro para o próximo bloco do rquivo, assim sequencialmente lendo-o/gravando-o/executando-o. Já a forma indexada de alocação de arquivos, consiste na mesma divisão em blocos, porém com um endereço unificado de memória que contém um índice de todos os ponteiros para cada parte do arquivo, dessa forma, a leitura/gravação/execução de um programa não necessita ser sequencial.
## 2. Quais as vantagens da alocação de disco encadeada em relação à contígua?

Ao dividir a alocação em blocos através do disco ( _extent_ ), cada bloco contendo um ponteiro para o bloco seguinte, o arquivo pode ser distribuido pelo disco sem a necessidade de ser alocado inteiramente num mesmo espaço de memória, contrário à contígua, que por necessitar de uma alocação inteira na partição disponível, acaba por fragmentar o espaço em disco ou não sendo possível de alocar. Porém sua leitura deve ser estritamente sequencial, já que um ponteiro de um bloco aponta para o próximo.

## 3. Quais as vantagens da alocação de disco indexada em relação à encadeada?

Por conter uma estrutura de única que contém os ponteiros para todos os blocos de um arquivo distribuido pelo disco (_bloco de índice_), a leitura/gravação de uma arquivo não necessariamente deve ser sequencial, pois os ponteiros não mais estão contidos no bloco do arquivo particionado, e sim no _bloco de índice_.

## 4. O que é uma tabela de alocação de arquivos?

Uma **Tabela de Alocação de Arquivos**, do inglês _*F*ile *A*llocation *T*able_ (*FAT*),  é um sistema de arquivos que armazena informações tais como: número do próximo _cluster_ do arquivo, o fim do mesmo, espaço não utilizado em disco e áreas reservadas do disco.
O sistema operacional percorre o ***FAT*** em busca do número do _cluster_ de cada bloco do arquivo que foi distribuído pelo disco até alcançar o final do arquivo. As principais variantes do formato ***FAT*** são o ***FAT12***, ***FAT16*** E ***FAT32***, nomeadas a partir do número de bits de cada elemento da tabela.

## 5. Pesquise quais são e as características dos principais sistemas de arquivos (ex. ntfs, ext4, etc) usados pelos sistema operacionals modernos (Linux, Windows e MacOS X).

***NTFS***: Do inglês _*N*ew *T*echnology *F*ile *S*ystem_, o sistema de arquivos _NTFS_ foi criado pela _Microsoft_ com o intuito de resolver as limitações do sistema de arquivos _FAT32_. Com avanços na área de: **segurança**, já que introduziu suporte à criptografia, na de recuperação de arquivos (***backups***), de forma mais avançada que as previamente conhecidas, no suporte a **discos rígidos maiores**, n a **compressão** de arquivos, tratamento de **falhas** e **erros**, nomes **UNICODE** e etc. O ***NTFS*** então se tornou o sistema de arquivos mais utilizado nos computadores, sendo este o padrão do _Windows_.

***EXT4***: Sistema de arquivos padrão do GNU/Linux, que introduz principalmente a endereçamento de 48-bits aumentando a capacidade de endereçar arquivos maiores. Para diminuir a latência rotacional do disco e a procura do braço ao ler arquivos em busca das _extents_, o ***EXT4*** tem algoritmos de alocação que mantém os blocos de um arquivo próximos uns dos outros o máximo possível.

***exFAT***: Criado para resolver os problemas do _FAT32_ , voltado para disposivitos flash, e com o foco no: suporte a arquivos grandes, maior velocidade e compatibilidade entre os dispositivos. O sistema de arquivos ***exFAT*** é recomendado para dispositivos de armazenamento externo com memória excedente a 4GB como HDs externos.
