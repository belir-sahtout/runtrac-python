def my_long_word(n, phrase):
    mots = phrase.split()
    mots_filtres = [mot for mot in mots if len(mot) > n]
    resultat = ' '.join(mots_filtres)
    return resultat

resultat = my_long_word(2 , "je suis le meilleur dev web de la décenie")
print(resultat)