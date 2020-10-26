import sys
from PyQt5 import QtWidgets

app = QtWidgets.QApplication(sys.argv)
window = QtWidgets.QMainWindow()
button = QtWidgets.QPushButton("Hello, world!")
window.setCentralWidget(button)
window.show()
sys.exit(app.exec_())
