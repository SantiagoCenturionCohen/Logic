

# Introducción de conjunción: Si tengo A y B, puedo deducir A ∧ B
def intro_conjunction(a, b):
    return ("AND", a, b)

# Eliminación de conjunción izquierda: Si tengo A ∧ B, puedo deducir A
def elim_conjunction_left(formula):
    if formula[0] == "AND":
        return formula[1]
    raise ValueError("La fórmula no es una conjunción")

# Eliminación de conjunción derecha: Si tengo A ∧ B, puedo deducir B
def elim_conjunction_right(formula):
    if formula[0] == "AND":
        return formula[2]
    raise ValueError("La fórmula no es una conjunción")

# Introducción de disyunción: Si tengo A, puedo deducir A ∨ B
def intro_disjunction_left(a, b):
    return ("OR", a, b)

# Eliminación de disyunción: Si tengo A ∨ B y ambos llevan a C, puedo deducir C
def elim_disjunction(formula, proof_a, proof_b):
    if formula[0] == "OR":
        if proof_a == proof_b:
            return proof_a
        raise ValueError("Las deducciones no son consistentes")
    raise ValueError("La fórmula no es una disyunción")

# Introducción de implicación: Si A lleva a B, puedo deducir A → B
def intro_implication(a, b):
    return ("IMPLIES", a, b)

# Eliminación de implicación (Modus Ponens): Si tengo A → B y A, puedo deducir B
def elim_implication(implication, a):
    if implication[0] == "IMPLIES" and implication[1] == a:
        return implication[2]
    raise ValueError("La implicación no aplica o no coincide con la premisa")


# Modus Tollens: Si tengo A -> B y NOT B, puedo deducir NOT A
def modus_tollens(implication, not_b):
    # Verificar que la fórmula es una implicación y que tenemos NOT B
    if implication[0] == "IMPLIES" and not_b == ("NOT", implication[2]):
        # Retornar NOT A
        return ("NOT", implication[1])
    raise ValueError("La implicación no aplica o no coincide con la premisa")

# Introducción a Bottom: Si tengo A y NOT A, puedo deducir Bottom
def intro_bottom(a, not_a):
    # Verificar que una es A y la otra es NOT A
    if (not_a == ("NOT", a)) or (a == ("NOT", not_a)):
        return "BOTTOM"
    
    raise ValueError("No se cumple la contradicción necesaria para deducir Bottom")

# Eliminacion de bottom: Si tengo bottom, puedo deducir cualquier cosa
def elim_bottom(b):
    if b == "BOTTOM":
        return "phi"
    raise ValueError("No se cumple la contradicción necesaria para eliminar Bottom")

def elim_negacion(a):
    if a == f"NOT NOT {a}":
        return a
# manejo de la entrada de usuario
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
    print("8. Modus Tollens")
    print("9. Introducción a bottom")
    print("10. Eliminacion de bottom")
    print("11. Eliminacion de la negación")

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
        
        elif choice == 8:
            implication = eval(input("Ingrese la implicación (A → B): "))
            a = input("Ingrese la premisa B: ")
            result = modus_tollens(implication, a)
            print(f"Resultado: {result}")

        elif choice == 9:
            a = input("Ingrese la primer premisa: ")
            b = input("Ingrese la segunda premisa: ")
    
             # Convertir la entrada "NOT X" a una tupla ("NOT", "X") si se usa este formato
            if b.startswith("NOT "):
                b = ("NOT", b[4:])  # convierte "NOT A" a ("NOT", "A")
            elif a.startswith("NOT "):
                a = ("NOT", a[4:])  # convierte "NOT A" a ("NOT", "A")
            
            result = intro_bottom(a, b)
            print(f"Resultado: {result}")

        elif choice == 10:
            a = input("Ingrese la primer premisa: ")
            
            result = elim_bottom(a)
            print(f"Resultado: {result}")  
        
        elif choice == 11:
            a = input("Ingrese la primer premisa: ")
            
            result = elim_negacion(a)
            print(f"Resultado: {result}")  
        
        else:
            print("Opción no válida.")
    
    except ValueError as e:
        print(f"Error: {e}")


main()
