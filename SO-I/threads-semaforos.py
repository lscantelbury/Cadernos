from threading import Thread
from threading import Semaphore
import os
import time
import random

lista = []
podeProduzir = Semaphore(10)
podeConsumir = Semaphore(0)
listaDiponivel = Semaphore(1)

class Produtor(Thread):
    def __init__(self, lista, num):
        Thread.__init__(self)
        self.lista = lista
        self.num = num

    def run(self):
        intAleatorio = None
        while True:
            podeProduzir.acquire() # Produziu 1, subtrai 1 dos que ainda podem produzir
            listaDiponivel.acquire() # Lista já está sendo utilizada, reservá-la para esse processo

            intAleatorio = random.randint(0, 10)
            self.lista.append(intAleatorio)
            print("Thread Produtor " + str(self.num) + " adicionou " + str(intAleatorio) + ':' + str(self.lista))
            time.sleep(0.5)

            listaDiponivel.release() # Terminei o processo, lista está liberada
            podeConsumir.release() # Já tem algo para ser consumido
class Consumidor(Thread):
    def __init__(self, lista, num):
        Thread.__init__(self)
        self.lista = lista
        self.num = num
    
    def run(self):
        intAleatorio = None
        while True:
            if len(lista) == 10:break
            podeConsumir.acquire() # Consumi um dado dos que podiam ser consumidos
            listaDiponivel.acquire() # Estou utilizando a lista, reservá-la pra mim

            intAleatorio = self.lista.pop(0)
            print("Thread Consumidor " + str(self.num) + " retirou " + str(intAleatorio) + ':' + str(self.lista))
            time.sleep(0.5)

            listaDiponivel.release() # Terminei, pode utilizar a lista
            podeProduzir.release() # Mais um item pode ser produzido

class Relogio(Thread):
    def __init__(self, secs):
        Thread.__init__(self)
        self.secs = secs
        self.contador = 0

    def run(self):
        while self.contador != self.secs:
            time.sleep(1)
            self.contador += 1
        os._exit(0)
def main():
    timer = Relogio(20) # O programa vai executar por 20 segundos
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