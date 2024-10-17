# Definir una función para convertir Celsius a Fahrenheit
def celsius_a_fahrenheit(celsius):
    # La fórmula de conversión es (C * 9/5) + 32
    return (celsius * 9/5) + 32

# Pedir al usuario que ingrese la temperatura en grados Celsius
celsius = float(input("Ingrese la temperatura en grados Celsius: "))

# Convertir la temperatura a Fahrenheit usando la función
fahrenheit = celsius_a_fahrenheit(celsius)

# Mostrar el resultado
print("La temperatura en grados Fahrenheit es:", fahrenheit)

