class Rectangle:
    def __init__(self, longueur, largeur):
        self.__longueur = longueur
        self.__largeur = largeur
    
    def perimetre(self):
        return 2 * (self.__longueur + self.__largeur)
    
    def surface(self):
        return self.__longueur * self.__largeur
    
    def get_longueur(self):
        return self.__longueur
    
    def set_longueur(self, longueur):
        self.__longueur = longueur
    
    def get_largeur(self):
        return self.__largeur
    
    def set_largeur(self, largeur):
        self.__largeur = largeur


class Parallelepipede(Rectangle):
    def __init__(self, longueur, largeur, hauteur):
        super().__init__(longueur, largeur)
        self.__hauteur = hauteur
    
    def volume(self):
        return self.surface() * self.__hauteur
    
    def get_hauteur(self):
        return self.__hauteur
    
    def set_hauteur(self, hauteur):
        self.__hauteur = hauteur
r = Rectangle(5, 7)
print("le périmètre est:", r.perimetre())  # perimetre pour le premier rectangle
print("la surface est:", r.surface())  # surface pour le premier rectangle

r.set_longueur(8)
r.set_largeur(4)
print("le périmètre est: ", r.perimetre())  # perimetre du deuxieme
print("la surface est:", r.surface())  # surface du deuxieme


p = Parallelepipede(3, 4, 5)
print("le périmètre est: ", p.perimetre())  # perimetre du //
print("la surface est:", p.surface())  # surface du //
print("le volume est:", p.volume())  # Volume du //

p.set_longueur(6)
p.set_largeur(8)
p.set_hauteur(2)
print("le périmètre est: ", p.perimetre())  # perimetre du deuxieme //
print("la surface est:", p.surface())  # surface du deuxieme //
print("le volume est:", p.volume())  # volume du deuxieme //
