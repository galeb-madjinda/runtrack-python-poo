class Personne:

    def __init__(self, prenom, nom):
        self.prenom = prenom
        self.nom = nom

    def SePresentery(self):
        print("Je suis", self.prenom, self.nom)

personne = Personne ('Galeb','Madjinda')
personne.SePresentery()

personne = Personne ('Anis','Anis')
personne.SePresentery()