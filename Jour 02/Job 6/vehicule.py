class Vehicule:
    def __init__(self, marque, annee, prix):
        self.marque = marque
        self.annee = annee
        self.prix = prix
    
    def informationsVehicule(self, modele):
        print("Marque:", self.marque)
        print("Modèle:", modele)
        print("Année:", self.annee)
        print("Prix:", self.prix)

    def demarrer(self):
        print("Attention, je roule.")



class Voiture(Vehicule):
    def __init__(self, marque, modele, annee, prix, portes=4):
        super().__init__(marque, annee, prix)
        self.modele = modele
        self.portes = portes
    
    def informationsVehicule(self):
        super().informationsVehicule(self.modele)
        print("Nombre de portes:", self.portes)
    
    def demarrer(self):
        print("La voiture démarre. Celle-ci n'a pas", self.portes, "portes, mais deux", "mon modèle préféré est", self.modele)


class Moto(Vehicule):
    def __init__(self, marque, modele, annee, prix, roue=2):
        super().__init__(marque, annee, prix)
        self.modele = modele
        self.roue = roue
    
    def informationsVehicule(self):
        super().informationsVehicule(self.modele)
        print("Nombre de roues:", self.roue)
    
    def demarrer(self):
        print("La moto démarre.", self.marque, "est une moto à", self.roue, "qu'on entend de loin !")


ma_voiture = Voiture("Porsche", "GT4S", 2022, 8000)
ma_voiture.informationsVehicule()
ma_voiture.demarrer()

ma_moto = Moto("Harley Davidson", "Low Rider", 2020, 12000)
ma_moto.informationsVehicule()
ma_moto.demarrer()
