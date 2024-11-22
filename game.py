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
    
    def next_turn(self):
        nouvelle_grille = [[0] * self.size for _ in range(self.size)]
        for x in range(self.size):
            for y in range(self.size):
                neighbors = self.count_neighbors(x, y)
                if neighbors == 3 or (neighbors == 2 and self.grille[x][y] == 1):
                    nouvelle_grille[x][y] = 1
        self.grille = nouvelle_grille
        self.turn += 1
        self.history.append(self.grille)
