# 🎨 MasterMind – SAÉ S1.01
 
> *Devine la combinaison secrète avant que l'ordinateur ne gagne !* 🕵️‍♀️
 
Un petit jeu de **MasterMind** en Python 🐍 : l'ordinateur cache 5 pions de couleur,
et toi, tu as **15 essais** pour les retrouver.
 
*BUT Informatique – Semestre 1 – IUT de Maubeuge (UPHF)*
*Par : [Nom Prénom 1] & [Nom Prénom 2] 💛*
 
---
 
## 🚀 Lancer le jeu
 
1. Installe pygame :
```bash
   pip install pygame
```
2. Mets tous les fichiers dans le même dossier.
3. Lance :
```bash
   python main.py
```
 
## 🎮 Comment jouer
 
| Action | Ce qu'il faut faire |
|---|---|
| 🎨 Choisir une couleur | Clique sur un pion dans la colonne de gauche |
| ⌫ Retirer le dernier pion | Clique sur le pion marron en bas de la colonne |
| ✅ Valider | Automatique dès que tu as posé 5 pions |
 
Après chaque essai, des petits points apparaissent à droite :
 
- ⚪ **Point blanc** = un pion de la bonne couleur **bien placé**
- ⚫ **Point noir** = un pion de la bonne couleur mais **mal placé**
Tu gagnes quand tu as **5 points blancs** 🎉
Si tu n'as pas trouvé après 15 essais, c'est perdu 😿 (mais la solution est révélée !)
 
Les couleurs du secret peuvent se répéter.
 
## 📁 Les fichiers
 
| Fichier | À quoi il sert |
|---|---|
| `main.py` | 🎯 Le programme principal : plateau, secret, boucle de jeu, message final |
| `mm.py` | 🖼️ La bibliothèque fournie (affichage pygame) + notre fonction `distance` |
| `fonctions.py` | 🧮 Le calcul du résultat : `nbBienPlaces`, `nbCouleursCommunes`, `nbMalPlaces`, `resultat` |
| `tests.py` | 🧪 Les jeux d'essais automatiques (34 tests) |
| `trace_tests.txt` | 📜 Ce que `tests.py` a affiché |
| `Rapport_SAE_S1.01.docx` | 📝 Le rapport |
 
> `demo.py` est un petit outil qui simule une partie sans souris pour faire les captures d'écran du rapport. Il n'est pas nécessaire pour jouer.
 
## 🧪 Lancer les tests
 
```bash
python tests.py
```
 
Tu dois voir `TOTAL ECHECS : 0` à la fin ✨
 
## 🧠 Le petit truc à retenir
 
Pour compter les pions **mal placés**, on calcule :
 
```
mal placés = couleurs en commun − bien placés
```
 
et pour les couleurs en commun, chaque pion du secret ne compte qu'**une seule fois**
(sinon une couleur répétée serait comptée en trop 🙅‍♀️).
 
## 🤖 Un mot sur l'aide reçue
 
Ce projet a été réalisé avec l'aide de **Claude** (IA d'Anthropic).
 
---
 
*Fait avec ☕, 🐍 et beaucoup de petits pions colorés.*
