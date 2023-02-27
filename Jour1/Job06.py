class Animal :

    def __init__(self, nom, age):
        self.nom = ''
        self.age = 0

    def Vieillir(self, age):
        self.age = age + 1
        print("L'animal a", self.age, "ans" )

    def nommer(self, nom):
        self.nom = nom
        print("L'animal se nomme",self.nom)

animal = Animal('Milou', 0)

animal.Vieillir(5)
animal.nommer('Milou')
