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