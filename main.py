from backup import save_game, load_game
from others import clear_screen
from game import Game

def main():
    clear_screen()
    print("Bienvenue dans le Jeu de la Vie de Conway!")

    while True:
        try:
            choice = input("1. Nouvelle grille\n2. Charger une grille existante\nVotre choix : ").strip()
            if choice not in {'1', '2'}:
                clear_screen()
                raise ValueError("Les options sont 1 pour une nouvelle partie et 2 pour charger la précédente grille.\n\033[32mVeuillez réessayer\033[0m")
            break
        except ValueError as e:
            print(f"\033[91mErreur :\033[0m {e}")
    
    clear_screen()
    grille, turn = None, 0
    color_alive, color_dead = None, None

    if choice == '2':  
        grille, turn, color_alive, color_dead = load_game()
        if grille is None:
            print("Impossible de charger la grille. Création d'une nouvelle partie.")
            choice = '1'
        else:
            n = len(grille)
            print("Grille chargée avec succès.")

    if choice == '1':  
        while True:
            try:
                print("taille max = 50       /      taille min = 5")
                n = int(input("Entrez la taille de la grille (n x n) : "))
                if n <= 4 or n > 60 :
                    raise ValueError()
                break
            except ValueError:
                clear_screen()
                print(f"\033[91mErreur :\033[0m Veuillez entrer un nombre entier positif. la limite est de 60")

        jeu = Game(None, n)
        clear_screen()
        color_alive = jeu.set_symbols_alive()
        clear_screen()
        color_dead = jeu.set_symbols_dead()
        clear_screen()
    else:
        jeu = Game(grille, n)
    
    jeu.turn = turn

    while True:
        print(f'Vivantes : {color_alive}   Mortes : {color_dead} \n')
        jeu.show_grille(color_alive, color_dead)
        action = input("Appuyez sur Entrée pour le prochain tour, ou 'Q' pour quitter : ").strip().lower()

        if action == 'q':
            save_game(jeu.grille, jeu.turn, color_alive, color_dead)
            print("Partie sauvegardée. À bientôt!")
            break

        jeu.next_turn()

if __name__ == "__main__":
    main()
