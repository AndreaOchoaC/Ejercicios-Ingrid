"""
EJERCICIO 2 - PYQT5: "Lista de tareas"  (~30 min)
Escribe una tarea, presiona "Agregar" (o Enter) y aparecerá en la lista.
Puedes seleccionar una tarea y borrarla. Un contador muestra cuántas hay.

INSTRUCCIONES: reemplaza cada ____ por el código correcto (hay 17 espacios).
"""
import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QVBoxLayout, QHBoxLayout,
                             QLineEdit, QPushButton, QListWidget, QLabel)


class ListaTareas(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Lista de tareas")
        self.resize(400, 350)

        # --- Widgets ---
        self.entrada = QLineEdit()
        self.entrada.setPlaceholderText("Escribe una tarea...")
        self.btn_agregar = QPushButton("Agregar")
        self.btn_borrar = QPushButton("Borrar seleccionada")
        self.lista = QListWidget()
        self.etiqueta = QLabel("Tareas: 0")

        # --- Layouts ---
        fila = QHBoxLayout()
        fila.addWidget(self.entrada)
        fila.addWidget(self.btn_agregar)

        layout = QVBoxLayout()
        layout.addLayout(fila)
        layout.addWidget(self.lista)
        layout.addWidget(self.btn_borrar)
        layout.addWidget(self.etiqueta)
        self.setLayout(layout)

        # --- Señales y slots ---
        self.btn_agregar.clicked.connect(self.agregar_tarea)
        self.btn_borrar.clicked.connect(self.borrar_tarea)
        self.entrada.returnPressed.connect(self.agregar_tarea)

    # --- Métodos ---
    def agregar_tarea(self):
        texto = self.entrada.text().strip()
        if texto:
            self.lista.addItem(texto)
            self.entrada.clear()
            self.actualizar_contador()

    def borrar_tarea(self):
        fila = self.lista.currentRow()
        if fila >= 0:
            self.lista.takeItem(fila)
            self.actualizar_contador()

    def actualizar_contador(self):
        self.etiqueta.setText(f"Tareas: {self.lista.count()}")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = ListaTareas()
    ventana.show()
    sys.exit(app.exec_())

# --- RETO EXTRA (opcional) ---------------------------------------------------
# a) Agrega un botón "Limpiar todo" que vacíe la lista (pista: lista.clear()).
# b) Muestra un QMessageBox si el usuario intenta agregar una tarea vacía.
