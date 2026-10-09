from PyQt6.QtWidgets import *

app = QApplication([])
button = QPushButton('Click')
button.resize(200,300)
button.setStyleSheet("""
                        QPushButton { background-color: #28A745; color: white; border-radius: 10px; 
                                      padding: 10px; font-size: 14px; font-weight: bold; }
                        QPushButton:hover { background-color: #218838; }
                        """)

def on_button_clicked():
    alert = QMessageBox()
    alert.setText('You clicked the button!')
    alert.exec()

button.clicked.connect(on_button_clicked)

button.show()
app.exec()