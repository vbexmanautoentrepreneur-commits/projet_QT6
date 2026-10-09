from PyQt6.QtWidgets import (QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QMessageBox)

from models import House


class HouseForm(QWidget):

    def __init__(self, parent=None):
        super().__init__()

        self.parent = parent

        self.setWindowTitle("Nouvelle maison")
        self.resize(400, 300)

        layout = QVBoxLayout()

        self.city = QLineEdit()
        self.address = QLineEdit()
        self.surface = QLineEdit()
        self.bedrooms = QLineEdit()
        self.price = QLineEdit()
        self.internet_link = QLineEdit()

        layout.addWidget(QLabel("Ville"))
        layout.addWidget(self.city)

        layout.addWidget(QLabel("Adresse"))
        layout.addWidget(self.address)

        layout.addWidget(QLabel("Surface"))
        layout.addWidget(self.surface)

        layout.addWidget(QLabel("Chambres"))
        layout.addWidget(self.bedrooms)

        layout.addWidget(QLabel("Prix"))
        layout.addWidget(self.price)

        layout.addWidget(QLabel("Internet_link"))
        layout.addWidget(self.internet_link)

        btn_save = QPushButton("Enregistrer")
        btn_save.clicked.connect(self.save)

        layout.addWidget(btn_save)

        self.setLayout(layout)

    def save(self):

        House.add(
            self.city.text(),
            self.address.text(),
            float(self.surface.text()),
            int(self.bedrooms.text()),
            float(self.price.text()),
            self.internet_link.text()
        )

        QMessageBox.information(self, "Information", "Maison enregistrée")
        self.parent.load_data()
        self.close()