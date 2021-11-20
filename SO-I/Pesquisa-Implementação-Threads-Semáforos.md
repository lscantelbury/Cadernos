# Implementação de Threads e Semáforos em Python:

A biblioteca "threading", vem nativamente no python e nos permite
implementar _threads_ e _semáforos_ de forma simples e intuitiva.

A seguir uma demonstração da biblioteca, utilizando-a para resolver problemas clássicos de concorrência:

---

## Problema Leitor/Escritor:

```python
from random import randint
from threading import Thread, Semaphore # Importando as classes Thread e Semaphore da biblioteca threading
import time
from Relogio import Relogio # Classe de cronômetro/timer

podeLer = Semaphore(1) # Semáforo inicializado com valor 1, indica se a lista pode ser lida no momento

podeEscrever = Semaphore(0) # Semáforo inicializado com valor 0, indica se a lista pode ser escrita no momento

listaDisponivel = Semaphore(1) # Semáforo inicializado com valor 1, indica se a lista não está sendo utilizada no momento

class Leitor(Thread): # Classe Leitor, filha da classe Thread
    def __init__(self, lista): # Inicializando a classe filha
        Thread.__init__(self) # Inicializando a classe pai
        self.lista = lista # Passando lista como parâmetro

    def run(self): # Função run é onde deve ser colocado o código principal a ser executado pela Thread

        while True:

            # Método acquire decrementa 1 do valor passado para o semáforo
            podeLer.acquire() # Menos pode ser lido
            listaDisponivel.acquire() # Lista está indisponível no momento

            soma = 0
            for i in self.lista: soma += i # Soma todos os itens da lista 
            print(soma)
            time.sleep(1)

            # Método release adiciona 1 ao valor passado para o semáforo
            listaDisponivel.release() # Lista já pode ser utilizada
            podeEscrever.release() # Lista já pode ser escrita

class Escritor(Thread): # Classe Escritor, filha da classe Thread
    def __init__(self, lista):
        Thread.__init__(self)
        self.lista = lista

    def run(self):
        while True:

            podeEscrever.acquire() # Menos um pode ser escrito
            listaDisponivel.acquire() # Lista indisponível no momento

            self.lista.pop(0) # Retira o primeiro elemento da lista
            self.lista.append(randint(0,10)) # Adiciona número aleatório entre 0 e 10 ao final da lista
            time.sleep(1)
            print(self.lista)

            listaDisponivel.release() # Lista já pode ser utilizada
            podeLer.release() # Lista já pode ser lida

def main():
    time = Relogio(10) # O programa irá rodar por 10 segundos
    time.start()

    lista = [1,2,3]
    print(lista)

    leitor1 = Leitor(lista)
    leitor1.start()

    leitor2 = Leitor(lista)
    leitor2.start()

    escritor1 = Escritor(lista)
    escritor1.start()

    escritor2 = Escritor(lista)
    escritor2.start()

main()
```

## Output:

![Leitor/Escritor](/home/luis/Imagens/leitor-escritor.png)

---

## Problema Produtor/Consumidor:

