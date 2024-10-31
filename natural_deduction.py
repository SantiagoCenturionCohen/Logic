# deduccion_natural.py

# Introducción de conjunción: Si tienes A y B, puedes deducir A ∧ B
def intro_conjunction(a, b):
    return ("AND", a, b)

# Eliminación de conjunción izquierda: Si tienes A ∧ B, puedes deducir A
def elim_conjunction_left(formula):
    if formula[0] == "AND":
        return formula[1]
    raise ValueError("La fórmula no es una conjunción")

# Eliminación de conjunción derecha: Si tienes A ∧ B, puedes deducir B
def elim_conjunction_right(formula):
    if formula[0] == "AND":
        return formula[2]
    raise ValueError("La fórmula no es una conjunción")

# Introducción de disyunción: Si tienes A, puedes deducir A ∨ B
def intro_disjunction_left(a, b):
    return ("OR", a, b)

# Eliminación de disyunción: Si tienes A ∨ B y ambos llevan a C, puedes deducir C
def elim_disjunction(formula, proof_a, proof_b):
    if formula[0] == "OR":
        if proof_a == proof_b:
            return proof_a
        raise ValueError("Las deducciones no son consistentes")
    raise ValueError("La fórmula no es una disyunción")

# Introducción de implicación: Si A lleva a B, puedes deducir A → B
def intro_implication(a, b):
    return ("IMPLIES", a, b)

# Eliminación de implicación (Modus Ponens): Si tienes A → B y A, puedes deducir B
def elim_implication(implication, a):
    if implication[0] == "IMPLIES" and implication[1] == a:
        return implication[2]
    raise ValueError("La implicación no aplica o no coincide con la premisa")

# Función para manejar la entrada del usuario
def main():
    print("Bienvenido a la herramienta de deducción natural")
    print("Operaciones disponibles:")
    print("1. Introducción de conjunción (A ∧ B)")
    print("2. Eliminación de conjunción izquierda (de A ∧ B deducir A)")
    print("3. Eliminación de conjunción derecha (de A ∧ B deducir B)")
    print("4. Introducción de disyunción (A ∨ B)")
    print("5. Eliminación de disyunción")
    print("6. Introducción de implicación (A → B)")
    print("7. Eliminación de implicación (Modus Ponens)")

    try:
        # Solicitar al usuario la operación a realizar
        choice = int(input("Elija una operación (1-7): "))
        
        if choice == 1:
            a = input("Ingrese la primera premisa (A): ")
            b = input("Ingrese la segunda premisa (B): ")
            result = intro_conjunction(a, b)
            print(f"Resultado: {result}")
        
        elif choice == 2:
            formula = eval(input("Ingrese la fórmula (A ∧ B): "))
            result = elim_conjunction_left(formula)
            print(f"Resultado: {result}")
        
        elif choice == 3:
            formula = eval(input("Ingrese la fórmula (A ∧ B): "))
            result = elim_conjunction_right(formula)
            print(f"Resultado: {result}")
        
        elif choice == 4:
            a = input("Ingrese la primera premisa (A): ")
            b = input("Ingrese la segunda premisa (B): ")
            result = intro_disjunction_left(a, b)
            print(f"Resultado: {result}")
        
        elif choice == 5:
            formula = eval(input("Ingrese la fórmula (A ∨ B): "))
            proof_a = input("Ingrese la deducción de la primera opción: ")
            proof_b = input("Ingrese la deducción de la segunda opción: ")
            result = elim_disjunction(formula, proof_a, proof_b)
            print(f"Resultado: {result}")
        
        elif choice == 6:
            a = input("Ingrese la primera premisa (A): ")
            b = input("Ingrese la segunda premisa (B): ")
            result = intro_implication(a, b)
            print(f"Resultado: {result}")
        
        elif choice == 7:
            implication = eval(input("Ingrese la implicación (A → B): "))
            a = input("Ingrese la premisa A: ")
            result = elim_implication(implication, a)
            print(f"Resultado: {result}")
        
        else:
            print("Opción no válida.")
    
    except ValueError as e:
        print(f"Error: {e}")

# Ejecutar el programa
main()
