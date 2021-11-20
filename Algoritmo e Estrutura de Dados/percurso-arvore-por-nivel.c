#include <stdio.h>
#include <stdlib.h>

// Struct "num" contendo um inteiro "valor"
struct num{
    int valor;
};
typedef struct num Item; // Definindo tipo "Item"

// Struct de cada nó da árvore, contendo um Item e dois nós: esquerdo e direito
struct no{
    Item num;
    struct no *esquerdo;
    struct no *direito
};
typedef struct no No;

// Struct da lista de números que serão inseridos a partir de uma árvore
typedef struct ListaDeNum{
    No *arv;
    struct ListaDeNum *prox;
} ListaDeNum;

ListaDeNum *inicio; // Ponteiro para inicio da lista
ListaDeNum *final; // Ponteiro para o final da lista

// Inicializando lista de numeros contendo os itens da árvore
void iniciarListaDeNum(){

    ListaDeNum *temp;
    temp = (ListaDeNum *)malloc(sizeof(ListaDeNum));

    // Checkando alocação    
    if (temp == NULL){
        printf("Não foi possível alocar!\n");
    }
    // Trocando primeiro item pelo último e vice-versa
    else{
        inicio = temp;
        final = inicio;
    }
}

// Função de inserção na lista
int inserir(No *x){
    
    ListaDeNum *temp;
    temp = (ListaDeNum *)malloc(sizeof(ListaDeNum));

    // Checkando alocação   
    if (temp == NULL){
        printf("Não foi possível alocar!\n");
    }
    else{
        temp->arv = x;
        final->prox = temp;
        final = final->prox;
        temp->prox = inicio;
    }
}

// Função para imprimir os itens da lista
void imprimir(){
    
    ListaDeNum *temp;
    temp = inicio->prox;
    
    while (temp->prox != inicio){
        printf("%d ", temp->arv->num.valor);
        temp = temp->prox;
    }
    
    printf("%d\n\n", temp->arv->num.valor);
}

// Inicializando a árvore
No *arvInitialize(){
    return NULL;
}

// Converte o valor passado como parâmetro para "num"
Item numCreate(int valor){
    Item num;
    num.valor = valor; // Atribuição direta sem ->
    return num;
}

// Função de inserção na árvore
No *inserirArvore(No *root, Item x){
    if (root == NULL){
        No *temp = (No *)malloc(sizeof(No));
        temp->num = x;
        temp->esquerdo = NULL;
        temp->direito = NULL;
        return temp;
    }
    else{
        // Se valor maior que a raiz, insere no mais a direita
        if (x.valor > root->num.valor){
            root->direito = inserirArvore(root->direito, x);
        }
        // Se menor, insere no mais a esquerda 
        else if (x.valor < root->num.valor){
            root->esquerdo = inserirArvore(root->esquerdo, x);
        }
    }
    return root;
}

// Função para limpar a árvore
void apagarArvore(No *root){
    // Se a árvore contiver itens, recursivamente apaga o ramos esquerdo e direito
    if (root != NULL){
        apagarArvore(root->esquerdo);
        apagarArvore(root->direito);
        free(root);
    }
}

// Função para remover item da lista
void RemoveListaDeNum(){
    inicio->prox = inicio->prox->prox;
}

// Função responsável pela impressão por nível da árvore
void printarArvore(No *root, int n){
    int count = 0;
    if (root != NULL){
        ListaDeNum *temp;
        inserir(root);
        temp = inicio->prox;
        while (count < n && temp != inicio){
            if (temp->arv->esquerdo != NULL){
                inserir(temp->arv->esquerdo);
                count++;
            }
            if (temp->arv->direito != NULL){
                inserir(temp->arv->direito);
                count++;
            }
            temp = temp->prox;
        }
    }
    // Imprime a lista
    imprimir();
    // Apagando a árvore depois do print
    apagarArvore(root);

    // Apagando item a item na lista de números
    for (int j = 0; j < n; j++){
        RemoveListaDeNum();
    }
}

int main(){
    iniciarListaDeNum(); // Inicia a lista
    No *root = arvInitialize();// Inicia a árvore

    int numeroCasos, n, x;     // Inicializando variáveis
    scanf("%d", &numeroCasos); // Lendo número de casos de teste
    for (int i = 0; i < numeroCasos; i++){
        iniciarListaDeNum();
        No *root = arvInitialize();
        scanf("%d", &n);
        for (int j = 0; j < n; j++){
            scanf("%d", &x);
            root = inserirArvore(root, numCreate(x));
        }
        printf("Case %d:\n", i + 1);
        printarArvore(root, n);
    }
    return 0;
}