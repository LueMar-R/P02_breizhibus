# -*- coding : utf8 -*-
import sys
from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtGui import QPixmap, QFont
from PyQt5.QtCore import QRect
from PyQt5.QtWidgets import QDialog, QApplication, QWidget, QComboBox, QMainWindow
from PyQt5.QtWidgets import QPushButton, QVBoxLayout, QLabel, QLineEdit, QStyleFactory
import mysql.connector
from bdd import Bdd
from popup import Popup
from fenetre_ajout import FenAjout
from fenetre_modif import FenModif
from ui_modif import Ui_Modif

class Fenetre(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.setWindowTitle("Breizhibus - Ploukuzanagi")
        self.setGeometry(320,40,300,680)
        self.setStyleSheet("background: #b9f20a;") 

        self.initUI()
        self.init_data()
        self.initCmd()

    def initUI(self):
        self.logo = QLabel()
        self.logo.setGeometry(0,0,300,300)
        self.logo.setText("")
        self.logo.setPixmap(QPixmap("logo2.png"))
        self.logo.setScaledContents(False)
        self.liste_lignes = QLabel()
        self.liste_lignes.setAlignment(QtCore.Qt.AlignCenter)
        self.liste_lignes.setFont(QFont("MS Shell Dlg 2", 10))
        self.texte_invit = QLabel()
        self.texte_invit.setText("Afficher les arrêts de la ligne :")
        self.combo = QComboBox()
        self.bouton = QPushButton("Rechercher") 
        self.bouton.setStyleSheet("background: #dff0c1;")
        self.bappel = QPushButton("Ok")
        self.bappel.setStyleSheet("background: #dff0c1;")
        self.label1 = QLabel()
        self.label1.setAlignment(QtCore.Qt.AlignCenter)
        self.label1.setFont(QFont("MS Shell Dlg 2", 9))
        self.label2 = QLabel() 
        self.label2.setAlignment(QtCore.Qt.AlignCenter)
        self.label2.setFont(QFont("MS Shell Dlg 2", 9))
        self.combo2 = QComboBox()

        layout = QVBoxLayout()
        layout.addWidget(self.logo)
        layout.addWidget(self.liste_lignes)     
        layout.addWidget(self.texte_invit)
        layout.addWidget(self.combo)
        layout.addWidget(self.bouton)
        layout.addWidget(self.label1)
        layout.addWidget(self.label2)
        layout.addWidget(self.combo2)
        layout.addWidget(self.bappel)
        self.setLayout(layout)

    def init_data(self):
        try:
            self.donnees = Bdd()
        except mysql.connector.errors.InterfaceError :
            self.pop = Popup()
            self.pop.connex_err()

    def initCmd(self):
        self.bouton.clicked.connect(self.appui_bouton) ##### envoyer vers commandes
        self.bappel.clicked.connect(self.commande_outil) ##### envoyer vers commandes
        self.liste_lignes.setText(self.donnees.affichage_lignes()) ##### envoyer vers commandes
        self.combo.addItems(self.donnees.lister_lignes()) ##### envoyer vers commandes
        self.combo2.addItems([" gestionnaire...", "Ajouter un bus", "Modifier ou supprimer un bus", "Calculer un itinéraire"])

    def appui_bouton(self):
        num_ligne = self.combo.currentText()
        num_ligne = int(num_ligne[0])
        # affichage des arrêts 
        ls = ["Arrêts :"]
        result = self.donnees.lister_arrets(num_ligne) 
        for i in result :
            ls.append(i[0])
        ls = "\n".join(ls)
        self.label1.setText(ls)
        # affichage des bus
        ls2 = ["Bus de la ligne :"]
        result2 = self.donnees.lister_bus_ligne(num_ligne) 
        for i in result2 :
            ls2.append(i[0])
        ls2 = "\n".join(ls2)
        self.label2.setText(ls2)

    def commande_outil(self): #!!
        if self.combo2.currentText() == "Ajouter un bus":
            self.fenetre_ajout = FenAjout()
            self.fenetre_ajout.show()
        elif self.combo2.currentText() == "Modifier ou supprimer un bus":
            print("modifier")
            self.fen_mod = FenModif()
            self.fen_mod.show()
        elif self.combo2.currentText() == "Calculer un itinéraire":
            print("calculer")
        else :
            self.pop = Popup()
            self.pop.choix_manquant()


