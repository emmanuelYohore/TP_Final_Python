from game import Game
from game import set_symbols_alive
from game import set_symbols_dead
from others import clear_screen

def main():
    clear_screen()
    while True:
        try:
            print("Bienvenue dans le Jeu de la Vie de Conway!")
            choice = input("1. Nouvelle grille\n2. Charger une grille existante\nVotre choix : ").strip()
            if choice != '1' and choice != '2' :
                raise ValueError("Les options sont 1 pour une nouvelle partie et 2 pour charger la précédente grille.")
            break
        except ValueError as e:
            print(f"\033[91mErreur :\033[0m {e} Veuillez entrer une option correcte.")
    clear_screen()
    grille, turn = None, 0

    if choice == '1':  
        while True:
            try:
                n = int(input("Entrez la taille de la grille (n x n) : "))
                if n <= 0:
                    raise ValueError("La taille de la grille doit être un nombre entier positif.")
                break
            except ValueError as e:
                print(f"\033[91mErreur :\033[0m {e}. Veuillez entrer un nombre entier positif.")
        
    clear_screen()
    color_alive = set_symbols_alive()
    color_dead = set_symbols_dead()
    jeu = Game(grille, n)
    jeu.turn = turn
    while True:
        jeu.show_grille(color_alive, color_dead)
        action = input("Appuyez sur Entrée pour le prochain tour, ou 'Q' pour quitter : ").strip().lower()
        
        
        
        jeu.next_turn()

if __name__ == "__main__":
    main()
