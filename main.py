import sys

from PyQt6.QtWidgets import QApplication

from views.main_window import MainWindow
from viewmodels.main_viewmodel import MainViewModel
from services.csv_service import CsvService


def main():

    app = QApplication(sys.argv)
    service = CsvService()
    vm = MainViewModel(service)
    window = MainWindow(vm)
    window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()