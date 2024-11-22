import random
from others import detect_cycle
from others import clear_screen

class Game:
    def __init__(self, grille=None, size=10):
        self.size = size
        if grille:
            self.grille = grille
        else:
            self.grille = self.genererate_grille()
        self.turn = 0
        self.history = []

    def genererate_grille(self):
        return [[random.randint(0, 1) for _ in range(self.size)] for _ in range(self.size)]
    
    def set_symbols_alive(self):
        color_choice_alive = {
            1: "⬜",
            2: "🟨",
            3: "😊",
            4: "⭐",
        }
        while True:
            print("Cellules vivantes :\n")
            try:
                for a, b in color_choice_alive.items():
                    print(a, ": ", b)
                color = int(input("\nChoisissez votre cellule vivante en mettant son numéro : "))
                if color not in color_choice_alive:
                    clear_screen()
                    raise ValueError()
                return color_choice_alive[color]
            except ValueError as e:
                clear_screen()
                print(f"\033[91mErreur :\033[0m Numéro invalide. Veuillez choisir un numéro dans la liste.")
           
    def set_symbols_dead(self):
        color_choice_dead = {
            1: "⬛",
            2: "🟦",
            3: "💀",
            4: "❌",
        }
        while True:
            print("Cellules mortes :\n")
            try:
                for a, b in color_choice_dead.items():
                    print(a, ": ", b)
                color = int(input("\nChoisissez votre cellule morte en mettant son numéro : "))
                if color not in color_choice_dead:
                    raise ValueError()
                return color_choice_dead[color]
            except ValueError as e:
                clear_screen()
                print(f"\033[91mErreur :\033[0m Numéro invalide. Veuillez choisir un numéro dans la liste.")
    
    def show_grille(self, color_alive, color_dead):
        for ligne in self.grille:
            print(' '.join(color_alive if cellule else color_dead for cellule in ligne))
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
        clear_screen()
        detect_cycle(self.history, self.turn)