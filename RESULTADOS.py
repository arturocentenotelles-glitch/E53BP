from PyQt5.QtWidgets import ( 
    QApplication, QMainWindow, QLabel, QPushButton,
    QGridLayout, QWidget, QRadioButton, QGroupBox, 
    QVBoxLayout, QMessageBox, QButtonGroup
)

import sys
from pregunta import Pregunta


class Principal(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Encuesta")
        self.crearCuestionario()
        self.index = 0
        self.maximo = len(self.cuestionario)

        self.lb_num = QLabel(str(self.cuestionario[self.index].num_pregunta))
        self.lb_pregunta = QLabel(self.cuestionario[self.index].texto)

        self.btn_siguiente = QPushButton("Siguiente")
        self.btn_siguiente.clicked.connect(self.siguiente)

        # RadioButtons
        self.opc_nunca = QRadioButton("Nunca")
        self.opc_casi_nunca = QRadioButton("Casi nunca")
        self.opc_frecuente = QRadioButton("Frecuentemente")
        self.opc_siempre = QRadioButton("Siempre")

        # Agruparlos para validar SIN or / return
        self.grupo = QButtonGroup()
        self.grupo.addButton(self.opc_nunca)
        self.grupo.addButton(self.opc_casi_nunca)
        self.grupo.addButton(self.opc_frecuente)
        self.grupo.addButton(self.opc_siempre)

        opciones_box = QGroupBox("Opciones de respuesta")
        opciones_layout = QVBoxLayout()
        opciones_layout.addWidget(self.opc_nunca)
        opciones_layout.addWidget(self.opc_casi_nunca)
        opciones_layout.addWidget(self.opc_frecuente)
        opciones_layout.addWidget(self.opc_siempre)
        opciones_box.setLayout(opciones_layout)

        layout = QGridLayout()
        layout.addWidget(self.lb_num, 0, 0)
        layout.addWidget(self.lb_pregunta, 1, 0)
        layout.addWidget(opciones_box, 2, 0)
        layout.addWidget(self.btn_siguiente, 3, 0)

        contenedor = QWidget()
        contenedor.setLayout(layout)
        self.setCentralWidget(contenedor)

    def siguiente(self):

        # VALIDACIÓN sin OR, sin TRUE/FALSE, sin RETURN
        seleccionado = self.grupo.checkedButton()

        # Si NO eligió nada
        if seleccionado == None:
            QMessageBox.warning(self, "Error", "Seleccione una opción antes de continuar")
        else:
            # Pasar a la siguiente pregunta
            self.index = self.index + 1

            # Si ya se acabó el cuestionario
            if self.index >= self.maximo:
                QMessageBox.information(self, "Fin", " Haz finalizado el cuestionario ")
                self.btn_siguiente.setEnabled(False)
            else:
                # Mostrar la siguiente pregunta
                self.lb_num.setText(str(self.cuestionario[self.index].num_pregunta))
                self.lb_pregunta.setText(self.cuestionario[self.index].texto)


    def crearCuestionario(self):
        pregunta1 = Pregunta(1, "¿Tienes algún familiar cercano con problemas de alcoholismo?", 0)
        pregunta2 = Pregunta(2, "¿Pasas más de 6 horas revisando redes sociales?", 0)
        pregunta3 = Pregunta(3, "¿Tus amigos te han incitado a probar alguna sustancia?", 0)

        self.cuestionario = [pregunta1, pregunta2, pregunta3]


app = QApplication(sys.argv)
window = Principal()
window.show()
app.exec_()
