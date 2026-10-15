#adivina el numero
import random

def adivina_el_numero():
    """Juego para adivinar un número entre 1 y 100."""
    numero_secreto = random.randint(1, 100)
    print("🎯 ¡He pensado en un número entre 1 y 100! Adivina cuál es.")

    while True:
        try:
            # Solicitar número al usuario
            intento = int(input("👉 Ingresa tu número: "))
            
            # Validar rango
            if intento < 1 or intento > 100:
                print("⚠️ El número debe estar entre 1 y 100.")
                continue

        except ValueError:
            print("❌ Por favor, introduce un número entero válido.")
            continue

        # Comparar con el número secreto
        if intento < numero_secreto:
            print("📈 El número secreto es mayor.")
        elif intento > numero_secreto:
            print("📉 El número secreto es menor.")
        else:
            print(f"🎉 ¡Felicidades! Adivinaste el número {numero_secreto}.")
            break

