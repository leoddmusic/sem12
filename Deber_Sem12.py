# Crear una matriz 3D para almacenar datos de temperaturas
# Primera dimensión: Ciudades (3 ciudades)
# Segunda dimensión: Semanas (4 semanas)
# Tercera dimensión: Días de la semana (7 días)
temperaturas = [
    [   # Ciudad 1
        [78, 80, 82, 79, 85, 88, 92],  # Semana 1
        [76, 79, 83, 81, 87, 89, 93],  # Semana 2
        [77, 81, 85, 82, 88, 91, 95],  # Semana 3
        [75, 78, 80, 79, 84, 87, 91]   # Semana 4
    ],
    [   # Ciudad 2
        [62, 64, 68, 70, 73, 75, 79],  # Semana 1
        [63, 66, 70, 72, 75, 77, 81],  # Semana 2
        [61, 65, 68, 70, 72, 76, 80],  # Semana 3
        [64, 67, 69, 71, 74, 77, 80]   # Semana 4
    ],
    [   # Ciudad 3
        [90, 92, 94, 91, 88, 85, 82],  # Semana 1
        [89, 91, 93, 90, 87, 84, 81],  # Semana 2
        [91, 93, 95, 92, 89, 86, 83],  # Semana 3
        [88, 90, 92, 89, 86, 83, 80]   # Semana 4
    ]
]

# Calcular el promedio de temperaturas para cada ciudad y semana
for i, ciudad in enumerate(temperaturas):
    for j, semana in enumerate(ciudad):
        promedio_semana = sum(semana) / len(semana)
        print(f"Promedio de temperaturas para Ciudad {i+1}, Semana {j+1}: {promedio_semana:.2f}°C")
