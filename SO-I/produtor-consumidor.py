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