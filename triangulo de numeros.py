def generar_triangulo():
    try:
        # Pide al usuario un número entero positivo
        n = int(input("Ingresa un número entero positivo para la base del triángulo: "))
        
        if n <= 0:
            print("El número debe ser mayor a 0.")
            return
        
        # Genera las filas del triángulo
        for i in range(1, n + 1):
            # Imprime los números desde 1 hasta i en la misma línea
            fila = " ".join(str(x) for x in range(1, i + 1))
            print(fila)
            
    except ValueError:
        print("Por favor, ingresa un número entero válido.")

# Ejecutar la función
generar_triangulo()