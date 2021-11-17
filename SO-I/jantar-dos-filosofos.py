from threading import Thread, Semaphore
from Relogio import Relogio
import time
import random

listaFilosofos = []

class Filosofo(Thread):
    def __init__(self, comendo, nome):
        Thread.__init__(self)
        self.comendo = comendo
        self.pensando = not comendo
        self.nome = nome

    def run(self):
        while True:

            self.comendo = random.choice([False, True])
            # A expressão abaixo utiliza de divisão modular para fazer uma lista circular
            # ex: lista = [1,2,3]; print(lista[0]) => 1; é a mesma coisa que print(lista[4 % len(lista)]) => 1
            # dessa forma simulo uma mesa em que cada filósofo está um do lado do outro em círculo.
            if (listaFilosofos[(listaFilosofos.index(self) % len(listaFilosofos))+1].comendo == False 
                and listaFilosofos[(listaFilosofos.index(self) % len(listaFilosofos))-1].comendo == False):
                self.comendo = True
                print(self.nome + " está comendo")
            else:
                self.comendo = False
                print(self.nome + " está pensando")

            time.sleep(random.random())
# Criando os filósofos, o caso inicial sempre tem dois que estão pensando 
# nas laterais de um que está comendo, no decorrer da execução, diferentes
# combinações de tentativas de comer acontecem. O filósofo só come se seus 
# vizinhos estiverem pensando. Eventualmente, ambos vizinhos pensam, e o 
# filósofos consegue comer
filosofo1 = Filosofo(False, "Sócrates"); listaFilosofos.append(filosofo1)
filosofo2 = Filosofo(False, "Aristóteles");listaFilosofos.append(filosofo2)
filosofo3 = Filosofo(False, "Platão");listaFilosofos.append(filosofo3)
filosofo4 = Filosofo(False, "Tales"); listaFilosofos.append(filosofo4)
filosofo5 = Filosofo(False, "Heráclito"); listaFilosofos.append(filosofo5)
filosofo6 = Filosofo(False, "Epiteto"); listaFilosofos.append(filosofo6)
filosofo7 = Filosofo(False, "Diógenes"); listaFilosofos.append(filosofo7)

quantosPodemComer = None

if len(listaFilosofos) % 2 == 0:
    # Se o número de filósofos for par, 50% pode comer simultâneamente
    quantosPodemComer = len(listaFilosofos)/2
else:
    # Se ímpar, apenas 50% do número de filósofos - 1
    quantosPodemComer = len(listaFilosofos) - 1/2
comendo = Semaphore(len(listaFilosofos))

def main():

    # O programa será executado por 5 segundos
    time = Relogio(2)
    time.start()

    filosofo1.start()
    filosofo2.start()
    filosofo3.start()
    filosofo4.start()
    filosofo5.start()
    filosofo6.start()
    filosofo7.start()

main()