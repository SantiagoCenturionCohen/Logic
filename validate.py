# Reglas de inferencia
def not_left(gamma, delta, formula):
    if formula[0] == "NOT":
        gamma.remove(formula)
        delta.append(formula[1])
    return gamma, delta

def not_right(gamma, delta, formula):
    if formula[0] == "NOT":
        delta.remove(formula)
        gamma.append(formula[1])
    return gamma, delta

def and_left(gamma, delta, formula):
    if formula[0] == "AND":
        gamma.remove(formula)
        gamma.extend([formula[1], formula[2]])
    return gamma, delta

def and_right(gamma, delta, formula):
    if formula[0] == "AND":
        delta.remove(formula)
        delta.extend([formula[1], formula[2]])
    return gamma, delta

def or_left(gamma, delta, formula):
    if formula[0] == "OR":
        new_gamma1 = gamma.copy() + [formula[1]]
        new_gamma2 = gamma.copy() + [formula[2]]
        return [(new_gamma1, delta), (new_gamma2, delta)]
    return [(gamma, delta)]

def or_right(gamma, delta, formula):
    if formula[0] == "OR":
        delta.remove(formula)
        delta.extend([formula[1], formula[2]])
    return [(gamma, delta)]

def implies_left(gamma, delta, formula):
    if formula[0] == "IMPLIES":
        gamma.remove(formula)
        gamma.append(("NOT", formula[1]))
        delta.append(formula[2])
    return gamma, delta

def implies_right(gamma, delta, formula):
    if formula[0] == "IMPLIES":
        delta.remove(formula)
        gamma.append(formula[1])
        delta.append(formula[2])
    return gamma, delta

# Función para verificar la validez del secuente
def check_sequent_validity(gamma, delta):
    for formula in gamma:
        if formula in delta:
            return True

    for formula in gamma:
        if formula[0] == "NOT":
            gamma, delta = not_left(gamma, delta, formula)
            return check_sequent_validity(gamma, delta)

    for formula in delta:
        if formula[0] == "NOT":
            gamma, delta = not_right(gamma, delta, formula)
            return check_sequent_validity(gamma, delta)

    return False

# Función principal para la interacción con el usuario
def main():
    print("Bienvenido al validador de secuentes")
    print("Ingrese las fórmulas en formato de tuplas, como ('NOT', 'p'), ('AND', 'p', 'q')...")

    try:
        # Recibir la parte izquierda (Gamma) del secuente
        gamma = eval(input("Ingrese las fórmulas de la parte izquierda (Gamma), en una lista: "))
        
        # Recibir la parte derecha (Delta) del secuente
        delta = eval(input("Ingrese las fórmulas de la parte derecha (Delta), en una lista: "))

        # Verificar validez del secuente
        if check_sequent_validity(gamma, delta):
            print("El secuente es válido.")
        else:
            print("El secuente no es válido.")

    except Exception as e:
        print(f"Error: {e}")

# Ejecutar el programa
main()
