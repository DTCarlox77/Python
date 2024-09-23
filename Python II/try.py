# try:
#     edad = int(input("Ingresa tu edad: "))
# except:
#     print("La edad no es válida.")
    

try:
    edad = int(input("Ingresa tu edad: "))
    edad = edad / 0
except ZeroDivisionError:
    print("No se puede dividir entre 0.")
except ValueError:
    print("El valor no es válido")
except Exception as e:
    print(f'Hubo un error: {e}')
finally:
    print("El programa ha terminado")