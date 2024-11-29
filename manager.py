from backup import save_game, load_game
from others import clear_screen
from game import Game

def manager():
    clear_screen()
    print("Bienvenue dans le Jeu de la Vie !\n")
    while True:
        try:
            choice = input("1. Nouvelle grille\n2. Charger une grille existante\nVotre choix : ").strip()
            if choice not in {'1', '2'}:
                clear_screen()
                raise ValueError(" Les options sont 1 pour une nouvelle partie et 2 pour charger la précédente grille.\n\033[32mVeuillez réessayer\033[0m\n")
            break
        except ValueError as e:
            print(f"\033[91m⚠️  Erreur :\033[0m {e}")
    clear_screen()
    grille, turn = None, 0
    color_alive, color_dead = None, None

    if choice == '2':  
        grille, turn, color_alive, color_dead, is_in_cycle, n = load_game()
        if grille is None:
            print("⚠️  Aucune grille détecté. Création d'une nouvelle partie.")
            choice = '1'
        else:
            if is_in_cycle:
                while True:
                    try:
                        print("⚠️  La partie chargée était en boucle.\n")
                        confirm = input("1. Charger la grille\n0. Reprendre une nouvelle grille\nVotre choix : ").strip()
                        if confirm not in {'0', '1'}:
                            raise ValueError("Veuillez entrer 1 pour charger la grille ou 0 pour reprendre une nouvelle grille.")
                        if confirm == '0':
                            print("\n\n⚠️  Chargement annulé. Création d'une nouvelle grille.")
                            choice = '1'
                        else:
                            print("Grille chargée avec succès.")
                        break
                    except ValueError as e:
                        clear_screen()
                        print(f"\033[91m⚠️  Erreur :\033[0m {e}")

    if choice == '1':  
        while True:
            try:
                print("taille max = 50       /      taille min = 5")
                n = int(input("\nEntrez la taille de la grille (n x n) : "))
                if n <= 4 or n > 50:
                    raise ValueError()
                break
            except ValueError:
                clear_screen()
                print(f"\033[91m⚠️  Erreur :\033[0m Veuillez entrer un nombre entier positif. la taille minimale est de 5 et la taille maximale est de 50\n")
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
        action = input("\nAPPUYEZ SUR :\n👉  Entrée pour le prochain tour\n👉  q pour sauvegarder et quitter\n👉  Ctrl + c pour interrompre la partie et quitter\nVotre choix  : ").strip().lower()
        if action == 'q':
            is_in_cycle = jeu.next_turn()
            if is_in_cycle:
                while True:
                    try:
                        print("⚠️  Une boucle est détectée dans la partie.\n")
                        confirm = input("1. Sauvegarder quand même\n0. Annuler la sauvegarde\nVotre choix : ").strip()
                        if confirm not in {'0', '1'}:
                            raise ValueError(" Veuillez entrer 1 pour sauvegarder ou 0 pour annuler.")
                        if confirm == '0':
                            print("Sauvegarde annulée. Continuons le jeu.")
                            break
                        else:
                            save_game(jeu.grille, jeu.turn, color_alive, color_dead, is_in_cycle)
                            print("À bientôt!")
                            return
                    except ValueError as e:
                        clear_screen()
                        print(f"\033[91m⚠️  Erreur :\033[0m {e}")
            else:
                save_game(jeu.grille, jeu.turn, color_alive, color_dead, is_in_cycle)
                print("À bientôt!")
                return
        jeu.next_turn()