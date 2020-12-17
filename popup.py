import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMessageBox

class Popup(QMessageBox):
    def __init__(self):
        QMessageBox.__init__(self)
        self.msg = QMessageBox()
        self.msg.setWindowTitle("Breizhibus - Erreur")
        self.msg.setStyleSheet("background-color: #36d292")

    def champ_vide_err(self):
    	self.msg.setIcon(QMessageBox.Critical)
    	self.msg.setText(f"Tous les champs sont obligatoires")
    	x = self.msg.exec_()

    def erreur_valeur(self):
        self.msg.setIcon(QMessageBox.Critical)
        self.msg.setText(f"Le nombre de place doit être un entier.")
        x = self.msg.exec_()

    def ref_exist_err(self):
    	self.msg.setIcon(QMessageBox.Critical)
    	self.msg.setText(f"Cette référence existe déjà dans la base !")
    	x = self.msg.exec_()    	

    def connex_err(self):
    	self.msg.setIcon(QMessageBox.Critical)
    	self.msg.setText(f"Une erreur est survenue. Vérifiez votre connexion avec le serveur et relancez l'application.")
    	x = self.msg.exec_()   

    def choix_manquant(self):
        self.msg.setIcon(QMessageBox.Warning)
        self.msg.setText(f"Veuillez faire un choix dans la liste déroulante.")
        x = self.msg.exec_()   

    def suppr_reussie(self):
        self.msg.setIcon(QMessageBox.Information)
        self.msg.setText(f"Le bus a bien été supprimé.")
        x = self.msg.exec_()   