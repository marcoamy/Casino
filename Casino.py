class Casino():
    """
        Le casino est un endroit magique ou les rêves peuvent devenir réalité...
        Et les pires cauchemars aussi, mouhahaha !
    """

    def __init__(self, banque, jeux=[], joueurs=[]):
        self.banque = banque
        self.jeux = jeux
        self.joueurs = joueurs

    def ajouter_joueur(self, joueur):
        if joueur.argent > 0 and joueur not in self.joueurs:
            self.joueurs.append(joueur)
            print("Bienvenu cher joueur, que la fortune vous soit favorable.")
            return True
        print("Revenez plus tard, pas de gens fauchés ici !")
        return False

    def enlever_joueur(self, joueur):
        for i, j in enumerate(self.joueurs):
            if joueur == j:
                self.joueurs.pop(i)
                if self.banque > 0:
                    print("Au-revoir, un plaisir comme toujours.")
                else:
                    print("On a plus rien, la fete est finie !")
                return True
        return False

    def ajouter_jeu(self, jeu):
        if jeu not in self.jeux:
            self.jeux.append(jeu)
            print("Et encore un jeu pour plumer les pigeons !\nEuh... Amuser les clients.")
            return True
        print("Mais on l'a deja celui-la...")
        return False

    def enlever_jeu(self, jeu):
        for i, j in enumerate(self.jeux):
            if jeu == j:
                self.jeux.pop(i)
                print("C'etait vraiment pas top ce jeu finalement...")
                return True
        return False

    def afficher_jeux(self):
        print("Voici la liste des jeux que vous propose notre etablissement :")
        for i, jeu in enumerate(self.jeux):
            # Appel a la fonction __str__() de la classe Jeu !
            print(i, '-', jeu)

    def modifier_banque(self, montant):
        # Quand le casino perd, le joueur gagne
        if montant < 0:
            if self.banque + montant > 0:
                self.banque -= montant
                return abs(montant)
            # La banqueroute
            else:
                self.banque = 0
                return abs(montant + self.banque)
        # Le casino gagne toujours
        else:
            self.banque += montant
            return self.banque