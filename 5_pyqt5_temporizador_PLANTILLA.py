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
        super().____()                                     # 1. Constructor de la clase padre
        self.setWindowTitle("Temporizador")
        self.resize(360, 280)

        self.segundos_totales = 0
        self.segundos_restantes = 0

        # --- Widgets ---
        self.etiqueta = QLabel("Segundos a contar:")
        self.spin = ____()                                 # 2. Selector numérico con flechas
        self.spin.____(1, 3600)                            # 3. Valor mínimo y máximo
        self.spin.setValue(10)

        self.pantalla = QLabel("00:10")
        self.pantalla.setAlignment(Qt.____)             # 4. Centra el texto
        self.pantalla.setStyleSheet("font-size: 48px; font-weight: bold;")

        self.barra = ____()                            # 5. Barra de progreso
        self.barra.setValue(0)

        self.btn_iniciar = ____("Iniciar")              # 6. Botón
        self.btn_pausa = QPushButton("Pausar")
        self.btn_reiniciar = QPushButton("Reiniciar")

        # --- Temporizador interno ---
        self.timer = ____()                                  # 7. Objeto que emite una señal cada cierto tiempo
        self.timer.____(1000)                           # 8. Intervalo en milisegundos (1 segundo)

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
        self.timer.timeout.____(self.tick)                  # 9. Conecta la señal del timer con tick()
        self.btn_iniciar.____.connect(self.iniciar)         # 10. Señal de clic del botón
        self.btn_pausa.clicked.connect(self.pausar)
        self.btn_reiniciar.clicked.connect(self.reiniciar)
        self.spin.____.connect(self.mostrar_tiempo)    # 11. Señal cuando cambia el número

    # --- Métodos ---
    def iniciar(self):
        if not self.timer.____():                          # 12. ¿El timer está corriendo?
            if self.segundos_restantes == 0:
                self.segundos_totales = self.spin.____()      # 13. Lee el valor del selector
                self.segundos_restantes = self.segundos_totales
                self.barra.____(self.segundos_totales)   # 14. Valor máximo de la barra
            self.timer.____()                                 # 15. Arranca el timer
            self.spin.____(False)                        # 16. Desactiva el selector mientras corre

    def pausar(self):
        self.timer.____()                                      # 17. Detiene el timer

    def reiniciar(self):
        self.timer.stop()
        self.segundos_restantes = 0
        self.spin.setEnabled(True)
        self.barra.setValue(0)
        self.mostrar_tiempo(self.spin.value())

    def tick(self):
        """Se ejecuta cada segundo."""
        self.segundos_restantes ____ 1                           # 18. Resta un segundo
        self.mostrar_tiempo(self.segundos_restantes)
        self.barra.____(self.segundos_totales - self.segundos_restantes)   # 19. Avance de la barra

        if self.segundos_restantes <= 0:
            self.timer.stop()
            self.spin.setEnabled(True)
            QMessageBox.____(self, "Tiempo", "¡Se acabó el tiempo!")    # 20. Cuadro de mensaje informativo

    def mostrar_tiempo(self, segundos):
        minutos, seg = ____(segundos, 60)                    # 21. Devuelve cociente y residuo
        self.pantalla.setText(f"{minutos:02d}:{seg:02d}")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = Temporizador()
    ventana.show()
    sys.exit(app.____())                                      # 22. Inicia el bucle de eventos

# --- RETO EXTRA (opcional) ---------------------------------------------------
# a) Cambia el color de la pantalla a rojo cuando queden 5 segundos o menos
#    (pista: setStyleSheet con "color: red;").
# b) Agrega un QCheckBox "Sonar alarma" y haz que suene QApplication.beep()
#    al terminar solo si está marcado.
