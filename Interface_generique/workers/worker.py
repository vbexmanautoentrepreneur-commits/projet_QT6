from PyQt6.QtCore import QObject, pyqtSignal, QRunnable,QThreadPool

class WorkerSignals(QObject):
    finished = pyqtSignal(object)
    error = pyqtSignal(str)

class Worker(QRunnable):
    pool = QThreadPool.globalInstance()
    def __init__(self, fn, *args, **kwargs):

        super().__init__()
        self.fn = fn
        self.args = args
        self.kwargs = kwargs
        self.signals = WorkerSignals()

    def run(self):

        try:
            result = self.fn(*self.args, **self.kwargs)
            self.signals.finished.emit(result)

        except Exception as e:

            self.signals.error.emit(str(e))

    def start(self):

        Worker.pool.start(self)