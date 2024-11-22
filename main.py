from game import Game
from others import clear_screen

def main():
    clear_screen()
    print("Bienvenue dans le Jeu de la Vie de Conway!")
    while True:
        try:
            choice = input("1. Nouvelle grille\n2. Charger une grille existante\nVotre choix : ").strip()
            if choice not in {'1', '2'}:
                clear_screen()
                raise ValueError("Les options sont 1 pour une nouvelle partie et 2 pour charger la précédente grille.\n\033[32mveuillez réessayer\033[0m")
            break
        except ValueError as e:
            print(f"\033[91mErreur :\033[0m {e}")
    
    clear_screen()
    grille, turn = None, 0

    if choice == '1':  
        while True:
            try:
                n = int(input("Entrez la taille de la grille (n x n) : "))
                if n <= 0:
                    raise ValueError()
                break
            except ValueError as e:
                print(f"\033[91mErreur :\033[0m Veuillez entrer un nombre entier positif.")
       
    jeu = Game(grille, n)
    clear_screen()
    color_alive = jeu.set_symbols_alive()
    clear_screen()
    color_dead = jeu.set_symbols_dead()
    clear_screen()

    while True:
        print(f'vivantes : {color_alive}   mortes : {color_dead} \n')
        jeu.show_grille(color_alive, color_dead)
        action = input("Appuyez sur Entrée pour le prochain tour, ou 'Q' pour quitter : ").strip().lower()
        if action == 'q':
            break
        jeu.next_turn()

if __name__ == "__main__":
    main()
