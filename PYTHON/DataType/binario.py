def decimal_a_binario(decimal):
    """Convierte un número decimal a binario."""
    if decimal == 0:
        return '0'

    binario = ''
    while decimal > 0:
        residuo = decimal % 2
        binario = str(residuo) + binario
        decimal //= 2
    return binario

def main():
    """Función principal para interactuar con el usuario."""

    while True:
        try:
            numero_decimal = int(input("Ingrese un número decimal: "))
            if numero_decimal < 0:
                raise ValueError("Por favor, ingrese un número decimal no negativo.")

            resultado_binario = decimal_a_binario(numero_decimal)
            print(f"El equivalente binario de {numero_decimal} es: {resultado_binario}")

            break  # Salir del bucle si la entrada es válida

        except ValueError as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    main()
