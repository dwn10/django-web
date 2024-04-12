
# 1) pip install tqdm

import time
from tqdm import tqdm

# Definir el número total de iteraciones
total_iterations = 100

# Crear la barra de progreso
with tqdm(total=total_iterations) as pbar:
    # Simular un proceso que tarda mucho tiempo
    for i in range(total_iterations):
        time.sleep(0.2)
        pbar.update()

# Mostrar un mensaje al final del proceso
print("Proceso completado!")