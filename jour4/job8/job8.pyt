L = [8, 24, 27, 48, 2,16, 9, 7, 84, 91]

somme_des_valeur_pair = 0

for valeur in L:
    if valeur % 2 == 0:
        somme_des_valeur_pair += valeur
        
print("le somme des valeurs pair de la liste sont :" ,somme_des_valeur_pair)