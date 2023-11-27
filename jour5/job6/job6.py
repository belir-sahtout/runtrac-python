def phare(nb_marche ,ht_marche):
    ht_phare = nb_marche * ht_marche
    ht_trajet = ht_phare * 2
    ht_jours = ht_trajet * 5
    ht_semaine = ht_jours *7
    print(ht_semaine)  


phare(10, 1) 
phare(50, 0.5)