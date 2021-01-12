from random import randrange

from Jeu import Jeu
from math import ceil

class Roulette(Jeu):
    """
        « La roulette est un cercle vicieux à l'intérieur duquel sont
        aménagés trente-sept alvéoles correspondant en priorité aux numéros
        sur lesquels vous n'avez pas misé. »
        Philippe Bouvard
    """

    def __init__(self, nom, casino):
        super().__init__(nom, casino)

    def __str__(self):
        return self.nom + " : le meilleur jeu de roulette de tous les temps !"

    def jouer(self, joueur):
        # Declaration des variables de depart
        continuer_partie = True  # Booleen qui est vrai tant qu'on peut continuer la partie

        print("Vous vous installez a la table de roulette avec", joueur.argent, "$.")

        while continuer_partie:  # Tant qu'on peut continuer la partie
            # on demande a l'utilisateur de saisir le nombre sur
            # lequel il va miser
            nombre_mise = -1
            while nombre_mise < 0 or nombre_mise > 49:
                nombre_mise = input("Tapez le nombre sur lequel vous voulez miser (entre 0 et 49) : ")
                # On convertit le nombre mise
                try:
                    nombre_mise = int(nombre_mise)
                except ValueError:
                    print("Vous n'avez pas saisi de nombre")
                    nombre_mise = -1
                    continue
                if nombre_mise < 0:
                    print("Ce nombre est negatif")
                elif nombre_mise > 49:
                    print("Ce nombre est superieur a 49")

            # À present, on selectionne la somme a miser sur le nombre
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

            # Le nombre mise et la mise ont ete selectionnes par
            # l'utilisateur, on fait tourner la roulette
            numero_gagnant = randrange(50)
            print("La roulette tourne... ... et s'arrête sur le numero", numero_gagnant)

            # On etablit le gain du joueur
            if numero_gagnant == nombre_mise:
                print("Felicitations ! Vous obtenez", mise * 3, "$ !")
                mise = mise * 3
                joueur.argent += mise
                # Le joueur gagne, le casino perd
                self.casino.modifier_banque(-1 * (mise))
            elif numero_gagnant % 2 == nombre_mise % 2:  # ils sont de la même couleur
                mise = ceil(mise * 0.5)
                print("Vous avez mise sur la bonne couleur. Vous obtenez", mise, "$")
                joueur.argent += mise
                # Le joueur gagne, le casino perd
                self.casino.modifier_banque(-1 * (mise * 3))
            else:
                print("Desole  c'est pas pour cette fois. Vous perdez votre mise.")
                joueur.argent -= mise
                self.casino.modifier_banque(mise)

            # On interrompt la partie si le joueur est ruine
            if joueur.argent <= 0:
                print("Vous êtes ruine ! C'est la fin de la partie.")
                continuer_partie = False
                joueur.sortir_casino()
            else:
                # On affiche l'argent du joueur
                print("Vous avez a present", joueur.argent, "$")
                quitter = input("Souhaitez-vous quitter le casino (o/n) ? ")
                if quitter.lower() == "o":
                    print("Vous quittez le casino avec vos gains.")
                    continuer_partie = False
                    joueur.sortir_casino()
