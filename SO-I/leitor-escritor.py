from os import listxattr
from random import randint
from threading import Thread, Semaphore
import time
from Relogio import Relogio

podeLer = Semaphore(1)
podeEscrever = Semaphore(0)
listaDisponivel = Semaphore(1)

class Leitor(Thread):
    def __init__(self, lista):
        Thread.__init__(self)
        self.lista = lista
        
    def run(self):
        while True:
            podeLer.acquire() # Menos um a ser lido
            listaDisponivel.acquire() # Lista está indisponível no momento

            soma = 0
            for i in self.lista: soma += i
            print(soma)
            time.sleep(1)

            listaDisponivel.release() # Já pode utilizar a lista
            podeEscrever.release()

class Escritor(Thread):
    def __init__(self, lista):
        Thread.__init__(self)
        self.lista = lista
    
    def run(self):
        while True:

            podeEscrever.acquire() # Menos um a ser escrito
            listaDisponivel.acquire() # Lista indisponível no momento

            self.lista.pop(0)
            self.lista.append(randint(0,10))
            time.sleep(1)
            print(self.lista)

            listaDisponivel.release() # Já pode utilizar a lista
            podeLer.release() # Já pode ler mais uma vez

def main():
    time = Relogio(10)
    time.start()
    
    lista = [1,2,3]
    print(lista)
    
    leitor = Leitor(lista)
    leitor.start()
    
    escritor = Escritor(lista)
    escritor.start()

main()