# Programación funcional en python
import sys

def main():
    
    argc = len(sys.argv)
    argv = sys.argv
    
    print(f'Hola, {argv[1]}')
    
    return

if __name__ == '__main__':
    main()