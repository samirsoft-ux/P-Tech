# -*- coding: utf-8 -*-
"""juego.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Bm8tDRbrOtYbRKwZU6CXSK-DBRl1n8VI
"""

!pip install ipywidgets

import ipywidgets as widgets
from IPython.display import display, clear_output
import random

class AdivinaElNumeroWidget:
    def __init__(self):
        self.numero_secreto = random.randint(1, 100)
        self.intentos = 0
        self.max_intentos = 5

        self.intento_text = widgets.Text(
            description='Intento:',
            disabled=False
        )
        self.intento_button = widgets.Button(description="Adivinar")
        self.intento_button.on_click(self.verificar_numero)
        self.output = widgets.Output()

        display(self.intento_text, self.intento_button, self.output)

    def verificar_numero(self, b):
        with self.output:
            clear_output(wait=True)
            try:
                intento = int(self.intento_text.value)
                self.intentos += 1
                if intento < self.numero_secreto:
                    print("Demasiado bajo.")
                elif intento > self.numero_secreto:
                    print("Demasiado alto.")
                else:
                    print("¡Correcto! ¡Has adivinado el número!")
                    self.intento_button.disabled = True
                    return

                if self.intentos >= self.max_intentos:
                    print(f"Fin del juego. El número era: {self.numero_secreto}")
                    self.intento_button.disabled = True
            except ValueError:
                print("Por favor, introduce un número válido.")

juego = AdivinaElNumeroWidget()