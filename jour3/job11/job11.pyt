def time():
   
    total_minutes = int(input("Veuillez entrer un nombre de minutes : "))

    
    heures = total_minutes // 60
    minutes = total_minutes % 60

    
    result = f"{heures} heures et {minutes} minutes"

    
    print(result)


time()
