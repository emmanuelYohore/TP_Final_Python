import random

class Game:
    def __init__(self, grille=None, size=10):
        self.size = size
        if grille :
            self.grille = grille
        else :
            self.grille = self.genererate_grille()
        self.turn = 0
        self.history = []

    def genererate_grille(self):
        return [[random.randint(0, 1) for _ in range(self.size)] for _ in range(self.size)]

    def show_grille(self):
        for ligne in self.grille:
            print(' '.join('⬜' if cellule else '⬛' for cellule in ligne))
        print(f"Tour : {self.turn}")

    def count_neighbors(self, x, y):
        neighbors = 0
        for dx, dy in [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]:
            nx, ny = (x + dx) % self.size, (y + dy) % self.size
            neighbors += self.grille[nx][ny]
        return neighbors
