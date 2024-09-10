# Obtener las palabras del cuento Green Eggs and Ham (GEH.txt) de Dr. Seuss y contar cuántas veces aparece cada palabra.

# Importación de librerías
import matplotlib.pyplot as plt

# Definición de funciones
def read_file(file):
    with open(file, 'r') as f:
        return f.read()
        f.close()
    
def get_words(text, words):
    text = text.lower()
    for word in text.split():
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
    
    # Histograma de las palabras del cuento, en orden de mayor a menor concurrencia
    sorted_words = dict(sorted(words.items(), key=lambda item: item[1], reverse=True))
    plt.bar(sorted_words.keys(), sorted_words.values())
    plt.xticks(rotation=90)
    plt.tight_layout(pad=0.4, w_pad=10, h_pad=1.0)
    plt.show()
    
main()
