"""
EJERCICIO 3 - KIVY: "Conversor Celsius a Fahrenheit"
El usuario escribe grados Celsius, presiona "Convertir" y se muestra el resultado.

INSTRUCCIONES: reemplaza cada ____ por el código correcto 
"""
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.core.window import Window

# ¿Cómo cambiar el color de fondo de la ventana? (usa Window.clearcolor) y un hexadecimal (usa get_color_from_hex)

class Conversor(____):                                     # 1. Layout del que hereda la clase
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = "____"                           # 2. Los widgets se apilan en columna
        self.padding = 20
        self.spacing = 10

        
        # ¿Cómo cambiar el estilo del texto?
        # Pista: font_color=(1, 1, 1, 1) y hint_text_color=(0.6, 0.6, 0.7, 1)
        # Pista: background_color
        # Pista: font_size

        self.add_widget(Label(text="Celsius a Fahrenheit", font_size=24))

        self.entrada = TextInput(
            hint_text="Grados Celsius",
            multiline=____,                                    # 3. Una sola línea (True / False)
            input_filter="float",
            font_size=22,
            # ¿qué propiedades de estilo se pueden agregar aquí?
        )
        self.____(self.entrada)                           # 4. Agrega el campo al layout

        boton = Button(text="Convertir")
        boton.bind(____=self.convertir)                     # 5. Evento al presionar el botón
        self.add_widget(boton)

        self.resultado = ____(text="Resultado: ---", font_size=22)   # 6. Widget de texto
        self.add_widget(self.resultado)

    def convertir(self, instancia):
        try:
            celsius = ____(self.entrada.text)                  # 7. Convierte el texto a número
            fahrenheit = celsius * 9 / 5 + 32
            self.resultado.____ = f"Resultado: {fahrenheit:.1f} °F"   # 8. Propiedad del texto
        except ____:                                      # 9. Error si el campo está vacío
            self.resultado.text = "Ingresa un número válido"


class ConversorApp(App):
    def build(self):
        self.title = "Conversor de temperatura"
        return ____()                                      # 10. Devuelve el widget raíz


if __name__ == "__main__":
    ConversorApp().run()

# --- RETO EXTRA (opcional) ---------------------------------------------------
# a) Agrega un segundo botón que convierta de Fahrenheit a Celsius.
# b) Cambia el color del resultado (color=(1, 0, 0, 1)) si la temperatura pasa de 30 °C.
