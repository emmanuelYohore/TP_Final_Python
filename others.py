import os

def detect_cycle(history, tour_actuel):
    for i, grille_precedente in enumerate(history[:-1]):
        if grille_precedente == history[-1]:
            print(f"Cycle détecté! Début : Tour {i}, Cycle actuel : {tour_actuel - i} tours.")
            return True
    return False

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

