alpha = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

def cryptage(lett, alpha, clef):
    if lett == " ":
        return " "
    else:
        index_lettre = alpha.index(lett)
        index_crypte = (index_lettre + clef) % 26  # Gérer le dépassement en utilisant le modulo
        return alpha[index_crypte]

mess = input("entrez votre message : ")
clef = int(input("entrez votre clef : "))

mess_cryp = ""

for lett in mess:
    mess_cryp += cryptage(lett, alpha, clef)

print(mess_cryp)

