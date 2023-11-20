nom_produit = "fraise"
prix = 2
quantité = 50

print(f"Informations produit :")
print(f" {nom_produit}")
print(f" {quantité}")
print(f" {prix}")

quantité_achetée = int(input("Combien de fraise souhaitez vous acheté"))

quantité -= quantité_achetée

prix *= 1.1 

print("\nInformations mises à jour du produit :")
print(f"Nom : {nom_produit}")
print(f"Prix unitaire (après inflation) : {prix:.2f} €")
print(f"Quantité en stock après achat : {quantité} unités")