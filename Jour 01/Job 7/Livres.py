class Livres:
    def __init__(self, titre, auteur, nbre_pages):
        self.__titre = titre
        self.__auteur = auteur
        self.__nbre_pages = nbre_pages
    def get_titre(self):
        return self.__titre
    def set_titre(self, titre):
        self.__titre = titre

    def get_auteur(self):
        return self.__auteur
    def set_auteur(self, auteur):
        self.__auteur = auteur

    def get_nbre_pages(self):
        return self.__nbre_pages
    
    def set_nbre_pages(self, nbre_pages):
        if not isinstance(nbre_pages, int):
            print("Erreur : le nombre de pages doit être un entier positif.")
        elif nbre_pages <= 0:
            print("Erreur : le nombre de pages doit être un entier positif.")
        else:
            self.__nbre_pages = nbre_pages
# Créer un livre dans la base 
mon_livre = Livres("American Psycho", "Bret Easton Ellis",0)
mon_livre.set_nbre_pages(526)
#écrire la liste
print("Premier Livre:", mon_livre.get_titre(),",", mon_livre.get_auteur(),",", 
      mon_livre.get_nbre_pages(), "pages.")
