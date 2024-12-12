import sys
import requests
from PyQt5.QtWidgets import (
    QApplication, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QPushButton,
    QListWidget, QMessageBox, QWidget
)
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt

API_URL = "http://127.0.0.1:8000/api/proyectos_list/"

class ProjectManager(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Gestión de Grupos - API")
        self.setStyleSheet("background-color: black; color: #D8BFD8;")
        
        
        self.font_general = QFont("Arial", 12, QFont.Bold)

        layout = QVBoxLayout()

        
        form_layout = QVBoxLayout()
        self.nombre_input = self.create_input_field("Nombre:")
        self.rut_input = self.create_input_field("RUT:")
        self.edad_input = self.create_input_field("Edad:")
        self.localidad_input = self.create_input_field("Localidad:")

        form_layout.addLayout(self.nombre_input[1])
        form_layout.addLayout(self.rut_input[1])
        form_layout.addLayout(self.edad_input[1])
        form_layout.addLayout(self.localidad_input[1])

        layout.addLayout(form_layout)

        
        button_layout = QHBoxLayout()
        agregar_button = QPushButton("Agregar Integrantes")
        agregar_button.setFont(self.font_general)
        agregar_button.setStyleSheet("background-color: black; color: #D8BFD8; border: 2px solid #D8BFD8;")
        agregar_button.clicked.connect(self.agregar_proyecto)

        cargar_button = QPushButton("Cargar Integrantes")
        cargar_button.setFont(self.font_general)
        cargar_button.setStyleSheet("background-color: black; color: #D8BFD8; border: 2px solid #D8BFD8;")
        cargar_button.clicked.connect(self.cargar_proyectos)

        button_layout.addWidget(agregar_button)
        button_layout.addWidget(cargar_button)

        layout.addLayout(button_layout)

        
        self.lista_proyectos = QListWidget()
        self.lista_proyectos.setFont(self.font_general)
        self.lista_proyectos.setStyleSheet("""
            QListWidget {
                background-image: url(Aespa________.jpg);
                background-repeat: no-repeat;
                background-position: center;
                border: 2px solid #D8BFD8;
                color: #D8BFD8;
            }
        """)
        layout.addWidget(self.lista_proyectos)

        self.setLayout(layout)

    def create_input_field(self, label_text):
        label = QLabel(label_text)
        label.setFont(self.font_general)
        label.setStyleSheet("color: #D8BFD8;")
        input_field = QLineEdit()
        input_field.setFont(self.font_general)
        input_field.setStyleSheet("background-color: black; color: #D8BFD8; border: 2px solid #D8BFD8;")
        layout = QHBoxLayout()
        layout.addWidget(label)
        layout.addWidget(input_field)
        return input_field, layout

    def cargar_proyectos(self):
        try:
            response = requests.get(API_URL)
            response.raise_for_status()
            proyectos = response.json()

            self.lista_proyectos.clear()
            for proyecto in proyectos:
                self.lista_proyectos.addItem(
                    f"ID: {proyecto['id']} - Nombre: {proyecto['nombre']}, RUT: {proyecto['rut']}, Edad: {proyecto['edad']}, Localidad: {proyecto['localidad']}"
                )
        except requests.exceptions.RequestException as e:
            QMessageBox.critical(self, "Error", f"No se pudieron cargar los integrantes: {e}")

    def agregar_proyecto(self):
        nombre = self.nombre_input[0].text().strip()
        rut = self.rut_input[0].text().strip()
        edad = self.edad_input[0].text().strip()
        localidad = self.localidad_input[0].text().strip()

        if not nombre or not rut or not edad or not localidad:
            QMessageBox.warning(self, "Advertencia", "Todos los campos son obligatorios")
            return

        try:
            data = {"nombre": nombre, "rut": rut, "edad": int(edad), "localidad": localidad}
            response = requests.post(API_URL, json=data)
            response.raise_for_status()

            QMessageBox.information(self, "Éxito", "Integrante agregado correctamente")
            self.cargar_proyectos()
            self.nombre_input[0].clear()
            self.rut_input[0].clear()
            self.edad_input[0].clear()
            self.localidad_input[0].clear()
        except requests.exceptions.RequestException as e:
            QMessageBox.critical(self, "Error", f"No se pudo agregar el proyecto: {e}")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ProjectManager()
    window.resize(600, 400)
    window.show()
    sys.exit(app.exec_())
