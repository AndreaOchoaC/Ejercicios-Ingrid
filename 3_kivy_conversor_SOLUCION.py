"""
EJERCICIO 3 - KIVY: "Conversor Celsius a Fahrenheit"  (~20 min)
El usuario escribe grados Celsius, presiona "Convertir" y se muestra el resultado.

INSTRUCCIONES: reemplaza cada ____ por el código correcto (hay 10 espacios).
"""
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.core.window import Window
from kivy.utils import get_color_from_hex

Window.clearcolor = get_color_from_hex("#60609c")

class Conversor(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = "vertical"
        self.padding = 20
        self.spacing = 10

        titulo = Label(text="Celsius a Fahrenheit", font_size=28, bold=True,
               color=get_color_from_hex("#cdd6f4"))

        self.add_widget(titulo)

        self.entrada = TextInput(
            hint_text="Grados Celsius",
            multiline=False,
            input_filter="float",
            font_size=22,
            padding=10,
            background_color=get_color_from_hex("#cdd6f4"),
            foreground_color=(1, 1, 1, 1),
            hint_text_color=(0.6, 0.6, 0.7, 1),
            cursor_color=(1, 1, 1, 1),
        )
        self.add_widget(self.entrada)

        boton = Button(text="Convertir")
        boton.bind(on_press=self.convertir)
        self.add_widget(boton)

        self.resultado = Label(text="Resultado: ---", font_size=22)
        self.add_widget(self.resultado)

    def convertir(self, instancia):
        try:
            celsius = float(self.entrada.text)
            fahrenheit = celsius * 9 / 5 + 32
            self.resultado.text = f"Resultado: {fahrenheit:.1f} °F"
        except ValueError:
            self.resultado.text = "Ingresa un número válido"


class ConversorApp(App):
    def build(self):
        self.title = "Conversor de temperatura"
        return Conversor()


if __name__ == "__main__":
    ConversorApp().run()

# --- RETO EXTRA (opcional) ---------------------------------------------------
# a) Agrega un segundo botón que convierta de Fahrenheit a Celsius.
# b) Cambia el color del resultado (color=(1, 0, 0, 1)) si la temperatura pasa de 30 °C.
