from PyQt6.QtWidgets import (
    QMainWindow,
    QWidget,
    QVBoxLayout,
    QPushButton,
    QTextEdit,
    QLabel,
    QToolBar,
)

from config.settings import *


class MainWindow(QMainWindow):

    def __init__(self, vm):

        super().__init__()

        self.vm = vm

        self.setWindowTitle(APP_NAME)

        self.resize(
            WINDOW_WIDTH,
            WINDOW_HEIGHT
        )

        self.create_ui()

        self.connect_signals()

    def create_ui(self):

        toolbar = QToolBar()

        self.addToolBar(toolbar)

        toolbar.addAction("CSV")

        toolbar.addAction("Excel")

        toolbar.addAction("PLM")

        toolbar.addAction("Reports")

        central = QWidget()

        self.setCentralWidget(central)

        layout = QVBoxLayout()

        central.setLayout(layout)

        self.btn_load = QPushButton(
            "Charger CSV"
        )

        self.text = QTextEdit()

        self.status = QLabel(
            "Prêt"
        )

        layout.addWidget(
            self.btn_load
        )

        layout.addWidget(
            self.text
        )

        layout.addWidget(
            self.status
        )

    def connect_signals(self):

        self.btn_load.clicked.connect(
            self.vm.load_csv
        )

        self.vm.text_loaded.connect(
            self.update_text
        )

        self.vm.status_changed.connect(
            self.status.setText
        )

    def update_text(self, text):

        self.text.setPlainText(text)