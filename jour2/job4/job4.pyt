
while True:
    try:
        N = int(input("Veuillez saisir un entier supérieur à zéro (N) : "))
        if N > 0:
            break  
        else:
            print("Veuillez saisir un entier supérieur à zéro.")
    except ValueError:
        print("Veuillez saisir un entier valide.")


for i in range(1, N + 1):
    print(f"\nTable de multiplication de {i} :")
    for j in range(1, 11):
        produit = i * j
        print(f"{i} * {j} = {produit}")
