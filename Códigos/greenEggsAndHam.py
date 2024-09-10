# Obtener las palabras del cuento Green Eggs and Ham (GEH.txt) de Dr. Seuss y contar cuántas veces aparece cada palabra.
def read_file(file):
    with open(file, 'r') as f:
        return f.read()
    
def get_words(text, words):
    for word in text.split():
        word = word.lower()
        if word in words:
            words[word] += 1
        else:
            words[word] = 1
        
def show_words(words):
    for word, count in words.items():
        print(f'{word}: {count}')

def main():
    # Leer el archivo
    GEH = read_file('GEH.txt')
    # Crear un diccionario
    words = {}
    # Separar las palabras
    get_words(GEH, words)
    # Imprimir las palabras
    show_words(words)
    print('\n')
    print(words)
    print('\n')
    print("Número de palabras en el cuento: " , len(words))
    
main()