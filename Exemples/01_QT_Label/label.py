from PyQt6.QtWidgets import *
app = QApplication([])
label = QLabel('Hello World!')
label.resize(400, 300)
label.show()
app.exec()