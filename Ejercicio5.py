def clasificar_calificacion(calificacion):
    if 95 <= calificacion <= 100:
        return "Calificación Excelente"
    elif 85 <= calificacion <= 94:
        return "Calificación Notable"
    elif 75 <= calificacion <= 84:
        return "Calificación Buena/Regular"
    elif 70 <= calificacion <= 74:
        return "Calificación Suficiente"
    elif 54 <= calificacion <= 65:
        return "Calificación N/A"
    else:
        return "Reprobado"

# Datos personales
nombre = "Jeronima Roque"
materia = "Inteligencia Artificial"

# Solicitar calificación al usuario
calificacion = int(input(f"{nombre}, ingrese su calificación en {materia}: "))

# Obtener la clasificación y mostrarla
resultado = clasificar_calificacion(calificacion)
print(f"\nNombre: {nombre}")
print(f"Materia: {materia}")
print(f"La calificación ingresada es: {calificacion}")
print(f"Resultado: {resultado}")
