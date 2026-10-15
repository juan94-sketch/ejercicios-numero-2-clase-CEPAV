#Solicitar una frase al usuario
frase = input("Ingresa una frase: ")

# Definir las vocales (incluyendo minúsculas, mayúsculas y acentos por si acaso)
vocales = "aeiouáéíóúAEIOUÁÉÍÓÚ"

# Inicializar el contador en cero
contador = 0

# Recorrer cada carácter de la frase ingresada
for caracter in frase:
    if caracter in vocales:
        contador += 1

# Mostrar el resultado final al usuario
print(f"La cantidad total de vocales en la frase es: {contador}")