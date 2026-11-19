"""
EJERCICIO 2 - PYQT5: "Lista de tareas"
Escribe una tarea, presiona "Agregar" (o Enter) y aparecerá en la lista.
Puedes seleccionar una tarea y borrarla. Un contador muestra cuántas hay.

INSTRUCCIONES: reemplaza cada ____ por el código correcto (hay 17 espacios).
"""
import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QVBoxLayout, QHBoxLayout,
                             QLineEdit, QPushButton, QListWidget, QLabel)


class ListaTareas(QWidget):
    def __init__(self):
        super().____()                                      # 1. Constructor de la clase padre
        self.setWindowTitle("Lista de tareas")
        self.resize(400, 350)

        # --- Widgets ---
        self.entrada = ____()                              # 2. Campo de texto de una línea
        self.entrada.____("Escribe una tarea...") # 3. Texto de ayuda dentro del campo
        self.btn_agregar = ____("Agregar")               # 4. Botón
        self.btn_borrar = QPushButton("Borrar seleccionada")
        self.lista = ____()                              # 5. Lista de elementos
        self.etiqueta = QLabel("Tareas: 0")

        # --- Layouts ---
        fila = QHBoxLayout()
        fila.addWidget(self.entrada)
        fila.____(self.btn_agregar)                        # 6. Agrega el botón a la fila

        layout = QVBoxLayout()
        layout.____(fila)                                  # 7. Agrega un layout dentro de otro
        layout.addWidget(self.lista)
        layout.addWidget(self.btn_borrar)
        layout.addWidget(self.etiqueta)
        self.____(layout)                                  # 8. Asigna el layout a la ventana

        # --- Señales y slots ---
        self.btn_agregar.clicked.____(self.agregar_tarea)    # 9. Conecta la señal con el método
        self.btn_borrar.clicked.connect(self.borrar_tarea)
        self.entrada.____.connect(self.agregar_tarea)  # 10. Señal al presionar Enter

    # --- Métodos ---
    def agregar_tarea(self):
        texto = self.entrada.____().strip()                     # 11. Lee el texto escrito
        if texto:
            self.lista.____(texto)                           # 12. Agrega un elemento a la lista
            self.entrada.____()                                # 13. Limpia el campo de texto
            self.actualizar_contador()

    def borrar_tarea(self):
        fila = self.lista.____()                          # 14. Índice del elemento seleccionado
        if fila >= 0:
            self.lista.____(fila)                           # 15. Quita el elemento de la lista
            self.actualizar_contador()

    def actualizar_contador(self):
        self.etiqueta.setText(f"Tareas: {self.lista.____()}")  # 16. Cantidad de elementos


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = ListaTareas()
    ventana.____()                                              # 17. Muestra la ventana
    sys.exit(app.exec_())

# --- RETO EXTRA (opcional) ---------------------------------------------------
# a) Agrega un botón "Limpiar todo" que vacíe la lista (pista: lista.clear()).
# b) Muestra un QMessageBox si el usuario intenta agregar una tarea vacía.
