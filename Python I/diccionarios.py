diccionario = {
    'clave' : 'Valor',
    'colores' : ('rojo','verde','azul'),
    'nombres' : list()
}

print(diccionario['colores'])
for color in (diccionario['colores']):
    print(color)
    
diccionario['nombres'].append("Oscar")
print(diccionario["nombres"][0])

diccionario['cs50profes'] = ['Eloisse', 'Adilia', 'Mike']

print(diccionario)