
import random

def piedra_papel_tijera():
    opciones = ["piedra", "papel", "tijera"]
    print("--- Piedra, Papel o Tijera ---")
    
    usuario = input("Elige piedra, papel o tijera: ").strip().lower()
    if usuario not in opciones:
        print("Opción no válida. Inténtalo de nuevo.")
        return
    
    computadora = random.choice(opciones)
    print(f"La computadora eligió: {computadora}")
    
    if usuario == computadora:
        print("¡Es un empate!")
    elif (usuario == "piedra" and computadora == "tijera") or \
         (usuario == "papel" and computadora == "piedra") or \
         (usuario == "tijera" and computadora == "papel"):
        print("¡Ganaste!")
    else:
        print("¡Perdiste!")

if __name__ == "__main__":
    piedra_papel_tijera()