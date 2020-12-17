import mysql.connector

class Bdd :

    @classmethod
    def ouvrir_connexion(cls):
        cls.bdd = mysql.connector.connect(user='root', password='root', host='localhost', port="8081", database='breizhibus')
        cls.curs = cls.bdd.cursor()

    @classmethod
    def fermer_connexion(cls):
        cls.curs.close()
        cls.bdd.close()

    @classmethod
    def lister_lignes(cls) :
        cls.ouvrir_connexion()
        cls.curs.execute("SELECT id_ligne, nom FROM lignes")
        result = cls.curs.fetchall()
        ls = []
        cls.fermer_connexion()
        for ligne in result :
            ligne = " : ".join(str(ligne[i]) for i in range(len(ligne)))
            ls.append(ligne)
        return ls

    @classmethod
    def affichage_lignes(cls) :
        cls.ouvrir_connexion()
        ll = "Lignes Breizhibus : \n"
        cls.curs.execute("SELECT * FROM lignes")
        for line in cls.curs :
            ll += str(line[0]) + " : " + line[1] + "\n"
        return ll

    @classmethod
    def lister_arrets(cls, numero):
        cls.ouvrir_connexion()
        query = f"SELECT nom FROM arrets \
                    JOIN arrets_lignes \
                    ON arrets.id_arret = arrets_lignes.id_arret \
                    WHERE id_ligne = {numero} "
        cls.curs.execute(query)
        result = cls.curs.fetchall()
        cls.fermer_connexion()
        return result

    @classmethod
    def lister_bus_ligne(cls, numero):
        cls.ouvrir_connexion()
        query = f"SELECT numero FROM bus \
                    WHERE id_ligne = {numero} "
        cls.curs.execute(query)
        result = cls.curs.fetchall()
        cls.fermer_connexion()
        return result

    @classmethod
    def lister_bus(cls):
        cls.ouvrir_connexion()
        query = f"SELECT numero FROM bus"
        cls.curs.execute(query)
        result = cls.curs.fetchall()
        cls.fermer_connexion()
        lb=[]
        for bus in result :
            lb.append(bus[0])
        print(lb)
        return lb

    @classmethod
    def ajouter_bus(cls, numero, immat, places, id_ligne):
        cls.ouvrir_connexion()
        val = (numero, immat, places, id_ligne)
        query = "INSERT INTO bus (numero, immatriculation, nombre_place, id_ligne) VALUES (%s, %s, %s, %s)"
        cls.curs.execute(query, val)
        cls.bdd.commit()
        cls.fermer_connexion()

    @classmethod
    def caracteriser_bus(cls, numero):
        cls.ouvrir_connexion()
        query = f"SELECT immatriculation, nombre_place, id_ligne FROM bus \
                    WHERE numero='{numero}' "
        cls.curs.execute(query)
        result = cls.curs.fetchall()
        cls.fermer_connexion()
        print(result)
        return result


    @classmethod
    def modifier_bus(cls, numero, immat, places, id_ligne):
        cls.ouvrir_connexion()
        query = f"UPDATE bus SET immatriculation='{immat}', nombre_place={places}, id_ligne={id_ligne} WHERE numero='{numero}'"
        cls.curs.execute(query)
        cls.bdd.commit()
        cls.fermer_connexion()

    @classmethod
    def supprimer_bus(cls, numero):
        cls.ouvrir_connexion()
        query = f"DELETE FROM bus WHERE numero='{numero}'"
        cls.curs.execute(query)
        cls.bdd.commit()
        cls.fermer_connexion()