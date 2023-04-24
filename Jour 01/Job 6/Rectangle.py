class Rectangle:
    def __init__(self, longueur, largeur):
        self.__longueur = longueur
        self.__largeur = largeur

    def get_longueur(self):
        return self.__longueur

    def set_longueur(self, longueur):
        self.__longueur = longueur

    def get_largeur(self):
        return self.__largeur

    def set_largeur(self, largeur):
        self.__largeur = largeur

# Créer un rectangle avec une longueur de 10 et une largeur de 5
mon_rectangle = Rectangle(10, 5)

# Afficher la longueur et la largeur initiales du rectangle
print("Longueur initiale :", mon_rectangle.get_longueur())
print("Largeur initiale :", mon_rectangle.get_largeur())

# Modifier la longueur et la largeur du rectangle
mon_rectangle.set_longueur(18)
mon_rectangle.set_largeur(12)

# Afficher la longueur et la largeur modifiées du rectangle
print("Nouvelle longueur :", mon_rectangle.get_longueur())
print("Nouvelle largeur :", mon_rectangle.get_largeur())
