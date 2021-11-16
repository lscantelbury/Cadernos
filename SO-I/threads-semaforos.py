from threading import Thread
from threading import Semaphore
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
        if len(lista) == 10: return
        while True:
            podeProduzir.acquire() # Produziu 1, subtrai 1 dos que ainda podem produzir
            listaDiponivel.acquire() # Lista já está sendo utilizada, reservá-la para esse processo

            intAleatorio = random.randint(0, 10)
            self.lista.append(intAleatorio)
            print("Thread Produtor " + str(self.num) + " adicionou " + str(intAleatorio) + ':' + str(self.lista))

            podeConsumir.release() # Já tem algo para ser consumido
            listaDiponivel.release() # Terminei o processo, lista está liberada
class Consumidor(Thread):
    def __init__(self, lista, num):
        Thread.__init__(self)
        self.lista = lista
        self.num = num
    
    def run(self):
        intAleatorio = None
        if len(lista) == 0: return
        while True:
            podeConsumir.acquire() # Consumi um dado dos que podiam ser consumidos
            listaDiponivel.acquire() # Estou utilizando a lista, reservá-la pra mim

            intAleatorio = self.lista.pop(0)
            print("Thread Consumidor " + str(self.num) + " retirou " + str(intAleatorio) + ':' + str(self.lista))

            podeProduzir.release() # Mais um item pode ser produzido
            listaDiponivel.release() # Terminei, pode utilizar a lista

produtor1 = Produtor(lista, 1)
produtor1.start()
consumidor1 = Consumidor(lista, 1)
consumidor1.start()
produtor2 = Produtor(lista, 2)
produtor2.start()
consumidor2 = Consumidor(lista, 2)
consumidor2.start()
