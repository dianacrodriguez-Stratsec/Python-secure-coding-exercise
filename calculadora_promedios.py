def ingresar_calificaciones():
    materias = []
    calificaciones = []

    while True:
        materia = input("Ingrese el nombre de la materia: ").strip()
        if not materia:
            print("El nombre de la materia no puede estar vacío.")
            continue

        try:
            nota = float(input(f"Ingrese la calificación de {materia} (0-10): "))
            if nota < 0 or nota > 10:
                print("La calificación debe estar entre 0 y 10.")
                continue
        except ValueError:
            print("Debe ingresar un número válido para la calificación.")
            continue

        materias.append(materia)
        calificaciones.append(nota)

        continuar = input("¿Desea ingresar otra materia? (s/n): ").strip().lower()
        if continuar != "s":
            break

    return materias, calificaciones


def calcular_promedio(calificaciones):
    if not calificaciones:
        return 0

    promedio = sum(calificaciones) / len(calificaciones)
    return promedio


def determinar_estado(calificaciones, umbral=5.0):
    aprobadas = []
    reprobadas = []

    for i, nota in enumerate(calificaciones):
        if nota >= umbral:
            aprobadas.append(i)
        else:
            reprobadas.append(i)

    return aprobadas, reprobadas


def encontrar_extremos(calificaciones):
    if not calificaciones:
        return None, None

    indice_max = calificaciones.index(max(calificaciones))
    indice_min = calificaciones.index(min(calificaciones))

    return indice_max, indice_min


def main():
    print("Bienvenida a la calculadora de Promedios")
    materias, calificaciones = ingresar_calificaciones()

    if not materias:
        print("No se ingresaron materias. El programa finalizará.")
        return

    promedio = calcular_promedio(calificaciones)
    aprobadas, reprobadas = determinar_estado(calificaciones)
    indice_max, indice_min = encontrar_extremos(calificaciones)

    print("\nRESUMEN FINAL")
    print("-------------------")

    print("\nMaterias y calificaciones:")
    for i in range(len(materias)):
        print(f"- {materias[i]}: {calificaciones[i]}")

    print(f"\nPromedio general: {promedio:.2f}")

    print("\nMaterias aprobadas:")
    if aprobadas:
        for i in aprobadas:
            print(f"{materias[i]} ({calificaciones[i]})")
    else:
        print("Ninguna materia aprobada.")

    print("\nMaterias reprobadas:")
    if reprobadas:
        for i in reprobadas:
            print(f"{materias[i]} ({calificaciones[i]})")
    else:
        print("Ninguna materia reprobada.")

    print(f"\n📈 Mejor calificación: {materias[indice_max]} ({calificaciones[indice_max]})")
    print(f"📉 Peor calificación: {materias[indice_min]} ({calificaciones[indice_min]})")

    print("\nGracias por usar la calculadora de promedios. ¡Hasta pronto!")


if __name__ == "__main__":
    main()