
    def calcule(num1, operator, num2):
    if operator == "+":
        return num1 + num2
    elif operator == "-":
        return num1 - num2
    elif operator == "*":
        return num1 * num2
    elif operator == "/":
        
        if num2 != 0:
            return num1 / num2
        else:
            return "Division par zéro"
    elif operator == "%":
       
        if num2 != 0:
            return num1 % num2
        else:
            return "Division par zéro"
    else:
        return "Opérateur non valide"

