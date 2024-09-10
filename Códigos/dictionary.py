# Programa de ejemplo sobre el uso de diccionarios
# Por: Maximiliano De La Cruz Lima
# Creado: 10/Septiembre/2024

# Crear un diccionario
phonebook = {'Chris': '555-1111', 'Katie': '555-2222', 'Joanne': '555-3333'}

print(phonebook)

# Acceder a un valor en el diccionario
print(phonebook['Chris'])

if 'Chris' in phonebook:
    print('Chris' in phonebook)
if 'Carlos' in phonebook:
    print('Carlos' in phonebook)
    
# Agregar un nuevo elemento al diccionario
phonebook['Carlos'] = '555-4444'

# Eliminar un elemento del diccionario
del phonebook['Carlos']