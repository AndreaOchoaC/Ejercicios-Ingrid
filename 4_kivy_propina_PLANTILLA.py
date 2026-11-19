"""
EJERCICIO 4 - KIVY + KV: "Calculadora de propina"
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
from kivy.properties import ____              # 1. Propiedad de tipo texto, observable desde KV


class PropinaLayout(____):                         # 2. Clase base (debe coincidir con <PropinaLayout> del .kv)
    resultado = ____("Total: ---")            # 3. Propiedad que el .kv muestra en una etiqueta

    def calcular(self):
        try:
            monto = float(self.ids.____.text)          # 4. id del TextInput definido en el .kv
            porcentaje = self.ids.propina.____         # 5. Propiedad del Slider con su valor actual
            propina = monto * porcentaje / 100
            total = monto + propina
            self.resultado = f"Propina: ${propina:.2f}  |  Total: ${total:.2f}"
        except ____:                              # 6. Error si el campo está vacío
            self.resultado = "Ingresa un monto válido"


class PropinaApp(____):                                  # 7. Clase base de toda aplicación Kivy
    def build(self):
        self.title = "Calculadora de propina"
        return ____()                          # 8. Devuelve el widget raíz


if __name__ == "__main__":
    PropinaApp().run()

# --- RETO EXTRA (opcional) ---------------------------------------------------
# a) Agrega un método limpiar() y un botón "Limpiar" en el .kv que lo llame
#    (pista: self.ids.monto.text = "" y self.resultado = "Total: ---").
# b) Agrega un segundo Slider para dividir la cuenta entre varias personas.
