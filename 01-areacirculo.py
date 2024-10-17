# Definir una función para calcular el área de un círculo
def calcular_area(radio):
    # La fórmula del área del círculo es π * radio^2
    return 3.1416 * radio * radio

# Pedir al usuario que ingrese el radio del círculo
radio = float(input("Ingrese el radio del círculo: "))

# Calcular el área usando la función
area = calcular_area(radio)

# Mostrar el resultado
print("El área del círculo es:", area)
