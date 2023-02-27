class Point : 

    def __init__(self, x , y):
        self.x = x
        self.y = y

#Affiche les cordonnées de X & Y
    def afficherLesPoints(self):
        print("Les coordonnées des points X et Y sont :",  "(", self.x, ";", self.y, ")")

#Donne la valeur de X
    def afficherX(self):
        return self.x

#Donne la valeur de Y
    def afficherY(self):
        return self.y

#Change la valeur de X
    def changerX (self):
        x = int(input("Entrer une nouvelle cordonnée pour X :"))
        print("La nouvelle cordonnée de X est :", x)

#Change la valeur de Y
    def changerY (self):
        y = int(input("Entrer une nouvelle cordonnée pour Y :"))
        print("La nouvelle cordonnée de Y est :", y)
        


AfficherLesPoints = Point(6, 10)
AfficherLesPoints.afficherLesPoints()

x = Point(6,10)
print("X a pour cordonnée :", x.afficherX())

y = Point(6,10)
print("Y a pour cordonnée :", y.afficherY())


print(x.changerX())

print(y.changerY())

