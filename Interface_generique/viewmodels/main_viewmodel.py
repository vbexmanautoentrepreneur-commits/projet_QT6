from PyQt6.QtCore import QObject
from PyQt6.QtCore import pyqtSignal

from Interface_generique.workers.worker import Worker


class MainViewModel(QObject):

    text_loaded = pyqtSignal(str)
    status_changed = pyqtSignal(str)

    def __init__(self, csv_service):

        super().__init__()
        self.csv_service = csv_service

    def load_csv(self):
        worker = Worker(self.csv_service.read_file)
        worker.signals.finished.connect(self.on_loaded)
        worker.signals.error.connect(self.status_changed.emit)
        worker.start()

    def on_loaded(self, content):
        self.text_loaded.emit(content)
        self.status_changed.emit("Chargement terminé")
