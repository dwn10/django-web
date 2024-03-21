# Resumen:

- Este código de Python está diseñado para apagar automáticamente la computadora después de un tiempo establecido por el usuario, brindando la posibilidad de cancelar el apagado antes de que ocurra.



## Explicación paso a paso:

## Importación:

- `import subprocess:` Importa el módulo `subprocess` que permite ejecutar comandos del sistema operativo desde Python.

## Variables:

- `t`: Almacena el tiempo de espera en segundos (inicializado en 1 segundo).
- `s`: Almacena la respuesta del usuario para cancelar el apagado (inicializada como cadena vacía).

## Función `turnoff()`:

- Solicita al usuario el tiempo de espera para el apagado en minutos y lo convierte a segundos.
- Si el tiempo ingresado es mayor a 1 segundo:
  -- Ejecuta el comando `shutdown -s -t %d` mediante `subprocess.call()`, donde `%d` es un marcador de posición para el tiempo en segundos. Esto programa el apagado del sistema.
  -- Pregunta al usuario si desea cancelar el apagado `(Desea cancelar[s/n]:)`. La respuesta se almacena en la variable `s`.
  -- Si `s` es igual a `"s" (cancelar)`, ejecuta el comando `shutdown -a` mediante `subprocess.call()` para abortar el apagado programado.
  -- Si `s` es igual a `"n" (no cancelar)`, no se realiza ninguna acción adicional.

## Llamada a la función:

Se llama a la función `turnoff()` para iniciar el proceso de apagado automático.


