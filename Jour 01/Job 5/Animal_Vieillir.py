class Animal:
    def __init__(self):
        self.age = 0
        self.prenom = ""

    def vieillir(self):
        self.age += 1

    def nommer(self, prenom):
        self.prenom = prenom

    # Instancier un objet Animal
mon_animal = Animal()

# Afficher l'âge initial de l'animal
print("L'âge initial de l'animal est :", mon_animal.age)
# Faire vieillir l'animal
mon_animal.vieillir()

# Afficher le nouvel âge de l'animal
print("L'âge de l'animal après une année est :", mon_animal.age)

mon_animal.nommer("Bob")
print ("il s'appelle", mon_animal.prenom)