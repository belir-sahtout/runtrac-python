def list():
    fruits=["pommes","cerise","orange","melon"]
    fruits.append("mangue")
    fruits[-1],fruits[1]=fruits[1],fruits[-1]
    print(fruits)

list()