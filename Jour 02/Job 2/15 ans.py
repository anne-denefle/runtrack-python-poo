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

eleve1 = Eleve() # instancier un élève par défaut (âge = 14 ans)
eleve1.bonjour() # dire bonjour à l'élève
eleve1.allerEnCours() # faire aller l'élève en cours
eleve1.modifierAge(15) # redéfinir l'âge de l'élève à 15 ans

prof1 = Professeur("mathématiques", 40) # instancier un professeur de mathématiques de 40 ans
prof1.bonjour() # dire bonjour au professeur
prof1.enseigner() # faire commencer le cours du professeur
