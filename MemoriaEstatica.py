calificaciones = []

for i in range(5):
    try:
        calificacion = int(input("Captura la calificación: "))
        calificaciones.append(calificacion)
    except ValueError:
        print("Por favor, ingresa un número válido.")


print("Calificaciones ingresadas:", calificaciones)
