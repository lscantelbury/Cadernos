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
main()