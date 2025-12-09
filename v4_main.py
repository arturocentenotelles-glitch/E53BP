from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QVBoxLayout, QGroupBox, QRadioButton, QButtonGroup, QScrollArea
from PyQt5.QtCore import Qt

class Resultados(QWidget):
    def _init_(self, score):
        super()._init_()
        self.setWindowTitle("Resultados")
        self.setFixedSize(400, 320)

        layout = QVBoxLayout()
        titulo = QLabel("Resultados del Test")
        titulo.setAlignment(Qt.AlignCenter)
        titulo.setStyleSheet("font-size:18px; font-weight:bold;")
        layout.addWidget(titulo)

        layout.addWidget(QLabel(f"Puntuación final: {score}"))

        if score <= 7:
            nivel = "Bajo nivel de adicción"
            consejo = "Mantén hábitos equilibrados."
        elif score <= 14:
            nivel = "Nivel medio de adicción"
            consejo = "Pon límites y evita revisar el celular seguido."
        else:
            nivel = "Nivel alto de adicción"
            consejo = "Reduce el uso del celular y busca actividades alternativas."

        lbl_nivel = QLabel(nivel)
        lbl_nivel.setStyleSheet("font-weight:bold; color:blue;")
        layout.addWidget(lbl_nivel)

        lbl_consejo = QLabel(consejo)
        lbl_consejo.setWordWrap(True)
        layout.addWidget(lbl_consejo)

        self.setLayout(layout)

class Test(QWidget):
    def _init_(self):
        super()._init_()
        self.setWindowTitle("Test")
        self.setFixedSize(600, 550)

        self.preguntas = [
            "1. ¿Cuánto tiempo usas redes sociales al día?",
            "2. ¿Te distraes en actividades importantes?",
            "3. ¿Te sientes ansioso sin el celular?",
            "4. ¿Revisas redes al despertar?",
            "5. ¿Te desvelas por redes?",
            "6. ¿Afecta tus tareas?",
            "7. ¿Ignoras personas por usar redes?",
            "8. ¿Publicas buscando atención?",
            "9. ¿Te urge responder mensajes?",
            "10. ¿Te molesta no recibir reacciones?"
        ]

        opciones = ["Nunca", "A veces", "Frecuentemente"]
        puntaje_map = {"Nunca": 0, "A veces": 1, "Frecuentemente": 2}

        caja = QVBoxLayout()
        scroll = QScrollArea()
        contenido = QWidget()
        layContenido = QVBoxLayout()

        self.respuestas = []
        self.puntaje_map = puntaje_map

        for p in self.preguntas:
            box = QGroupBox(p)
            boxLay = QVBoxLayout()
            grupo = QButtonGroup()

            for op in opciones:
                rb = QRadioButton(op)
                grupo.addButton(rb)
                boxLay.addWidget(rb)

            box.setLayout(boxLay)
            layContenido.addWidget(box)
            self.respuestas.append(grupo)

        contenido.setLayout(layContenido)
        scroll.setWidget(contenido)
        scroll.setWidgetResizable(True)
        caja.addWidget(scroll)

        btn = QPushButton("Ver Resultados")
        btn.clicked.connect(self.calcular)
        caja.addWidget(btn)

        self.setLayout(caja)

    def calcular(self):
        total = 0
        for grupo in self.respuestas:
            seleccionado = grupo.checkedButton()
            if seleccionado:
                total += self.puntaje_map[seleccionado.text()]
        self.res = Resultados(total)
        self.res.show()

app = QApplication([])
win = Test()
win.show()
app.exec_()
