from PyQt6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QPushButton,
    QTableWidget,
    QTableWidgetItem
)

from models import House
from ui.house_form import HouseForm


class MainWindow(QWidget):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("Gestion Immobilière")
        self.resize(900, 500)

        layout = QVBoxLayout()

        self.btn_add = QPushButton("Ajouter une maison")
        self.btn_add.clicked.connect(self.open_form)

        self.table = QTableWidget()

        layout.addWidget(self.btn_add)
        layout.addWidget(self.table)

        self.setLayout(layout)

        self.load_data()

    def load_data(self):

        houses = House.get_all()

        self.table.setColumnCount(7)
        self.table.setHorizontalHeaderLabels([
            "ID",
            "Ville",
            "Adresse",
            "Surface",
            "Chambres",
            "Prix",
            "Internet_Link"
        ])

        self.table.setRowCount(len(houses))

        for row_idx, row in enumerate(houses):
            for col_idx, value in enumerate(row):
                self.table.setItem(
                    row_idx,
                    col_idx,
                    QTableWidgetItem(str(value))
                )

    def open_form(self):
        self.form = HouseForm(self)
        self.form.show()