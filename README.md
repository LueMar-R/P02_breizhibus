# P02_breizhibus

##  La base de données 

## Le fonctionnement de l'appli

## choix techniques

Le code python se compose de 6 fichiers :
- Un fichier ["main"](main.py) de quelques lignes qui sert à lancer l'appli,
- Un fichier ["fenêtre principale"](fenetre_principale.py), qui contient la classe _Fenetre_ et permet d'afficher, lors de l'appel par le main, une instance de cette classe.
- deux fichiers ["fenêtre ajout"](fenetre_ajout.py) et ["fenêtre modif"](fenetre_modif.py) qui contiennent deux classes du même nom qui permettent d'afficher, lorsqu'elles sont appelées par la classe _Fenetre_, respectivement une fenêtre qui permet d'ajouter et une qui permet de modifier/supprimer un bus.
- Un fichier ["bdd"](bdd.py) qui crée la connexion avec la base de données mysql et contient diverses méthodes applicables pour requérir les données.
- Un fichier ["popup"](popup.py) qui contient une classe du même nom et permet l'affichage de fenêtre popup dans divers cas d'erreurs (dont l'affichage est géré dnas le code par la gestion des excepions _try/except_)

Les principaux modules pythons utilisés sont :
* `mysql.connector`, qui permet  de créer la connexion avec la base de données,
* `pyqt5`, pour la création de toute l'interface graphique.

## difficultés rencontrées 

J'ai réalisé ma première inteface graphique pour ce projet. J'ai donc dû apprendre à utiliser PyQt depuis la abse pour pouvoir le réaliser.
