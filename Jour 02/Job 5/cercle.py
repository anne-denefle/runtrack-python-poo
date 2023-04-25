import math

class Forme:
    def aire(self):
        return 0

class Rectangle(Forme):
    def __init__(self, largeur, hauteur):
        self.largeur = largeur
        self.hauteur = hauteur
    
    def aire(self):
        return self.largeur * self.hauteur

class Cercle(Forme):
    def __init__(self, radius):
        self.radius = radius
        
    def aire(self):
        return math.pi * self.radius ** 2

# Créer une instance de Rectangle et calculer son aire
mon_rectangle = Rectangle(5, 10)
print("L'aire du rectangle est :", mon_rectangle.aire())

# Créer une instance de Cercle et calculer son aire
mon_cercle = Cercle(4)
print("L'aire du cercle est :", mon_cercle.aire())
