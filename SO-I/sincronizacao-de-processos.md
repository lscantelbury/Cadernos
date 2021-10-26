# Sincronização de processos:

## Sincronização de processos/threads:

* Um processo cooperativo ou thread pode afetar ou ser afetado pelos outros processos/threads que estão executando no sistema.
* Processos/threads podem compartilhar dados e o acesso concorrente aos dados pode resultar em inconsistências.
* Há necessidade de mecanismos para ordenar o acesso a dados compartilhados por processos ou threads concorrentes.

## Fundamentos:

* Relembranco o problema do produtor e do consumidor:
	* Produtor:
		```java
		while(count == Buffer_Size);
		++count;
		Buffer[in~= item;
		In = (in+1) % Buffer_Size;
		```
	* Consumifdor:
		```java
		while(count == 0);
		--count;
		item = Buffer[out];
		out = (out + 1_ % Buffer_Size;
		```
* Isoladamente, os procedimentos estão corretos, porém, pode ocorrer um problema no acesso à variável compartilhada **count**.
* A implementação em linguagem de máquina para:
	* ++count:
	> Reg1 = Count;
	> Reg1 = Reg1 + 1;
	> Count = Reg1;
	* --count:
	> Reg2 = Count;
	> Reg2 = Reg2 - 1;
	> Count = Reg2;
	- Ex: Supondo inicialmente count=5. Uma execução seria:
	
|s1 |produtor  |Reg1 = count  |Reg1 = 5 |
|:--|:--------:|:------------:|--------:|
|s2 |produtor  |Reg1 = Reg1 +1|Reg1 = 6 |
|s3 |consumidor|Reg2 = count  |Reg2 = 5 |
|s4 |consumidor|Reg2 = Reg2 -1|Reg2 = 4 |
|s5 |produtor  |count = Reg1  |count = 6|
|s6 |consumidor|count = Reg2  |count = 4|

* O resultado incorreto se deve ao acesso concorrente à variável count.
* O resultado da execução depende da ordem específica em que o acesso ocorre. A isso se dá o nome de condição de corrida (race condition).
* Para evitar esse problema é necessário que cada um dos procedimentos possa manipular o recurso compartilhado.

## Seções Críticas:
* Para controlar o acesso a um recurso compartilhado, declaramos uma seção de código como sendo crítica, e em seguida, é controlado o acesso a essa região.
* Nessa região crítica é feito o acesso ao recurso compartilhado.
* Quando um processo ou thread estiver executandoem sua seção crítica, nenhuma outra terá premissão para executar em sua seção crítica.
* Assim, a execução das regiões críticas pelas threads é mutuamente exclusiva no tempo.

## Semáforos:
* Ferramenta de sincrnização, baseada em uma variável inteira, que só é acessada por duas operações-padrão: *P* e *V*(P - *proberen*, ou test; V - *verhogen*, ou incremento).
* Definições de *P* e *V*:
	> P(S): while S <= 0 do no-op;
	> S--;
	>
	> V(S): S++
* As modificaçoes no valor inteiro do semáforo nas operações *P* e *V* devem ser executadas de forma indivisível.
* A estratégia geral para usar um semáforo binário no controla de acesso a ua seção crítica é o seguinte:
	- Supor S inicializado em 1:
	> Semaphore S:
	>
	> P(S);
	> CriticalSection();
	> V(S);

