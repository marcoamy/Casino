class Joueur():
    """
        « J'avais senti pétiller mon argent au moment qu'il avait
        lâché le mot de cartes et de dés. »
        Alexander Hamilton
    """

    def __init__(self, nom, argent):
        self.nom = nom
        self.argent = argent
        self.casino = None

    def entrer_casino(self, casino):
        if casino.ajouter_joueur(self):
            self.casino = casino
            return True
        return False

    def sortir_casino(self):
        self.casino.enlever_joueur(self)

    def jouer(self):
        self.casino.afficher_jeux()
        choix = -1
        while choix < 0 or choix > len(self.casino.jeux):
            choix = input("A quel jeu (n°) voulez-vous jouer ?")
            try:
                choix = int(choix)
            except ValueError:
                print("Vous n'avez pas saisi de nombre")
                choix = -1
                continue
            if choix < 0:
                print("Le choix saisie est negatif.")
            if choix > len(self.casino.jeux):
                print("Nous n'avons pas ce jeu desole.")
        print("Excellent choix, bonne partie, amusez-vous bien !")
        self.casino.jeux[choix].jouer(self)