# 1. Abstracción

class Persona:
    
    nombre = ''
    __password = ''
    edad = ''
    
    def __decir_edad(self):
        return f'Mi edad es {self.edad}'

# 2. Encapsulación (Privado, Pública)
# 3. Herencia 

class Animal:
    raza = ''
    edad = ''
    
    def emitir_sonido(self):
        return
    
class Gato(Animal):
    nombre = ''
    
    def caer_de_pie(self):
        return
    
class Perro(Animal):
    nombre = ''
    
    def superolfato(self):
        return

# Polimorfismo