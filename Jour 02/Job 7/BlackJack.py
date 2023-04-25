import random

class Carte:
    def __init__(self, valeur, couleur):
        self.valeur = valeur
        self.couleur = couleur
    
    def __str__(self):
        if self.valeur == 1:
            return "As de " + self.couleur
        elif self.valeur == 11:
            return "Valet de " + self.couleur
        elif self.valeur == 12:
            return "Dame de " + self.couleur
        elif self.valeur == 13:
            return "Roi de " + self.couleur
        else:
            return str(self.valeur) + " de " + self.couleur


class Jeu:
    def __init__(self):
        self.paquet = []
        
    def initialiser(self):
        self.paquet = []
        for couleur in ["Coeur", "Pique", "Carreau", "Trèfle"]:
            for valeur in range(1, 14):
                self.paquet.append(Carte(valeur, couleur))
    
    def melanger(self):
        random.shuffle(self.paquet)
        
    def tirer_carte(self):
        return self.paquet.pop()
    
    def nouvelle_partie(self):
        self.initialiser()
        self.melanger()
        self.main_joueur = [self.tirer_carte(), self.tirer_carte()]
        self.main_croupier = [self.tirer_carte(), self.tirer_carte()]
    

def calculer_points(main):
    total = 0
    as_count = 0
    for carte in main:
        if carte.valeur == 1:
            as_count += 1
            total += 11
        elif carte.valeur > 10:
            total += 10
        else:
            total += carte.valeur
    while as_count > 0 and total > 21:
        total -= 10
        as_count -= 1
    return total


def afficher_main(main):
    for carte in main:
        print(carte)


def jouer_partie():
    jeu = Jeu()
    jeu.nouvelle_partie()
    print("Main du joueur :")
    afficher_main(jeu.main_joueur)
    print("Main du croupier :")
    print(jeu.main_croupier[0])
    while True:
        choix = input("Voulez-vous tirer une carte (T) ou passer (P) ? ")
        if choix.lower() == "t":
            nouvelle_carte = jeu.tirer_carte()
            jeu.main_joueur.append(nouvelle_carte)
            print("Vous avez tiré :")
            print(nouvelle_carte)
            points_joueur = calculer_points(jeu.main_joueur)
            print("Total des points : ", points_joueur)
            if points_joueur > 21:
                print("Vous avez perdu !")
                return
        elif choix.lower() == "p":
            points_joueur = calculer_points(jeu.main_joueur)
            print("Total des points : ", points_joueur)
            break
    print("Main du croupier :")
    afficher_main(jeu.main_croupier)
    while calculer_points(jeu.main_croupier) < 17:
        nouvelle_carte = jeu.tirer_carte()
        jeu.main_croupier.append(nouvelle_carte)
        print("Le croupier tire une carte :")
        print(nouvelle_carte)
        points_croupier = calculer_points(jeu.main_croupier)
        print("Total des points du croupier : ", points_croupier)
        if points_croupier > 21:
            print("Le croupier a dépassé 21 points, vous avez gagné !")
            return
    points_croupier = calculer_points(jeu.main_croupier)
    print("Total des points du croupier : ", points_croupier)
    points_joueur = calculer_points(jeu.main_joueur)
    if points_croupier > points_joueur:
        print("Le croupier a gagné !")
    elif points_croupier < points_joueur:
        print("Vous avez gagné !")
    else:
        print("Égalité !")


jouer_partie()

           
