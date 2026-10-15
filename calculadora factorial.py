def calcular_factorial():
    try:
        n = int(input("Ingresa un número entero no negativo: "))
        if n < 0:
            print("El número debe ser no negativo.")
            return
        
        factorial = 1
        for i in range(1, n + 1):
            factorial *= i
        
        print(f"El factorial de {n} es: {factorial}")
    except ValueError:
        print("Por favor, introduce un número entero válido.")

if __name__ == "__main__":
    calcular_factorial()