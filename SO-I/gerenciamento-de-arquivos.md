# Lista de Gerenciamento de Arquivos

## 1. Faça um resumo de 1 página com os pontos principais relacionados ao gerenciamento de arquivos.

## 2. Quais as vantagens da alocação de disco encadeada em relação à contígua?

Ao dividir a alocação em blocos através do disco ( _extent_ ), cada bloco contendo um ponteiro para o bloco seguinte, o arquivo pode ser distribuido pelo disco sem a necessidade de ser alocado inteiramente num mesmo espaço de memória, contrário à contígua, que por necessitar de uma alocação inteira na partição disponível, acaba por fragmentar o espaço em disco ou não sendo possível de alocar. Porém sua leitura deve ser estritamente sequencial, já que um ponteiro de um bloco aponta para o próximo.

## 3. Quais as vantagens da alocação de disco indexada em relação à encadeada?

Por conter uma estrutura de única que contém os ponteiros para todos os blocos de um arquivo distribuido pelo disco (_bloco de índice_), a leitura/gravação de uma arquivo não necessariamente deve ser sequencial, pois os ponteiros não mais estão contidos no bloco do arquivo particionado, e sim no _bloco de índice_.

## 4. O que é uma tabela de alocação de arquivos?

Uma **Tabela de Alocação de Arquivos**, do inglês _*F*ile *A*llocation *T*able_ (*FAT*),  é um sistema de arquivos que armazena informações tais como: número do próximo _cluster_ do arquivo, o fim do mesmo, espaço não utilizado em disco e áreas reservadas do disco.
O SO percorre o ***FAT*** em busca do número do _cluster_ de cada bloco do arquivo que foi distribuído pelo disco até alcançar o final do arquivo. As principais variantes do formato ***FAT*** são o ***FAT12***, ***FAT16*** E ***FAT32***, nomeadas a partir do número de bits de cada elemento da tabela.

## 5. Pesquise quais são e as características dos principais sistemas de arquivos (ex. ntfs, ext4, etc) usados pelos SOs modernos (Linux, Windows e MacOS X).