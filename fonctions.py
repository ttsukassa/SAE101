import mm 
import random
import pygame

NB_PIONS = 5

def genererSecret() -> list:
    #Combinaison secrète :5 couleurs tirer au hasard (répétitions possibles).
    secret = []
    for _ in range(NB_PIONS):
        secret.append(random.choice(mm.TabCouleur))
    return secret


def afficherMessage(f: pygame.Surface, texte: str) -> None:
    police = pygame.font.SysFont("monospace", 18)
    pygame.draw.rect(f, mm.Blanc, [200, 690, 500, 28])
    f.blit(police.render(texte, 1, mm.Noir), (230, 692))
    pygame.display.update()


#Fonctions pour calculer le résultat d'une proposition

def nbBienPlaces(secret: list, prop: list) -> int:
    #Compte les pions qui ont la bonne couleur au bon endroit.
    nb = 0
    for i in range(len(secret)):
        if secret[i] == prop[i]:
            nb = nb + 1
    return nb


def nbCouleursCommunes(secret: list, prop: list) -> int:
    # Compte les pions en commun (on ignore la position).
    # Pour chaque couleur du secret, on garde le plus petit nombre
    # d'apparitions entre le secret et la proposition.
    nb = 0
    vues = []
    for c in secret:
        if c not in vues:
            vues.append(c)
            nb = nb + min(secret.count(c), prop.count(c))
    return nb


def nbMalPlaces(secret: list, prop: list) -> int:
    #Pions de la bonne couleur mais pas au bon endroit.
    return nbCouleursCommunes(secret, prop) - nbBienPlaces(secret, prop)


def resultat(secret: list, prop: list) -> tuple:
    # Retourneum tuple avc (nombre de bien places, nombre de mal placés).
    return (nbBienPlaces(secret, prop), nbMalPlaces(secret, prop))
