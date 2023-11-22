def determine_developpeur(langage):
    
    if langage == "JavaScript":
        print("Tu es un développeur web")
    elif langage == "python":
        print("Tu es un développeur IA")
    elif langage == "java":
        print("Tu es un développeur logiciel")
    elif langage == "reactjs":
        print("tu es developpeur mobile")
    else:
        print("un jour tu sera le meilleur developpeur")

langage = input("quel type de dev etes vous , JavaScript , python , java , reactjs : ")
result=determine_developpeur(langage)
print(result)
