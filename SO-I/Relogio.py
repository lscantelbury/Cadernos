from threading import Thread
import time
import os
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