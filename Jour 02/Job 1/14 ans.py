class Personne: #définit la classe parent
    def __init__(self, age=14):
        self.age = age
        
    def afficherAge(self):
        print(f"J'ai {self.age} ans")
        
    def bonjour(self):
        print("Hello")
        
    def modifierAge(self, new_age):
        self.age = new_age
        
        
class Eleve(Personne): #définit la classe fille 1
    def allerEnCours(self):
        print("Je vais en cours")
        
    def affichageAge(self):
        print(f"J'ai {self.age} ans")
        
        
class Professeur(Personne): #définit la classe fille 2
    def __init__(self, matiereEnseignee, age=30):
        super().__init__(age)
        self.__matiereEnseignee = matiereEnseignee
        
    def enseigner(self):
        print("Le cours va commencer")

p1 = Personne()
e1 = Eleve()

print(e1.age)  # affiche 14

