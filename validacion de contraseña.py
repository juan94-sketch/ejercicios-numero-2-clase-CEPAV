import re

def validar_contrasena():
    # Pide al usuario que ingrese una contraseña
    password = input("Ingresa una contraseña para validar: ")
    
    errores = []
    
    # 1. Tiene al menos 8 caracteres
    if len(password) < 8:
        errores.append("• Debe tener al menos 8 caracteres.")
    
    # 2. Contiene al menos una letra mayúscula
    if not any(c.isupper() for c in password):
        errores.append("• Debe contener al menos una letra mayúscula.")
        
    # 3. Contiene al menos una letra minúscula
    if not any(c.islower() for c in password):
        errores.append("• Debe contener al menos una letra minúscula.")
        
    # 4. Contiene al menos un número
    if not any(c.isdigit() for c in password):
        errores.append("• Debe contener al menos un número.")
        
    # 5. Contiene al menos un carácter especial
    if not re.search(r"[!@#$%^&*(),.?\":{}|<>\-_=+\[\]\\/`~]", password):
        errores.append("• Debe contener al menos un carácter especial (ej. @, #, $, etc.).")
        
    # Resultado final
    if not errores:
        print("¡Éxito! La contraseña cumple con todos los criterios de seguridad.")
    else:
        print("Error: La contraseña no cumple con los siguientes requisitos:")
        for error in errores:
            print(error)

# Ejecutar la función
validar_contrasena()