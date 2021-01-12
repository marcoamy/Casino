from random import randrange

from Jeu import Jeu


class MachineASous(Jeu):
    """
        « Les dictateurs et les bandits manchots exercent un pouvoir totalitaire.
        En Asie, Pol Pot assassinait le peuple.
        Chez nous, Jack Pot le rançonne. »
        Philippe Bouvard
    """

    def __init__(self, nom, casino):
        super().__init__(nom, casino)

    def __str__(self):
        return self.nom + " : la meilleure de toutes les machines a sous !"

    def jouer(self, joueur):
        # Declaration des variables de depart
        continuer_partie = True  # Booleen qui est vrai tant qu'on peut continuer la partie

        print("Vous vous installez a la machine a sous avec", joueur.argent, "$.")

        while continuer_partie:  # Tant qu'on peut continuer la partie
            # on demande a l'utilisateur de saisir la somme a miser
            mise = 0
            while mise <= 0 or mise > joueur.argent:
                mise = input("Tapez le montant de votre mise : ")
                # On convertit la mise
                try:
                    mise = int(mise)
                except ValueError:
                    print("Vous n'avez pas saisi de nombre")
                    mise = -1
                    continue
                if mise <= 0:
                    print("La mise saisie est negative ou nulle.")
                if mise > joueur.argent:
                    print("Vous ne pouvez miser autant, vous n'avez que", joueur.argent, "$")

            # Tirage aleatoire
            # Initialisation : liste cntenant le resultat
            # 3 listes (lignes) contenant chacune 3 chiffres
            res = []
            # Generation du tableau des valeurs aleatoires :
            res = []
            n = 3
            for i in range(n):
                ligne = []
                for j in range(n):
                    ligne.append(randrange(4))
                res.append(ligne)
                print(ligne)
            mul_gain = 0
            for i in range(n):
                if res[i][0] == res[i][1] == res[i][2]:
                    # Le multiplicateur de gain augmente pour chaque test valide
                    mul_gain += 1
            # Test sur les diagonales
            if res[0][0] == res[1][1] == res[2][2]:
                mul_gain += 1
            if res[0][2] == res[1][1] == res[2][0]:
                mul_gain += 1

            if mul_gain == 0:
                joueur.argent -= mise
                # le casino gagne
                self.casino.modifier_banque(mise)
            else:
                joueur.argent += mise * mul_gain
                self.casino.modifier_banque(-1 * (mise * mul_gain))

            # On interrompt la partie si le joueur est ruine
            if joueur.argent <= 0:
                print("Vous êtes ruine ! C'est la fin de la partie.")
                continuer_partie = False
            else:
                # On affiche l'argent du joueur
                print("Vous avez a present", joueur.argent, "$")
                quitter = input("Souhaitez-vous quitter le casino (o/n) ? ")
                if quitter.lower() == "o":
                    print("Vous quittez le casino avec vos gains.")
                    continuer_partie = False
                    joueur.sortir_casino()