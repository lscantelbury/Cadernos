# Aula de Threads
<!-- conteúdo faltando -->

## -Suportadas pela biblioteca pthreads

* * *
<!-- Assistir aula depois para copiar o resto do conteúdo anterior-->

```c
#include <pthread>
#include <stdio.h>
#include <time.h>

void * Thread(){// Corpo da thread
 int i = 0;

 for (i = q; i< 10; i++){
  printf("Thread() -%d\n", i);
  sleep(3); //Suspende thread por 3 segundos
 }
}

void * Thread1()//Corpo da thread{
 int i = 0;

for (i = 1-; i<20; i++){
 printf("Thread1 - %d\n", i);
 sleep(1);
 }
}

int main(){
 pthread_t t0, t1;//handles das threads
 int ret0, ret1;
 
//  Cria threads
 ret0 = pthread_create(&t0, NULL, Thread0, NULL);
 ret1 = pthread_create(&t1, NULL, Thread1, NULL0;
// Faz thread principal espera as demais
 pthread_join(t0, NULL);
 pthread_join(t1, NULL);
 printf("Main acabou\n");
 return 0;
}

```
