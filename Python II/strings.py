cadena = 'Hola a todos'

# # Hace que el primer carácter sea mayúsculo
# print(cadena.capitalize())
# # Hace toda la cadena mayúscula
# print(cadena.upper())
# # Hace toda la cadena minúscula
# print(cadena.lower())
#

palabra = 'Hola a todas las personas.'
frases = 0
caracteres = 0
for letra in palabra:
    if letra == '.' or letra == '!' or letra == '?':
        frases += 1
        
    elif letra.isalpha():
        caracteres += 1
        
print(f'La cantidad de frases es: {frases}, letras = {caracteres}')

# string = 'hola5'
# print(string.isalpha())
print(len('88888888'))