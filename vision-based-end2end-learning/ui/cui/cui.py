"""
    * Grabar dataset (r, record)
    * Cargar dataset (l, load)
    * Pausar piloto (p, pause)
    * Relanzar piloto (u, unpause)
    * Cambiar cerebro (c, change)
    * Evaluar comportamiento (e, evaluate)
"""
from pynput import keyboard

class CUI:

    def __init__(self):
        self.listener = keyboard.Listener(
            on_press=self.on_press,
            on_release=self.on_release
        )

    def on_press(self, key):
        try:
            print(f'Pressed key {key.char}')
        except AttributeError:
            print(f'Not alphanumeric {key}')

    def on_release(self, key):
        print(f'Released {key}')

    def start(self):
        self.listener.start()


if __name__ == "__main__":

    c = CUI()
    c.start()

    import time
    time.sleep(5)