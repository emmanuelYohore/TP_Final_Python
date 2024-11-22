from game import Game
from backup import save_game, load_game
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
    if choice == '2':  
        grille, turn = load_game()
        if grille is None:
            print("Impossible de charger la grille. Création d'une nouvelle partie.")
            choice = '1'  
        else:
            n = len(grille) 
            print("Grille chargée avec succès.")

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
    jeu = Game(grille, n)
    jeu.turn = turn
    while True:
        jeu.show_grille()
        action = input("Appuyez sur Entrée pour le prochain tour, ou 'Q' pour quitter : ").strip().lower()
        
        if action == 'q':
            save_game(jeu.grille, jeu.turn)
            print("Partie sauvegardée. À bientôt!")
            break
        
        jeu.next_turn()

if __name__ == "__main__":
    main()
