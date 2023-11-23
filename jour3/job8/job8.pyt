def produit(type, saison):
    if type == "fruit":
        if saison == "hiver":
             print("orange,mandarine,kiwi")
        elif saison == "été":
            print("poire,fraise,kiwi")
        else:
            print("pas de produit pour cette saison")
    if type == "legume":
        if saison == "été":
            print("carotte,topnambour,endive")
        elif saison == "hiver":
            print("artichaut,aubergine,endive")
        else:
            print("pas de produit pour cette saison")


type_input = input ("entrez un type de produit (fruit/legume) : ")
saison_input = input ("entrez une saison : ")

produit(type_input, saison_input)





        

    
    
