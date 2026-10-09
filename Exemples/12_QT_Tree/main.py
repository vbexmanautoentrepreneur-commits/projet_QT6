from PyQt6.QtWidgets import QApplication, QTreeView
from PyQt6.QtGui import QFileSystemModel
import sys

app = QApplication(sys.argv)

model = QFileSystemModel()
model.setRootPath("")

tree = QTreeView()
tree.setModel(model)
tree.setRootIndex(model.index("C:/"))
tree.resize(800, 600)
tree.show()

sys.exit(app.exec())
