class Nodo:
    def __init__(self, valor):  # Constructor correcto
        self.valor = valor
        self.siguiente = None

# Crear nodos con valores ingresados por el usuario
nodo1 = Nodo(int(input("Introduce el valor del primer nodo: ")))
nodo2 = Nodo(int(input("Introduce el valor del segundo nodo: ")))
nodo3 = Nodo(int(input("Introduce el valor del tercer nodo: ")))
nodo4 = Nodo(int(input("Introduce el valor del cuarto nodo: ")))  # Corregido el mensaje

# Enlazar los nodos
nodo1.siguiente = nodo2
nodo2.siguiente = nodo3
nodo3.siguiente = nodo4

# Mostrar los valores de la lista enlazada
print("\nValores de la lista enlazada:")
print(nodo1.valor, "->", nodo1.siguiente.valor, "->", nodo1.siguiente.siguiente.valor, "->", nodo1.siguiente.siguiente.siguiente.valor)
