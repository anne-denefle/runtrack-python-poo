class Forme:
    def aire(self):
        return 0

class Rectangle(Forme):
    def __init__(self, largeur, hauteur):
        self.largeur = largeur
        self.hauteur = hauteur
    
    def aire(self):
        return self.largeur * self.hauteur

# Créer un rectangle de largeur 5 et de hauteur 10
mon_rectangle = Rectangle(5, 10)

# Imprimer l'aire du rectangle
print("l'aire du rectangle est:", mon_rectangle.aire())  # aire du rectangle
