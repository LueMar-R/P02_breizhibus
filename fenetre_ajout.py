# -*- coding : utf8 -*-
import sys
from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import QRect
from PyQt5.QtWidgets import QDialog, QApplication, QWidget, QComboBox, QMainWindow
from PyQt5.QtWidgets import QPushButton, QVBoxLayout, QLabel, QLineEdit, QStyleFactory
import mysql.connector
from bdd import Bdd
from popup import Popup

class FenAjout(QDialog):
    def __init__(self):
        QDialog.__init__(self)
        self.setWindowTitle("Breizhibus - Ajouter un bus")
        self.setGeometry(400,200,300,350)
        self.setStyleSheet("background: #b9f20a;") 

        self.initUI()
        self.init_data()
        self.initCmd()

    def initUI(self):
        self.nom_bus = QLabel()
        self.nom_bus.setText("Numero du nouveau bus :")
        self.immat = QLabel()
        self.immat.setText("Immatriculation :")
        self.nbplace = QLabel()
        self.nbplace.setText("Nombre de places :")
        self.choixli = QLabel()
        self.choixli.setText("Ligne à affecter :")
        self.retour = QLabel()
        self.affect_ligne = QComboBox(self)
        self.champ1 = QLineEdit()
        self.champ2 = QLineEdit()
        self.champ3 = QLineEdit()
        self.btok = QPushButton("Ajouter")

        layout = QVBoxLayout()
        layout.addWidget(self.nom_bus)     
        layout.addWidget(self.champ1)
        layout.addWidget(self.immat)
        layout.addWidget(self.champ2)
        layout.addWidget(self.nbplace)
        layout.addWidget(self.champ3)
        layout.addWidget(self.choixli)
        layout.addWidget(self.affect_ligne)
        layout.addWidget(self.btok)
        layout.addWidget(self.retour)
        self.setLayout(layout)

    def init_data(self):
        try:
            self.donnees = Bdd()
        except mysql.connector.errors.InterfaceError :
            self.pop = Popup()
            self.pop.connex_err()

    def initCmd(self):
        self.btok.clicked.connect(self.appui_ok) 
        self.affect_ligne.addItems(self.donnees.lister_lignes()) 

    def appui_ok(self):
        num = self.champ1.text() 
        immat = self.champ2.text()
        places = int(self.champ3.text()) 
        ligne = self.affect_ligne.currentText()
        bus_existants = self.donnees.lister_bus()
        if num in bus_existants: 
            self.pop1 = Popup()
            self.pop1.ref_exist_err()
        else : 
            if (bool(num) & bool(immat) & bool(places)):
                try:
                    self.donnees.ajouter_bus(num, immat, places, ligne[0])
                    self.retour.setText(f"Le bus {num} a bien été ajouté en base")
                    self.champ3.setText("")
                    self.champ1.setText("")
                    self.champ2.setText("")
                except ValueError:
                    self.pop2 = Popup()
                    self.pop2.erreur_valeur() 
            else :
                self.pop3 = Popup()
                self.pop3.champ_vide_err() 

