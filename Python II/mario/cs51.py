def get_int(mensaje):
    
    while True:
        
        try:
            numero = int(input(mensaje))
            break
        except:
            continue
    
    return numero