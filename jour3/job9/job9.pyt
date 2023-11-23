def moyenne(note1, note2, note3):
    moyenne_resultat = (note1 + note2 + note3) /3
    return moyenne_resultat

note1 = float(input("entrez la premier note: "))
note2 = float(input("entrez la deuxième note: "))
note3 = float(input("entrez la troisième note: "))

moyenne_etudiant = moyenne(note1, note2, note3)

print("la moyenne des note est :", moyenne_etudiant)

if 15 <= moyenne_etudiant <=20:
    print("très bon élève")
elif 11 <= moyenne_etudiant <=14:
    print("bon élève")
elif 8 <= moyenne_etudiant <=10:
    print("élève moyen")
elif 0 <= moyenne_etudiant <=7:
    print("élève devant faire des defforts")
else:
    print("la moyenne ne peut pas étre calculé")
    
