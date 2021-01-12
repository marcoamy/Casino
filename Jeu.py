class Jeu():
    """
        « On peut en savoir plus sur quelqu'un en une heure de jeu
        qu'en une année de conversation. »
        Platon
    """

    def __init__(self, nom, casino):
        self.nom = nom
        if casino.ajouter_jeu(self):
            self.casino = casino
        else:
            self.casino = None

    def jouer(self, joueur):
        pass

    def __str__(self):
        return self.nom