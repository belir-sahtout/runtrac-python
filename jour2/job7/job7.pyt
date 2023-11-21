chaine = "abcdefghijklmnopqrstuvwxyz" * 1

longueur_chaine = len(chaine)
niveau_max = int((longueur_chaine + 1) / 2)

for niveau in range(1, niveau_max + 1):
    espace = " " * (niveau_max - niveau)
    caracteres = chaine[:2 * niveau - 1]
    ligne = espace + caracteres + espace
    print(ligne)
