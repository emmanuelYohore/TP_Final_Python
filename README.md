# 🧬 Jeu de la Vie - Game of Life

Bienvenue dans Le Jeu de la Vie, une simulation basée sur les célèbres règles de Conway. Ce projet, écrit en Python, permet de créer, sauvegarder, charger et explorer l'évolution de grilles.

---

## 📋 Sommaire
- [Description](#-description)
- [Fonctionnalités](#-fonctionnalités)
- [Installation](#-installation)
- [Utilisation](#-utilisation)
- [Règles du Jeu](#-règles-du-jeu)
- [Exemple de Sauvegarde](#-exemple-de-sauvegarde)
- [Auteurs](#-auteurs)

---

## 📝 Description

Le Jeu de la Vie est une simulation où des cellules "vivantes" et "mortes" évoluent selon des règles prédéfinies à chaque tour. Ce projet offre :
- Une interface interactive.
- Une personnalisation des symboles pour les cellules vivantes et mortes.
- La détection et la gestion des cycles dans les grilles.
- La sauvegarde et le chargement de parties.

---

## ✨ Fonctionnalités

- Créez une nouvelle grille avec une taille personnalisée (de 5x5 à 50x50).
- Personnalisez les symboles des cellules vivantes et mortes.
- Chargez une grille sauvegardée ou reprenez une nouvelle partie.
- Détection de cycles pour identifier les boucles infinies.
- Sauvegardez et rechargez votre partie en toute simplicité.

---

## 💻 Installation

1. Clonez ce dépôt :
   ```bash
   git clone https://github.com/emmanuelYohore/TP_Final_Python.git
   cd TP_Final_Python

---

## 🚀 Utilisation

1. Lancer le jeu :
   ```bash
   python main.py

2. Suivez les instructions affichées pour :
   - Créer une nouvelle grille.
   - Choisir vos cellules(mortes/vivantes)
   - Charger une sauvegarde existante.
   - Explorer les cycles et sauvegarder vos parties.

---

## ⚙️ Règles du Jeu

Les cellules suivent les règles de Conway :

1.  Survie :
        Une cellule vivante reste vivante si elle a 2 ou 3 voisins vivants.
2.  Naissance :
        Une cellule morte devient vivante si elle a exactement 3 voisins vivants.
3.   Mort :
        Une cellule vivante meurt si elle a moins de 2 voisins (solitude) ou plus de 3 voisins (surpopulation).

---

## 🧩 Exemple de Sauvegarde

Voici à quoi ressemble un fichier de sauvegarde (saves/save_game.txt) :

                    3
                    ⬜
                    ⬛
                    0
                    000000
                    001110
                    000000
                    000000

- 3 : Tour actuel.
- ⬜ : Symbole des cellules vivantes.
- ⬛ : Symbole des cellules mortes.
- 0 : Indicateur de cycle détecté (1 si un cycle est détecté).
- Grille : Matrice représentant l’état actuel du jeu.

---

## 🤝 Auteurs

  # Godwin OBLASSE
  # Emmanuel YOHORE


MERCI ! 😊 