from cs51 import *

altura = 0

while altura > 8 or altura < 1:
    altura = get_int('Ingrese la altura: ')
    
for i in range(1, altura + 1):
    print(' ' * (altura - i) + '#' * i + '  ' + '#' * i)