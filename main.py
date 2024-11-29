from manager import manager

def main():
    try:
        manager()
    except KeyboardInterrupt:
        print("\n⚠️  Interruption détectée. Fermeture du jeu. À bientôt !")

if __name__ == "__main__":
    main()