```python
from threading import Thread
from threading import Semaphore
from Relogio import Relogio
import time
import random

lista = []
podeProduzir = Semaphore(10) # Indica que 10 podem ser produzidos 
podeConsumir = Semaphore(0) # Indica que 0 podem ser consumidos inicialmente
listaDiponivel = Semaphore(1) # Indica se a lista está sendo utilizada no momento

class Produtor(Thread):
    def __init__(self, lista, num):
        Thread.__init__(self)
        self.lista = lista
        self.num = num

    def run(self):
        while True:
            podeProduzir.acquire() # Produziu 1, subtrai 1 dos que ainda podem produzir
            listaDiponivel.acquire() # Lista está sendo utilizada, reservá-la para este processo

            self.lista.append(random.randint(0, 10))# Adiciona número aleatório de 0 a 10 ao final da lista
            print(f"Produtor {str(self.num)} adicionou {str(self.lista[-1])}: {str(self.lista)}")
            time.sleep(0.5)

            listaDiponivel.release() # Terminado o processo, lista está liberada
            podeConsumir.release() # Mais 1 pode ser consumido

class Consumidor(Thread):
    def __init__(self, lista, num):
        Thread.__init__(self)
        self.lista = lista
        self.num = num

    def run(self):
        ultimo = None
        while True:
            if len(lista) == 10:break
            podeConsumir.acquire() # Menos 1 pode ser consumido
            listaDiponivel.acquire() # Lista está sendo utilizada, reservá-la para este processo

            ultimo = self.lista.pop(0) # Retira o primeiro item da lista
            print(f"Consumidor {str(self.num)} retirou {str(ultimo)}: {str(self.lista)}")
            time.sleep(0.5)

            listaDiponivel.release() # Lista já pode ser utilizada
            podeProduzir.release() # Mais 1 item pode ser produzido


def main():
    timer = Relogio(10) # O programa vai executar por 10 segundos
    timer.start()

    produtor1 = Produtor(lista, 1)
    produtor1.start()

    consumidor1 = Consumidor(lista, 1)
    consumidor1.start()

    produtor2 = Produtor(lista, 2)
    produtor2.start()

    consumidor2 = Consumidor(lista, 2)
    consumidor2.start()

    exit()

main()
```

## Output:

![Produtor/Consumidor](/home/luis/Imagens/produtor-consumidor.png)

---

## Problema do Jantar dos Filósofos:

```python
from threading import Thread, Semaphore
import random
import time

class Filosofo(Thread):
    comendo = True # Indica se todos estão comendo
    def __init__(self, nome,  index, garfoEsquerdo, garfoDireito):
        Thread.__init__(self)
        self.nome = nome
        self.index = index
        self.garfoEsquerdo = garfoEsquerdo
        self.garfoDireito = garfoDireito

    def run(self):
        while self.comendo:
            time.sleep(random.randint(1,5)) # Tempo inicial que o filósofo pensa.
            print(f'Filósofo {self.nome} quer comer.')
            self.comer() # Filósofo começa a comer.

    def comer(self):
        # Se ambos os semáforos (talheres) estiverem livres, o filósofo come.
        esquerdo, direito = self.garfoEsquerdo, self.garfoDireito

        while self.comendo:
            esquerdo.acquire() # Indica que o garfo à sua esquerda não pode ser utilizado 

            disponivel = direito.acquire(False) # Verifica disponibilidade do garfo direito
            if disponivel:
                break  

            # Caso o garfo direito não esteja disponível, solta o garfo esquerdo
            esquerdo.release()

            # Filósofo troca os talheres
            print(f'Filósofo {self.nome} troca os talheres.')
            esquerdo, direito = direito, esquerdo 
        else:
            return

        print(f'Filósofo {self.nome} come.')
        time.sleep(5)
        print(f'Filósofo {self.nome} começa a pensar.')

        # Solta os dois talheres depois de comer
        direito.release()
        esquerdo.release()

def main():
    # Inicializando vetor de semáforos(talheres)
    talheres = [Semaphore() for n in range(5)]

    # A divisão modular -> (i+1)%5 é usada para pegar circularmente os talheres direito e esquerdo entre 1-5
    nome=["Sócrates", "Platão", "Aristóteles", "Epíteto", "Tales"] # Nomes para cada um dos filósofos
    filosofos = [Filosofo(nome[i], i, talheres[i % 5],
                talheres[(i+1) % 5])
                for i in range(5)
                ]

    # Inicializa as threads de cada filósofo
    Filosofo.comendo = True
    for filosofo in filosofos:
        filosofo.start()
    time.sleep(10)
    Filosofo.comendo = False

    print("Todos comeram.")

main()
```

## Output:

![Jantar dos Filósofos](/home/luis/Imagens/jantar-dos-filosos.png)

> **Sistemas Operacionais I**
> 
> Luís Henrique Scantelbury de Almeida
> 
> Luã Maury Maquiné da Silva
> 
> Arthur Lucas dos Santos Bezerra
> 
> __17/11/2021__
