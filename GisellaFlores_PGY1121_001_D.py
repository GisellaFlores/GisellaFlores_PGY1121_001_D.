def mostrar_ubicaciones(ubicaciones):
    print("")
    print("Ubicaciones disponibles:")
    for i in range(len(ubicaciones)):
        if i % 10 == 0:
            print()
        if ubicaciones[i] == 0:
            print(i + 1, end=" ")
        else:
            print("X", end=" ")
    print("\n")

def comprar_entradas(ubicaciones, precios, asistentes):
    cantidad = int(input("¿Cuántas entradas desea comprar? (1-3): "))
    if cantidad < 1 or cantidad > 3:
        print("Cantidad inválida. Intente nuevamente.")
        return

    entradas_compradas = 0
    while entradas_compradas < cantidad:
        mostrar_ubicaciones(ubicaciones)
        ubicacion = int(input("Seleccione una ubicación: "))
        if ubicacion < 1 or ubicacion > 100:
            print("Ubicación inválida. Intente nuevamente.")
            continue

        if ubicaciones[ubicacion - 1] == 1:
            print("Esta ubicación no está disponible. Seleccione otra.")
        else:
            ubicaciones[ubicacion - 1] = 1
            precio = obtener_precio(precios, ubicacion)
            run = input("Ingrese el RUN de la persona: ")
            asistentes[ubicacion - 1] = run
            print("Ubicación", ubicacion, "comprada por $", precio)
            entradas_compradas += 1

def obtener_precio(precios, ubicacion):
    if ubicacion <= 20:
        return precios[0]
    elif ubicacion <= 50:
        return precios[1]
    else:
        return precios[2]

def mostrar_asistentes(asistentes):
    print("")
    print("Listado de asistentes:")
    asistentes_ordenados = sorted(asistentes)
    for run in asistentes_ordenados:
        for i in range(len(asistentes)):
            if asistentes[i] == run:
                print("RUN:", run, "- Ubicación:", i + 1)
                break
    print()

def mostrar_ganancias(asistentes, precios):
    tipos_entradas = ["Platinum", "Gold", "Silver"]
    cantidad_entradas = [0] * 3
    total_ganancias = 0

    for i in range(len(asistentes)):
        if asistentes[i] != "":
            precio = obtener_precio(precios, i + 1)
            total_ganancias += precio
            if i + 1 <= 20:
                cantidad_entradas[0] += 1
            elif i + 1 <= 50:
                cantidad_entradas[1] += 1
            else:
                cantidad_entradas[2] += 1

    print("Ganancias totales:")
    print("")
    total_final = 0
    total_cantidad_entradas = 0
    for i in range(3):
        total_tipo_entrada = cantidad_entradas[i] * precios[i]
        print("* ", tipos_entradas[i], "- Cantidad:", cantidad_entradas[i], "- Total:", total_tipo_entrada)
        total_final += total_tipo_entrada
        total_cantidad_entradas += cantidad_entradas[i]
    print("")
    print("TOTAL:", total_cantidad_entradas, " - ", total_final)
    print()

def main():
    ubicaciones = [0] * 100
    precios = [120000, 80000, 50000]
    asistentes = [""] * 100

    while True:
        print("")
        print("***************** MENÚ *****************")
        print("1. Comprar entradas")
        print("2. Mostrar ubicaciones disponibles")
        print("3. Ver listado de asistentes")
        print("4. Mostrar ganancias totales")
        print("5. Salir")
        opcion = int(input("Introduzca una opción: "))

        if opcion == 1:
            comprar_entradas(ubicaciones, precios, asistentes)
        elif opcion == 2:
            mostrar_ubicaciones(ubicaciones)
        elif opcion == 3:
            mostrar_asistentes(asistentes)
        elif opcion == 4:
            mostrar_ganancias(asistentes, precios)
        elif opcion == 5:
            print("")
            print("¡Gracias por su compra!")
            print("Gisella Flores T.")
            print("10/7/2023")
            print("")
            break
        else:
            print("Opción inválida. Intente nuevamente.")
if __name__ == "__main__":
    main()
