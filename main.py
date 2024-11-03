import natural_deduction 

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
        choice = int(input("Elija una operación (1-11): "))
        
        if choice == 1:
            a = input("Ingrese la primera premisa (A): ")
            b = input("Ingrese la segunda premisa (B): ")
            result = natural_deduction.intro_conjunction(a, b)
            print(f"Resultado: {result}")
        
        elif choice == 2:
            formula = eval(input("Ingrese la fórmula (A ∧ B): "))
            result = natural_deduction.elim_conjunction_left(formula)
            print(f"Resultado: {result}")
        
        elif choice == 3:
            formula = eval(input("Ingrese la fórmula (A ∧ B): "))
            result = natural_deduction.elim_conjunction_right(formula)
            print(f"Resultado: {result}")
        
        elif choice == 4:
            a = input("Ingrese la primera premisa (A): ")
            b = input("Ingrese la segunda premisa (B): ")
            result = natural_deduction.intro_disjunction_left(a, b)
            print(f"Resultado: {result}")
        
        elif choice == 5:
            formula = eval(input("Ingrese la fórmula (A ∨ B): "))
            proof_a = input("Ingrese la deducción de la primera opción: ")
            proof_b = input("Ingrese la deducción de la segunda opción: ")
            result = natural_deduction.elim_disjunction(formula, proof_a, proof_b)
            print(f"Resultado: {result}")
        
        elif choice == 6:
            a = input("Ingrese la primera premisa (A): ")
            b = input("Ingrese la segunda premisa (B): ")
            result = natural_deduction.intro_implication(a, b)
            print(f"Resultado: {result}")
        
        elif choice == 7:
            implication = eval(input("Ingrese la implicación (A → B): "))
            a = input("Ingrese la premisa A: ")
            result = natural_deduction.elim_implication(implication, a)
            print(f"Resultado: {result}")
        
        elif choice == 8:
            implication = eval(input("Ingrese la implicación (A → B): "))
            a = input("Ingrese la premisa B: ")
            result = natural_deduction.modus_tollens(implication, a)
            print(f"Resultado: {result}")

        elif choice == 9:
            a = input("Ingrese la primer premisa: ")
            b = input("Ingrese la segunda premisa: ")
    
             # Convertir la entrada "NOT X" a una tupla ("NOT", "X") si se usa este formato
            if b.startswith("NOT "):
                b = ("NOT", b[4:])  # convierte "NOT A" a ("NOT", "A")
            elif a.startswith("NOT "):
                a = ("NOT", a[4:])  # convierte "NOT A" a ("NOT", "A")
            
            result = natural_deduction.intro_bottom(a, b)
            print(f"Resultado: {result}")

        elif choice == 10:
            a = input("Ingrese la primer premisa: ")
            
            result = natural_deduction.elim_bottom(a)
            print(f"Resultado: {result}")  
        
        elif choice == 11:
            a = input("Ingrese la primer premisa: ")
            
            result = natural_deduction.elim_negacion(a)
            print(f"Resultado: {result}")  
        
        else:
            print("Opción no válida.")
    
    except ValueError as e:
        print(f"Error: {e}")


main()