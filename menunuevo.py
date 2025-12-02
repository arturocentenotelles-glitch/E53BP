import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QGridLayout, QLabel, QTabWidget,QVBoxLayout, QLineEdit, QPushButton, QMessageBox, QRadioButton, QButtonGroup
from PyQt5.QtCore import *
from registro import registro
from test import test 
# Clase Pregunta usada para el test
class Pregunta:
    def __init__(self, num_pregunta, texto, puntaje=0):
        self.num_pregunta = num_pregunta
        self.texto = texto
        self.puntaje = puntaje

# Ventana Principal
class Principal(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Menu")
        self.setGeometry(100, 100, 600, 400)

        # Tabs
        self.tabs = QTabWidget()
        self.setCentralWidget(self.tabs)

        # Crear pestañas
        self.tab_registro = QWidget()
        self.tab_test = QWidget()
        self.tab_res = QWidget()

        self.tabs.addTab(self.tab_registro, "Registro")
        self.tabs.addTab(self.tab_test, "Test")
        self.tabs.addTab(self.tab_res, "Resultados")

        # Crear contenido
        self.crear_pestana_registro()
        self.crear_pestana_test()
        self.crear_pestana_resultados()


    # PESTAÑA REGISTRO
    def crear_pestana_registro(self):
        layout = QVBoxLayout()

        layout.addWidget(QLabel("Crear Cuenta"))

        self.input_correo = QLineEdit()
        self.input_contra = QLineEdit()
        self.input_contra.setEchoMode(QLineEdit.Password)

        layout.addWidget(QLabel("Correo:"))
        layout.addWidget(self.input_correo)
        layout.addWidget(QLabel("Contraseña:"))
        layout.addWidget(self.input_contra)

        btn_registrar = QPushButton("Registrar")
        btn_registrar.clicked.connect(self.registrar_usuario)
        layout.addWidget(btn_registrar)

        self.tab_registro.setLayout(layout)

    def registrar_usuario(self):
        correo = self.input_correo.text()
        contra = self.input_contra.text()

        if correo == "" or contra == "":
            QMessageBox.warning(self, "Error", "Completa todos los campos")
            return

        QMessageBox.information(self, "Éxito", "Cuenta creada correctamente")

    # PESTAÑA TEST
    def crear_pestana_test(self):
        layout = QGridLayout()

        # Crear preguntas
        self.crearCuestionario()
        self.index = 0
        self.maximo = len(self.cuestionario)
        self.puntaje_total = 0

        # Widgets
        self.lb_num = QLabel("")
        self.lb_pregunta = QLabel("")
        self.lb_pregunta.setWordWrap(True)

        self.opcion_siempre = QRadioButton("Siempre")
        self.opcion_frecuente = QRadioButton("Frecuentemente")
        self.opcion_aveces = QRadioButton("A veces")
        self.opcion_nunca = QRadioButton("Nunca")

        self.grupo_opciones = QButtonGroup()
        self.grupo_opciones.addButton(self.opcion_siempre)
        self.grupo_opciones.addButton(self.opcion_frecuente)
        self.grupo_opciones.addButton(self.opcion_aveces)
        self.grupo_opciones.addButton(self.opcion_nunca)

        self.btn_siguiente = QPushButton("Siguiente")
        self.btn_siguiente.clicked.connect(self.siguiente)

        # Layout
        layout.addWidget(self.lb_num, 0, 0)
        layout.addWidget(self.lb_pregunta, 1, 0)

        layout.addWidget(self.opcion_siempre, 2, 0)
        layout.addWidget(self.opcion_frecuente, 3, 0)
        layout.addWidget(self.opcion_aveces, 4, 0)
        layout.addWidget(self.opcion_nunca, 5, 0)

        layout.addWidget(self.btn_siguiente, 6, 0)

        self.tab_test.setLayout(layout)

        self.mostrarPregunta()

    def crearCuestionario(self):
        self.cuestionario = [
        Pregunta(1, "¿Sientes la necesidad constante de revisar tus redes sociales?"),
        Pregunta(2, "¿Has dejado tareas o actividades importantes por usar redes sociales?"),
        Pregunta(3, "¿Te sientes ansioso o incómodo cuando no puedes usar redes sociales?"),
        Pregunta(4, "¿Usas redes sociales incluso cuando deberías estar haciendo otra cosa importante?"),
        Pregunta(5, "¿Te cuesta dejar de usar redes sociales cuando decides detenerte?"),
        Pregunta(6, "¿Has ocultado o mentido sobre cuánto tiempo pasas en redes sociales?"),
        Pregunta(7, "¿Prefieres estar en redes sociales antes que pasar tiempo con amigos o familia?"),
        Pregunta(8, "¿Sientes que las redes sociales son lo que más te hace sentir bien en tu día?"),
        Pregunta(9, "¿Has gastado dinero en funciones, suscripciones o mejoras dentro de redes sociales?"),
        Pregunta(10, "¿Te molesta cuando alguien te pide dejar de usar el celular o las redes sociales?"),
        Pregunta(11, "¿Has perdido horas de sueño por usar redes sociales?"),
        Pregunta(12, "¿Ha disminuido tu rendimiento escolar o laboral por usar redes sociales?"),
        Pregunta(13, "¿Te distraes pensando en redes sociales cuando no las estás usando?"),
        Pregunta(14, "¿Has intentado reducir el uso de redes sociales sin lograrlo?"),
        Pregunta(15, "¿Sientes que las redes sociales son más importantes que tus relaciones personales?")
    ]


    def mostrarPregunta(self):
        # Limpiar selección
        self.grupo_opciones.setExclusive(False)
        for btn in [self.opcion_siempre, self.opcion_frecuente, self.opcion_aveces, self.opcion_nunca]:
            btn.setChecked(False)
        self.grupo_opciones.setExclusive(True)

        # Mostrar pregunta
        pregunta = self.cuestionario[self.index]
        self.lb_num.setText(f"Pregunta {pregunta.num_pregunta}")
        self.lb_pregunta.setText(pregunta.texto)

    def obtenerPuntajeOpcion(self):
        if self.opcion_siempre.isChecked(): return 3
        if self.opcion_frecuente.isChecked(): return 2
        if self.opcion_aveces.isChecked(): return 1
        if self.opcion_nunca.isChecked(): return 0
        return None

    def siguiente(self):
        puntaje = self.obtenerPuntajeOpcion()

        if puntaje is None:
            QMessageBox.warning(self, "Advertencia", "Debes seleccionar una opción.")
            return

        self.cuestionario[self.index].puntaje = puntaje
        self.puntaje_total += puntaje

        if self.index < self.maximo - 1:
            self.index += 1
            self.mostrarPregunta()
        else:
            self.finalizarTest()

    def finalizarTest(self):
        QMessageBox.information(
            self,
            "Resultado",
            f"Has finalizado el test.\n\nTu puntuación total es: {self.puntaje_total} puntos."
        )
    # PESTAÑA RESULTADOS
    def crear_pestana_resultados(self):
        layout = QGridLayout()
        etiqueta3 = QLabel("Resultados (a futuro puedes mostrar historial)")
        layout.addWidget(etiqueta3, 0, 0)
        self.tab_res.setLayout(layout)

# Ejecutar app
app = QApplication(sys.argv)
window = Principal()
window.show()
app.exec()
