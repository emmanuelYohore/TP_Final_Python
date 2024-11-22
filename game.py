import random

class Game:
    def __init__(self, grille=None, taille=10):
        self.taille = taille
        if grille :
            self.grille = grille
        else :
            self.grille = self.genererate_grille()
        self.tour = 0
        self.history = []

    def genererate_grille(self):
        return [[random.randint(0, 1) for _ in range(self.taille)] for _ in range(self.taille)]

    def show_grille(self):
        for ligne in self.grille:
            print(' '.join('⬜' if cellule else '⬛' for cellule in ligne))
        print(f"Tour : {self.tour}")
