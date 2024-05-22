


def simple_hash(key):
    return ord(key[0])

class Dictionary:
    def __init__(self, size):
        self.size = size
        self.table = [[] for _ in range(size)]

    def insert(self, key, value):
        index = simple_hash(key) % self.size
        self.table[index].append((key, value))

    def search(self, key):
        index = simple_hash(key) % self.size
        for k, v in self.table[index]:
            if k == key:
                return v
        return "Palabra no encontrada en el diccionario."

def main():
    size = int(input("Ingrese el tamaño del diccionario: "))
    dictionary = Dictionary(size)

    print("Bienvenido al diccionario interactivo.")
    print("Por favor, ingrese las palabras y sus significados.")

    while True:
        word = input("Palabra: ")
        meaning = input("Significado: ")
        dictionary.insert(word, meaning)

        another = input("¿Desea agregar otra palabra? (s/n): ")
        if another.lower() != 's':
            break

    print("\nBúsqueda de significados:")
    while True:
        search_word = input("Ingrese la palabra para buscar su significado (o 'salir' para terminar): ")
        if search_word.lower() == 'salir':
            print("Saliendo del diccionario.")
            break
        else:
            result = dictionary.search(search_word)
            print(result)

if __name__ == "__main__":
    main()
