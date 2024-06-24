from datetime import date, time, datetime
from decimal import Decimal

def identify_data_type(input_data):
    """Identifies the data type of the input and provides an explanation."""

    data_types = {
        str: "Cadena de texto (string): Secuencia de caracteres.",
        int: "Número entero (int): Número sin decimales.",
        float: "Número de punto flotante (float): Número con decimales.",
        Decimal: "Número decimal (Decimal): Representación precisa de decimales.",
        date: "Fecha (date): Representa una fecha específica (año, mes, día).",
        time: "Hora (time): Representa una hora específica (hora, minuto, segundo).",
        datetime: "Fecha y hora (datetime): Combina fecha y hora.",
    }

    for data_type, explanation in data_types.items():
        if isinstance(input_data, data_type):
            return f"Tipo de dato: {data_type.__name__}\nExplicación: {explanation}"

    return "Tipo de dato no reconocido"

while True:
    user_input = input("Introduce un valor (o escribe 'salir' para terminar): ")
    if user_input.lower() == "salir":
        break

    try:
        # Intenta convertir la entrada a diferentes tipos de datos
        # Primero, intenta convertir a fecha o fecha y hora
        for fmt in ["%Y-%m-%d", "%Y-%m-%d %H:%M:%S", "%H:%M:%S"]:
            try:
                converted_input = datetime.strptime(user_input, fmt)
                if fmt == "%H:%M:%S":
                    converted_input = converted_input.time()
                break  # Sale del bucle si la conversión es exitosa
            except ValueError:
                pass  # Si falla la conversión, intenta el siguiente formato

        # Si no se pudo convertir a fecha o fecha y hora, intenta otros tipos
        else:
            converted_input = eval(user_input)  # Use eval with caution in production
    except (NameError, SyntaxError, ValueError):
        converted_input = user_input  # Si no se puede convertir, asume que es una cadena

    result = identify_data_type(converted_input)
    print(result) 


