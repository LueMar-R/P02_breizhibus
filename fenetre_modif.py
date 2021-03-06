# -*- coding : utf8 -*-
import sys
from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import QRect
from PyQt5.QtWidgets import QDialog, QApplication, QWidget, QComboBox, QTabWidget
from PyQt5.QtWidgets import QPushButton, QGridLayout, QLabel, QLineEdit, QStyleFactory
import mysql.connector
from bdd import Bdd
from popup import Popup

class FenModif(QDialog):
    def __init__(self):
        QDialog.__init__(self)
        self.setWindowTitle("Breizhibus - modifier / supprimer")
        self.setGeometry(400,200,403,319)
        self.setStyleSheet("background: #b9f20a;") 

        self.initUI()
        self.init_data()
        self.initCmd()

    def initUI(self):
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(185, 242, 10))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(222, 255, 119))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(203, 248, 64))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(92, 121, 5))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(123, 161, 6))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 170, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(185, 242, 10))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 170, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.HighlightedText, brush)
        brush = QtGui.QBrush(QtGui.QColor(220, 248, 132))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(185, 242, 10))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(222, 255, 119))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(203, 248, 64))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(92, 121, 5))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(123, 161, 6))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 170, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(185, 242, 10))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 170, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(185, 242, 10))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(222, 255, 119))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(203, 248, 64))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(92, 121, 5))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(123, 161, 6))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(92, 121, 5))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 170, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(92, 121, 5))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(185, 242, 10))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(185, 242, 10))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 170, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        self.setPalette(palette)
        self.nom_bus = QtWidgets.QLabel() # QtWidgets.QLabel(Dialog)
        self.nom_bus.setGeometry(QtCore.QRect(90, 10, 201, 20))
        self.nom_bus.setAlignment(QtCore.Qt.AlignCenter)
        self.nom_bus.setObjectName("nom_bus")
        self.nom_bus.setText("Numéro du bus à modifier/supprimer :")
        self.tabWidget = QtWidgets.QTabWidget() #
        self.tabWidget.setGeometry(QtCore.QRect(0, 70, 401, 251))
        self.tabWidget.setTabPosition(QtWidgets.QTabWidget.North)
        self.tabWidget.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.tabWidget.setElideMode(QtCore.Qt.ElideNone)
        self.tabWidget.setObjectName("tabWidget")
        self.tab_modifier = QtWidgets.QWidget()
        self.tab_modifier.setObjectName("tab_modifier")
        #self.tab_modifier.setText("Modifier un bus")
        self.champ_immat = QtWidgets.QLineEdit(self.tab_modifier)
        self.champ_immat.setGeometry(QtCore.QRect(140, 30, 211, 20))
        self.champ_immat.setObjectName("champ_immat")
        self.affect_ligne = QtWidgets.QComboBox(self.tab_modifier)
        self.affect_ligne.setGeometry(QtCore.QRect(140, 110, 111, 22))
        self.affect_ligne.setObjectName("affect_ligne")
        self.btok_2 = QtWidgets.QPushButton(self.tab_modifier)
        self.btok_2.setGeometry(QtCore.QRect(130, 160, 121, 23))
        self.btok_2.setObjectName("btok_2")
        self.btok_2.setText("Valider")
        self.immat = QtWidgets.QLabel(self.tab_modifier)
        self.immat.setGeometry(QtCore.QRect(30, 30, 111, 20))
        self.immat.setObjectName("immat")
        self.immat.setText( "Immatricultaion :")
        self.nbplace = QtWidgets.QLabel(self.tab_modifier)
        self.nbplace.setGeometry(QtCore.QRect(30, 70, 111, 20))
        self.nbplace.setObjectName("nbplace")
        self.nbplace.setText("Nombre de places :")
        self.choixli = QtWidgets.QLabel(self.tab_modifier)
        self.choixli.setGeometry(QtCore.QRect(30, 110, 111, 20))
        self.choixli.setObjectName("choixli")
        self.choixli.setText("Ligne d\'affectation :")
        self.champ_place = QtWidgets.QLineEdit(self.tab_modifier)
        self.champ_place.setGeometry(QtCore.QRect(140, 70, 211, 20))
        self.champ_place.setObjectName("champ_place")
        self.retour = QtWidgets.QLabel(self.tab_modifier)
        self.retour.setGeometry(QtCore.QRect(80, 190, 221, 20))
        self.retour.setText("")
        self.retour.setAlignment(QtCore.Qt.AlignCenter)
        self.retour.setObjectName("retour")
        self.tabWidget.addTab(self.tab_modifier, "Modifier le bus")
        self.tab_supprimer = QtWidgets.QWidget()
        self.tab_supprimer.setObjectName("tab_supprimer")
        #self.tab_supprimer.setText("Supprimer de la base")
        self.image = QtWidgets.QLabel(self.tab_supprimer)
        self.image.setGeometry(QtCore.QRect(140, 10, 91, 91))
        self.image.setText("")
        self.image.setPixmap(QtGui.QPixmap("corbeille.png"))
        self.image.setScaledContents(True)
        self.image.setAlignment(QtCore.Qt.AlignCenter)
        self.image.setObjectName("image")
        self.avert = QtWidgets.QLabel(self.tab_supprimer)
        self.avert.setGeometry(QtCore.QRect(6, 110, 381, 20))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 92, 10))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 92, 10))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(92, 121, 5))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        self.avert.setPalette(palette)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.avert.setFont(font)
        self.avert.setAlignment(QtCore.Qt.AlignCenter)
        self.avert.setObjectName("avert")
        self.avert.setText("Etes-vous sûr(e) de vouloir faire celà ?")
        self.label = QtWidgets.QLabel(self.tab_supprimer)
        self.label.setGeometry(QtCore.QRect(10, 140, 371, 20))
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.label.setText("Cette action est définitive et ne peut pas être annulée...")
        self.btok2 = QtWidgets.QPushButton(self.tab_supprimer)
        self.btok2.setGeometry(QtCore.QRect(104, 170, 181, 23))
        self.btok2.setObjectName("btok2")
        self.btok2.setText("Supprimer quand même !")
        self.tabWidget.addTab(self.tab_supprimer, "Supprimer de la base")
        self.choix_bus = QtWidgets.QComboBox()
        self.choix_bus.setGeometry(QtCore.QRect(140, 40, 101, 22))
        self.choix_bus.setObjectName("choix_bus")

        self.tabWidget.setCurrentIndex(0)

        layout = QGridLayout()
        layout.addWidget(self.nom_bus)     
        layout.addWidget(self.choix_bus)
        layout.addWidget(self.tabWidget)
        self.setLayout(layout)

    def init_data(self):
        try:
            self.donnees = Bdd()
        except mysql.connector.errors.InterfaceError :
            self.pop = Popup()
            self.pop.connex_err()

    def initCmd(self):
        self.choix_bus.addItems(self.donnees.lister_bus())
        self.btok_2.clicked.connect(self.modification) 
        self.affect_ligne.addItems(self.donnees.lister_lignes())
        self.btok2.clicked.connect(self.suppression) 


    def suppression(self):
        numero = self.choix_bus.currentText()
        self.donnees.supprimer_bus(numero)
        self.pop = Popup()
        self.pop.suppr_reussie()
        self.close()

    def modification(self):
        numero = self.choix_bus.currentText()
        immat = self.champ_immat.text()
        places = self.champ_place.text()
        id_ligne = self.affect_ligne.currentText()
        id_ligne = id_ligne[0]
        if (bool(immat) & bool(places)):
            try:
                self.donnees.modifier_bus(numero, immat, places, id_ligne)
                self.retour.setText("La modification a été effectuée.")
                self.champ_immat.clear()
                self.champ_place.clear()
            except ValueError:
                self.pop2 = Popup()
                self.pop2.erreur_valeur() 
        else :
            self.pop3 = Popup()
            self.pop3.champ_vide_err() 