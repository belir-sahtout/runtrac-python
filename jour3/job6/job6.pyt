def nombre():
   
    nombre = float(input("Veuillez entrer un nombre : "))

    # Vérifier le signe du nombre
    if nombre > 0:
        print("positif")
    elif nombre < 0:
        print("négatif")
    else:
        print("le nombre est nul")

nombre()

    