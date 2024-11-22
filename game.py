import random
from others import detect_cycle
from others import clear_screen

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
    
    def set_symbols_alive(self) -> str:
       color_choice_alive = {
           1 : "⬜" ,
           2: "🟪",
           3: "🟧",
           4: "🟩",
       }
       
       for a, b in color_choice_alive.items:
           print(a,": ",b)
       color = int(input(" Choisissez une couleur en mettant un numéro : ") )  
       return color_choice_alive[color]
           
    def set_symbols_dead(self):
       color_choice_dead = {
           1 : "⬜" ,
           2: "🟪",
           3: "🟧",
           4: "🟩",
       }
           
    
        
        
            

    def show_grille(self, color_alive, color_dead):
        for ligne in self.grille:
            print(' '.join(self.color_alive if cellule else self.color_dead for cellule in ligne))
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
