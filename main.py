import random
import pygame
import mm
from fonctions import resultat

NB_PIONS = 5
NB_COUPS_MAX = 15


def genererSecret() -> list:
    """Combinaison secrète : 5 couleurs tirées au hasard (répétitions possibles)."""
    secret = []
    for _ in range(NB_PIONS):
        secret.append(random.choice(mm.TabCouleur))
    return secret


def afficherMessage(f: pygame.Surface, texte: str) -> None:
    police = pygame.font.SysFont("monospace", 18)
    pygame.draw.rect(f, mm.Blanc, [200, 690, 500, 28])
    f.blit(police.render(texte, 1, mm.Noir), (230, 692))
    pygame.display.update()


def main() -> None:
    pygame.init()
    fenetre = pygame.display.set_mode((800, 720))
    fenetre.fill(mm.Blanc)

    # a. affichage de l'IHM
    mm.afficherPlateau(fenetre)
    mm.afficherChoixCouleur(fenetre)
    pygame.display.update()

    # b. combinaison secrète
    secret = genererSecret()

    # c. boucle de jeu
    gagne = False
    ligne = 1
    while not gagne and ligne <= NB_COUPS_MAX:
        prop = mm.construireProposition(fenetre, ligne)      # i
        res = resultat(secret, prop)                          # ii
        mm.afficherResultat(fenetre, res, ligne)              # iii
        pygame.display.update()
        if res[0] == NB_PIONS:
            gagne = True
        else:
            ligne = ligne + 1

    # d. message final
    mm.afficherSecret(fenetre, secret)
    if gagne:
        if ligne == 1:
            afficherMessage(fenetre, "Vous avez gagné en 1 coup !")
        else:
            afficherMessage(fenetre, "Vous avez gagné en " + str(ligne) + " coups !")
    else:
        afficherMessage(fenetre, "Vous avez perdu !")

    # e. attendre la fermeture de la fenêtre
    attente = True
    while attente:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                attente = False
    pygame.quit()


if __name__ == "__main__":
    main()
