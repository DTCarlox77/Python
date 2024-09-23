from cs50 import get_int

def main():
    
    altura = 0
    
    while altura < 1 or altura > 8:
        altura = get_int('height: ')
        
    generar_bloques(altura)

def generar_bloques(altura):
    
    for i in range(altura):
        
        print(' ' * (altura - (i + 1)) + '#' * (i + 1))

if __name__ == '__main__':
    main()