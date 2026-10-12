import pygame
import mm
from fonctions import genererSecret, resultat, afficherMessage

NB_PIONS = 5
NB_COUPS_MAX = 15

def main() -> None:
    pygame.init()
    fenetre = pygame.display.set_mode((800, 720))

    rejouer = True
    while rejouer:
        fenetre.fill(mm.Blanc)

        # a. affichage de l'IHM
        mm.afficherPlateau(fenetre)
        mm.afficherChoixCouleur(fenetre)
        pygame.display.update()

        # b.combinaison secrète
        secret = genererSecret()

        #c. boucle de jeu
        gagne = False
        ligne = 1
        while not gagne and ligne <= NB_COUPS_MAX:
            numLigne = ligne + 1   # mm.py afiche la ligne trop haut donc g decaler de 1
            prop = mm.construireProposition(fenetre, numLigne)      # i
            res = resultat(secret, prop)                             # ii
            mm.afficherResultat(fenetre, res, numLigne)              # iii
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

        # affichage des touches
        police = pygame.font.SysFont("monospace", 15)
        fenetre.blit(police.render("Echap : quitter", 1, mm.Noir), (20, 600))
        fenetre.blit(police.render("R : rejouer", 1, mm.Noir), (20, 625))
        pygame.display.update()

        # e attendre : Echap quitte, R rejoue
        rejouer = False
        attente = True
        while attente:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    attente = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        attente = False
                    if event.key == pygame.K_r:
                        rejouer = True
                        attente = False
    pygame.quit()


if __name__ == "__main__":
    main()
