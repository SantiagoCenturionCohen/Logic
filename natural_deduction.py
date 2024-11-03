

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
    return (a, "->", b)

# Eliminación de implicación (Modus Ponens): Si tengo A → B y A, puedo deducir B
def elim_implication(implication, a):
    if implication[1] == "->" and implication[0] == a:
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
# Eliminacion de la negacion: si tengo doble negacion de A, tengo A
def elim_negacion(a):
    if a == f"NOT NOT {a}":
        return a
# manejo de la entrada de usuario

