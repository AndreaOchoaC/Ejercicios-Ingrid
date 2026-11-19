"""
EJERCICIO 4 - KIVY + KV: "Calculadora de propina"  (~25 min)
Este proyecto tiene DOS archivos que trabajan juntos:
  - propina.py  -> la lógica (este archivo)
  - propina.kv  -> la interfaz (lenguaje KV)
Kivy carga propina.kv automáticamente porque la clase se llama PropinaApp
(nombre de la clase sin "App", en minúsculas + ".kv").

INSTRUCCIONES: completa los espacios ____ en AMBOS archivos (hay 15 en total,
numerados del 1 al 15).
"""
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import StringProperty


class PropinaLayout(BoxLayout):
    resultado = StringProperty("Total: ---")

    def calcular(self):
        try:
            monto = float(self.ids.monto.text)
            porcentaje = self.ids.propina.value
            propina = monto * porcentaje / 100
            total = monto + propina
            self.resultado = f"Propina: ${propina:.2f}  |  Total: ${total:.2f}"
        except ValueError:
            self.resultado = "Ingresa un monto válido"


class SolPropinaApp(App):
    def build(self):
        self.title = "Calculadora de propina"
        return PropinaLayout()


if __name__ == "__main__":
    SolPropinaApp().run()

# --- RETO EXTRA (opcional) ---------------------------------------------------
# a) Agrega un método limpiar() y un botón "Limpiar" en el .kv que lo llame
#    (pista: self.ids.monto.text = "" y self.resultado = "Total: ---").
# b) Agrega un segundo Slider para dividir la cuenta entre varias personas.
