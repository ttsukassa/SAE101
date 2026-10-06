"""Jeux d'essais des fonctions du calcul du résultat (et de distance)."""
import sys
import mm
from fonctions import nbBienPlaces, nbCouleursCommunes, nbMalPlaces, resultat

N, B, G, BL, R, V, O, P = (mm.Noir, mm.Blanc, mm.Gris, mm.Bleu,
                           mm.Rouge, mm.Vert, mm.Orange, mm.Rose)
NOM = {N: "Noir", B: "Blanc", G: "Gris", BL: "Bleu", R: "Rouge", V: "Vert", O: "Orange", P: "Rose"}
def s(l): return "[" + ",".join(NOM[c] for c in l) + "]"

echecs = 0
def verif(fonction, nom, args, attendu, affichage, justification):
    global echecs
    obtenu = fonction(*args)
    ok = (obtenu == attendu) or (isinstance(attendu, float) and abs(obtenu - attendu) < 1e-9)
    if not ok: echecs += 1
    print(f"{nom:<14} | {affichage:<55} | attendu={attendu!s:<8} | obtenu={obtenu!s:<8} | {'OK' if ok else 'ECHEC'}  # {justification}")

print("=== distance ===")
D = [
 ([0,0],[3,4],5.0,"triplet pythagoricien 3-4-5"),
 ([5,5],[5,5],0.0,"points identiques"),
 ([0,0],[7,0],7.0,"même ordonnée"),
 ([2,9],[2,3],6.0,"même abscisse"),
 ([3,4],[0,0],5.0,"symétrie d(a,b)=d(b,a)"),
 ([-1,-1],[2,3],5.0,"coordonnées négatives"),
 ([75,80],[78,84],5.0,"cas réel : clic à 5 px d'un bouton"),
 ([0,0],[1,1],2**0.5,"résultat irrationnel"),
]
for a,b,att,j in D:
    verif(mm.distance,"distance",(a,b),att,f"a={a}, b={b}",j)

print("\n=== nbBienPlaces ===")
S1=[R,V,BL,O,P]
BP = [
 (S1,[R,V,BL,O,P],5,"identique"),
 (S1,[N,B,G,N,B],0,"aucune couleur commune"),
 (S1,[V,R,O,BL,P],1,"seul le dernier est bien placé"),
 (S1,[R,N,BL,N,P],3,"cas mixte, 3 bien placés"),
 ([R,R,R,R,R],[R,V,R,V,R],3,"secret monochrome"),
 ([R,V,BL,O,P],[P,O,BL,V,R],1,"inversion : seul le centre reste"),
]
for sec,prop,att,j in BP:
    verif(nbBienPlaces,"nbBienPlaces",(sec,prop),att,f"S={s(sec)} P={s(prop)}",j)

print("\n=== nbCouleursCommunes ===")
CC = [
 (S1,[R,V,BL,O,P],5,"identique"),
 (S1,[N,B,G,N,B],0,"aucune couleur commune"),
 (S1,[V,R,P,BL,O],5,"permutation : toutes les couleurs sont communes"),
 ([R,R,B,G,N],[N,N,N,R,R],3,"N répété 3 fois dans la proposition, 1 seul dans le secret"),
 (S1,[R,R,R,R,R],1,"une couleur répétée : comptée une seule fois"),
 ([R,R,R,V,V],[V,V,V,R,R],4,"doublons des deux côtés : min(2,3)+min(3,2)"),
]
for sec,prop,att,j in CC:
    verif(nbCouleursCommunes,"nbCouleursCom.",(sec,prop),att,f"S={s(sec)} P={s(prop)}",j)

print("\n=== nbMalPlaces ===")
MP = [
 (S1,[R,V,BL,O,P],0,"identique : aucun mal placé"),
 (S1,[N,B,G,N,B],0,"aucune couleur commune"),
 (S1,[V,R,O,BL,P],4,"4 bonnes couleurs décalées + 1 bien placé"),
 (S1,[V,R,P,BL,O],5,"toutes les couleurs, aucune bien placée"),
 ([R,R,B,G,N],[B,B,B,B,R],1,"doublons : B bien placé (non recompté), seul R est mal placé"),
 ([R,R,B,G,N],[N,N,N,R,R],3,"3 N dans la proposition, 1 seul dans le secret : N compté une fois"),
 ([R,R,R,V,V],[V,V,V,R,R],4,"doublons : 3 V dans prop mais 2 dans secret"),
 ([R,V,BL,O,P],[R,R,R,R,R],0,"une couleur répétée : un seul R compte (bien placé)"),
]
for sec,prop,att,j in MP:
    verif(nbMalPlaces,"nbMalPlaces",(sec,prop),att,f"S={s(sec)} P={s(prop)}",j)

print("\n=== resultat (tuple bien placés, mal placés) ===")
RS = [
 (S1,[R,V,BL,O,P],(5,0),"victoire"),
 (S1,[N,B,G,N,B],(0,0),"rien en commun"),
 (S1,[V,R,P,BL,O],(0,5),"que des mal placés"),
 ([R,R,B,G,N],[R,B,R,N,G],(1,4),"cas mixte avec doublons"),
 ([R,R,B,G,N],[B,B,B,B,R],(1,1),"doublons dans la proposition"),
 ([V,V,V,V,V],[V,R,R,R,R],(1,0),"secret monochrome"),
]
for sec,prop,att,j in RS:
    verif(resultat,"resultat",(sec,prop),att,f"S={s(sec)} P={s(prop)}",j)

print("\nSecret non modifié :", end=" ")
sec=[R,R,B,G,N]; copie=list(sec); resultat(sec,[B,B,B,B,R])
print("OK" if sec==copie else "ECHEC")
print("\nTOTAL ECHECS :", echecs)
sys.exit(1 if echecs else 0)