## Semáforos no Linux:
* Exemplo de sincronização com semáforos:
```c
#include <pthread.h>
#include <stdio.h>
#include <time.h>
#include <semaphore.h>

sem_t semid; // Variavel para semaforo
void * Thread1(){
	int i = 0;

	sem_wait(&semido); // Inicio regiao critica
	for (i = 1; i < 10; i++){
		printf("T2 - %d\n", i);
		sleep(1);
	}
	sem_ost(&semid);// Fim regiao critica
}

void * Thread2(){
	int i = 0;

	sem_wait(&semid);
	for (i = 1; i < 10; i++){
		printf("T2 - %d\n", i);
		sleep(1);
	}
	sem_post(&semid);
}

int main(){
	pthread_t t1, t2;
	int ret1, ret2;

	// Cria semaforo iniciado com 1 
	sem_init(&semid, 0, 1);

	ret1 = pthread_create(&t1, NULL, Thread1, NULL);
	ret2 = pthread_create(&t2, NULL, Thread2, NULL);
	pthread_join(t1, NULL);
	pthread_join(t2, NULL);
	printf("Main acabou\n");
}

```

## Deadlocks:

* Impasse causado quando dois oumais processosestão esperando indeinidamente por um evento que somente pode ser causado por um dos processos em espera.
	- Exemplo:
	> P0		P1
	> P(S);		P(Q);
	> P(Q);		P(S);
	> .			.
	> .			.
	> .			.
	> V(S);		V(Q);
	> V(Q)		V(S);
	- P(Q) de P0 esperará por V(Q) e P1, e P(S) de P1 esperará por V(S) de P0.
* Desenvolvedor dev ter cuidado!
---
# Problemas Clássicos de Sincronização:

## Produtor/Consumidor com buffer limitado:
* Inicialização:
	- Mutex = 1 // Semaforo para acesso sincronizado ao buffer
	- Empty = BUFFER_SIZE // Semaforo para indicar posições vazias do buffer
	- Full = 0 // Semaforo para indicar posições cheias do buffer

### Produtor:
	```java
	public void enter (Object item){
		empty.P();
		mutex.P();

		// add an item to the buffer

		mutex.V();
		full.V*(;
	}
	```
### Consumidor: 
	```java 
	public Object remove(){
		full.P();
		mutex.P();

		// remove an item from the buffer
		mutex.V;
		empty.V();
	}
	```
## Problema dos Leitores e Escritores:
* Problema em que há a disinção entre processs que desejam somente realizar uma leitura de um recurso compartilhado (leitores), e os que desejam atualizá-lo (escritores).
	- Nesse caso, leitores podem acessar o recurso compartilhado ao mesmo tempo, mas escritores deverão ter acesso exclusivo para evitar problemas.
	- Variável: readerCount - Variável para controlar se há leitores acessando o recurso compartilhado.
	- Semáforos:
		- Mutex - Semáforo usado para sincronizar o acesso à readerCount.
		- Escritex - Semáforo para sincronizar o acessos dos escritores.
* Leitores:
	```c 
	while(true){
		mutex.P();
		++readerCount;

		// Se for o 1º leitor, avisa a todos o acesso de leitura

		if (readerCount == 1){
			escritex.P();

		mutex.V();

		// Lendo recurso compartilhado

		mutex.P();
		--readerCount;

		// Se for o ultimo leitor, avisa a todos que não há acesso de leitura

		if (readerCount == 0)
			escritex.V(0;

		mutex.V();
	}
* Escritores:
	```c
	while(true){
		escritex.P();
		// Escrevendo
		escritex.V();
	}
	```
---
## Jantar dos filósofos:
* Exemplo de uma vasta classe de problemas de controle de concorrência.
	- É uma representação simples da necessidae de alocar vários recursos entre vários processos, sem incorrer em deadlocks ou paralisação.
	- Quando um filósofo está com fome ele teta pegar os garfos próximos de si (garfos entre seus colegas da esquerda e direita). Só um garfo pode ser pego por vez, e esse não pode estar em uso. Quando termina de comer, o filósofo solta os dois garfos.
* Solução:
	```c
	while (true){
	// pega o garfo esquerdo
	chopStick[i].P();
	// pega o garfo direito
	chopStick[(i + 1) % 5].P();
	// Come
	// devolve o garfo direito
	chopStick[(i + 1) % 5].V();
	//pensa
	}
	```
* Problema?
