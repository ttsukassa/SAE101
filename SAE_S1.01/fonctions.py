# Fonctions pour calculer le résultat d'une proposition


def nbBienPlaces(secret: list, prop: list) -> int:
    """Compte les pions qui ont la bonne couleur au bon endroit."""
    nb = 0
    for i in range(len(secret)):
        if secret[i] == prop[i]:
            nb = nb + 1
    return nb


def nbCouleursCommunes(secret: list, prop: list) -> int:
    """Compte les pions en commun (on ignore la position).
    Pour chaque couleur du secret, on garde le plus petit nombre
    d'apparitions entre le secret et la proposition."""
    nb = 0
    vues = []
    for c in secret:
        if c not in vues:
            vues.append(c)
            nb = nb + min(secret.count(c), prop.count(c))
    return nb


def nbMalPlaces(secret: list, prop: list) -> int:
    """Pions de la bonne couleur mais pas au bon endroit."""
    return nbCouleursCommunes(secret, prop) - nbBienPlaces(secret, prop)


def resultat(secret: list, prop: list) -> tuple:
    """Retourne (nombre de bien placés, nombre de mal placés)."""
    return (nbBienPlaces(secret, prop), nbMalPlaces(secret, prop))
