import os

SAVE_PATH = "saves/save_game.txt"

def save_game(grille, tour, color_alive, color_dead, is_in_cycle):
    os.makedirs(os.path.dirname(SAVE_PATH), exist_ok=True)
    try:
        with open(SAVE_PATH, "w") as fichier:
            fichier.write(f"{tour}\n")
            fichier.write(f"{color_alive}\n")
            fichier.write(f"{color_dead}\n")
            fichier.write(f"{int(is_in_cycle)}\n")
            for ligne in grille:
                fichier.write("".join(str(cell) for cell in ligne) + "\n")
        print("Partie sauvegardée avec succès.")
    except Exception as e:
        print(f"Erreur lors de la sauvegarde : {e}")


def load_game():
    if not os.path.exists(SAVE_PATH):
        print("Aucune sauvegarde trouvée.")
        return None, 0, None, None, False
    try:
        with open(SAVE_PATH, "r") as fichier:
            lignes = fichier.readlines()
            tour = int(lignes[0].strip())
            color_alive = lignes[1].strip()
            color_dead = lignes[2].strip()
            is_in_cycle = bool(int(lignes[3].strip()))
            grille = [list(map(int, ligne.strip())) for ligne in lignes[4:]]
            n = len(grille)
        return grille, tour, color_alive, color_dead, is_in_cycle, n
    except Exception as e:
        print(f"Erreur lors du chargement de la sauvegarde : {e}")
        return None, 0, None, None, False, 0
