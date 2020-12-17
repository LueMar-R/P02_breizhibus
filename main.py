from PyQt5 import QtWidgets, QtGui
from PyQt5.QtWidgets import QApplication, QStyleFactory
from PyQt5.QtGui import QFont
from fenetre_principale import Fenetre
import sys

def main():
    app = QApplication.instance() 
    if not app:
        app = QApplication(sys.argv)
    app.setStyle(QStyleFactory.create("Fusion"))

    fen = Fenetre()
    font = QtGui.QFont("Noto Serif Lao", 12, QtGui.QFont.Bold)
    fen.setFont(font)
    fen.show()

    app.exec_()

main()
