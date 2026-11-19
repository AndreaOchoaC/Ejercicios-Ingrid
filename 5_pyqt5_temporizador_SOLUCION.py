"""
EJERCICIO 5 - PYQT5: "Temporizador de cuenta regresiva"
Elige cuántos segundos quieres, presiona "Iniciar" y la cuenta regresiva
comienza: se actualizan la pantalla y la barra de progreso. Puedes pausar o
reiniciar. Al llegar a cero aparece un mensaje.

INSTRUCCIONES: reemplaza cada ____ por el código correcto (hay 22 espacios,
numerados del 1 al 22).
"""
import sys
from PyQt5.QtCore import Qt, QTimer
from PyQt5.QtWidgets import (QApplication, QWidget, QVBoxLayout, QHBoxLayout,
                             QLabel, QSpinBox, QPushButton, QProgressBar,
                             QMessageBox)


class Temporizador(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Temporizador")
        self.resize(360, 280)

        self.segundos_totales = 0
        self.segundos_restantes = 0

        # --- Widgets ---
        self.etiqueta = QLabel("Segundos a contar:")
        self.spin = QSpinBox()
        self.spin.setRange(1, 3600)
        self.spin.setValue(10)

        self.pantalla = QLabel("00:10")
        self.pantalla.setAlignment(Qt.AlignCenter)
        self.pantalla.setStyleSheet("font-size: 48px; font-weight: bold;")

        self.barra = QProgressBar()
        self.barra.setValue(0)

        self.btn_iniciar = QPushButton("Iniciar")
        self.btn_pausa = QPushButton("Pausar")
        self.btn_reiniciar = QPushButton("Reiniciar")

        # --- Temporizador interno ---
        self.timer = QTimer()
        self.timer.setInterval(1000)

        # --- Layouts ---
        fila_spin = QHBoxLayout()
        fila_spin.addWidget(self.etiqueta)
        fila_spin.addWidget(self.spin)

        fila_botones = QHBoxLayout()
        fila_botones.addWidget(self.btn_iniciar)
        fila_botones.addWidget(self.btn_pausa)
        fila_botones.addWidget(self.btn_reiniciar)

        layout = QVBoxLayout()
        layout.addLayout(fila_spin)
        layout.addWidget(self.pantalla)
        layout.addWidget(self.barra)
        layout.addLayout(fila_botones)
        self.setLayout(layout)

        # --- Señales y slots ---
        self.timer.timeout.connect(self.tick)
        self.btn_iniciar.clicked.connect(self.iniciar)
        self.btn_pausa.clicked.connect(self.pausar)
        self.btn_reiniciar.clicked.connect(self.reiniciar)
        self.spin.valueChanged.connect(self.mostrar_tiempo)

    # --- Métodos ---
    def iniciar(self):
        if not self.timer.isActive():
            if self.segundos_restantes == 0:
                self.segundos_totales = self.spin.value()
                self.segundos_restantes = self.segundos_totales
                self.barra.setMaximum(self.segundos_totales)
            self.timer.start()
            self.spin.setEnabled(False)

    def pausar(self):
        self.timer.stop()

    def reiniciar(self):
        self.timer.stop()
        self.segundos_restantes = 0
        self.spin.setEnabled(True)
        self.barra.setValue(0)
        self.mostrar_tiempo(self.spin.value())

    def tick(self):
        """Se ejecuta cada segundo."""
        self.segundos_restantes -= 1
        self.mostrar_tiempo(self.segundos_restantes)
        self.barra.setValue(self.segundos_totales - self.segundos_restantes)

        if self.segundos_restantes <= 0:
            self.timer.stop()
            self.spin.setEnabled(True)
            QMessageBox.information(self, "Tiempo", "¡Se acabó el tiempo!")

    def mostrar_tiempo(self, segundos):
        minutos, seg = divmod(segundos, 60)
        self.pantalla.setText(f"{minutos:02d}:{seg:02d}")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = Temporizador()
    ventana.show()
    sys.exit(app.exec_())

# --- RETO EXTRA (opcional) ---------------------------------------------------
# a) Cambia el color de la pantalla a rojo cuando queden 5 segundos o menos
#    (pista: setStyleSheet con "color: red;").
# b) Agrega un QCheckBox "Sonar alarma" y haz que suene QApplication.beep()
#    al terminar solo si está marcado.
