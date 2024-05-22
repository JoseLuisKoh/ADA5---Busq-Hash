

def simple_hash(key):
    return ord(key[0])

class HashTable:
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
        return None

def main():
    size = int(input("Ingrese el tamaño de la tabla hash: "))
    hash_table = HashTable(size)

    while True:
        print("\n1. Insertar elemento")
        print("2. Buscar elemento")
        print("3. Salir")
        choice = input("Ingrese su elección: ")

        if choice == '1':
            key = input("Ingrese la clave: ")
            value = input("Ingrese el valor: ")
            hash_table.insert(key, value)
            print("Elemento insertado correctamente.")
        elif choice == '2':
            key = input("Ingrese la clave a buscar: ")
            result = hash_table.search(key)
            if result:
                print("El valor asociado a la clave {} es: {}".format(key, result))
            else:
                print("Clave no encontrada en la tabla.")
        elif choice == '3':
            print("Saliendo del programa.")
            break
        else:
            print("Opción inválida. Por favor, ingrese 1, 2 o 3.")

if __name__ == "__main__":
    main()
