#include <iostream>

using namespace std;

//variaveis universais
int produtosRegistrados, codigo, quantidade, tamanho;
float preco, matriz[0][3];

//Funçao para ler e atribuir os valores das variaveis
void lerProduto(){
    cout << "Código do produto: ";
    cin >> codigo;
    cout << "Quantidade do produto: ";
    cin >> quantidade;
    cout << "Preco do produto: ";
    cin >> preco;
    if (preco > 10){
        tamanho++;
    }
}

//Funçao para criar ledger de produtos
void adicionarProdutoNaMatriz(){
    matriz[produtosRegistrados][0] = codigo;
    matriz[produtosRegistrados][1] = quantidade;
    matriz[produtosRegistrados][2] = preco;
    cout<<" "<<endl;
}

//Funçao para printar matriz
void printarMatriz(){
    cout << "CODIGO/QUANTIDADE/PRECO:"<<endl;
    cout <<""<<endl;
    for (int i = 0; i <= produtosRegistrados; i++){
        cout <<"Produto "<< (i + 1) << " - "<< matriz[i][0]<<"    "<<matriz[i][1]<<"    "<<matriz[i][2]<<"\n";
    }
}

//Funçao para criar matriz com produtos acima de 10 reais
void maisDeDezReais(float* ptr){
    for (int i = 0; i <= produtosRegistrados; i++){
        if (matriz[i][2] > 10){
            *(ptr + i) = matriz[i][2];
        }
    }
}

//Funçao para printar produtos acima de 10 reais
void printarMatrizDezReais(float* ptr){
    for (int i = 0; i < tamanho; i++){
        cout<<*(ptr + i)<<endl;
    }
}

//Funçao para calcular media de produtos acima de 10 reais
float media(float* ptr){
    float aux;
    float soma = 0;
    for (int i = 0; i < tamanho; i++){
        soma += *(ptr + i);
        aux++;
    }
    return (soma/aux);
}
//CODIGO PRINCIPAL
int main(){
    float *pointer = NULL;
    char resposta = 's';
    do{
        lerProduto();
        adicionarProdutoNaMatriz();
        cout <<"Deseja resgistrar outro produto?(s/n)";
        cin >> resposta;
        cout<<" "<<endl;
        if (resposta == 's'){
            produtosRegistrados++;
        }
    }while(resposta == 's');
    pointer = new float[tamanho];
    printarMatriz();
    cout<<" "<<endl;
    maisDeDezReais(pointer);
    cout<<"-Preços acima de 10 reais:"<<endl;
    printarMatrizDezReais(pointer);
    cout<<" "<<endl;
    cout<<"-Média de preço dos produtos acima de 10 reais"<<endl;
    cout<<media(pointer)<<endl;
}
