# Exercício de Threads e Semáforos:

## Implementando exemplo 1/2:

![](/home/luis/Imagens/print%20codigo%20SO.png)

De acordo com as aulas do dia 18/10 e 20/10

## Modificando exemplo 1:

![Compilando conforme explicado na aula](/home/luis/Imagens/exemplo%201%20modificado.png)

Adicionando semáforos e duplicando as threads.

## Compilando exemplo 1:

![](/home/luis/Imagens/compilando%20exemplo%201.png)

## Executando exemplo 1:

![](/home/luis/Imagens/executando%20exemplo%201.png)

### Resultados:

Ao implementar duas seções críticas nas funções `Thread0()`e `Thread1()`, a execução manteve os outputs das threads em ordem:

```c

sem_t semid;

void * Thread0() {
	int i=0;
	sem_wait(&semid);// Iniciando seção crítica, P.

	for(i=1;i<10;i++){
		printf(" Thread0 - %d\n",i);
		sleep(3);
	}
	sem_post(&semid); // Finalizando seção crítica, S
}

void * Thread1(){
	int i=0;
	sem_wait(&semid); // Iniciando seção crítica, P.

	for(i=10;i<20;i++){
		printf(" Thread1 - %d\n",i);
		sleep(1);
	} 
	sem_post(&semid); // Finalizando seção crítica, S.
} 
```

Dentro da função `main()`, mais duas threads são criadas, ret2 e ret3, executando as funções `Thread0()` e `Thread1()` respectivamente:

```c
int main(){
    pthread_t t0, t1, t2, t3;
    int ret0, ret1, ret2, ret3;
    
    sem_init(&semid, 0, 1);

    ret0 = pthread_create(&t0, NULL, Thread0, NULL);
    ret1 = pthread_create(&t1, NULL, Thread1, NULL);
    ret2 = pthread_create(&t2, NULL, Thread0, NULL); // Thread0 duplicada
    ret3 = pthread_create(&t3, NULL, Thread1, NULL); // Thread1 duplicada

    pthread_join(t0, NULL);
    pthread_join(t1, NULL);
    pthread_join(t2, NULL);
    pthread_join(t3, NULL);

    printf("Main acabou\n");
}
```

## Modificando exemplo 2:

![](/home/luis/Imagens/exemplo%202%20modificado.png)

## Compilando exemplo 2:

![](/home/luis/Imagens/compilando%20exemplo%202.png)



## Executando exemplo 2:

![](/home/luis/Imagens/executando%20exemplo%202.png)

### Resultados:

Os outputs de cada uma das funções foram intercalados e duplicados. Primeiro todos os outputs da `Thread1()`e depois todos os outputs da `Thread2()`. Após isso o processo se repetiu pois duas threads a mais, executando as funções `Thread1()` e `Thread2()`, foram adicionadas.

```c
int main(){ 
	pthread_t t1,t2, t3, t4; 
	int ret1,ret2, ret3, ret4; 

	sem_init(&semid, 0, 1); 
	
	ret1 = pthread_create(&t1,NULL, Thread1, NULL); 
	ret2 = pthread_create(&t2,NULL, Thread2, NULL); 
	ret3 = pthread_create(&t3,NULL, Thread1, NULL); // Thread1 duplicada
	ret4 = pthread_create(&t4,NULL, Thread2, NULL); // Thread2 duplicada

	pthread_join(t1,NULL); 
	pthread_join(t2,NULL); 
	pthread_join(t3,NULL); 
	pthread_join(t4,NULL); 
	
	printf("Main acabou\n"); 
} 
```

## Conclusão:

Devido o tempo de espera de cada função, o sistema operacional as executou com prioridade diferente sobre as outras. 

No exemplo 1, o tempo de `sleep()` da `Thread0()` é maior que o da `Thread1()`, o que resultou em outputs sequenciais, primeiro todas as threads que executavam `Thread0()` e depois todas que executavam `Thread1()`. 

Já no exemplo 2, como o tempo de `sleep()` de ambas funções eram o mesmo, o resultado foi um input intercalado.

> Manaus/AM - 26/10/2021
